from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, session
from flask_login import LoginManager
from flask_session import Session
import sqlite3


app = Flask("Flask - Lab")
sess = Session()
DATABASE = 'database.db'

def initialize_database():
    # Tworzenie tabeli 'users' i 'books', jeśli nie istnieją
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()

        # Tabela użytkowników
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                is_admin INTEGER NOT NULL DEFAULT 0
            )
        ''')

        # Tabela książek
        cur.execute('''
            CREATE TABLE IF NOT EXISTS books (
                ksiazka TEXT,
                autor TEXT
            )
        ''')

        # Dodanie administratora, jeśli tabela 'users' jest pusta
        cur.execute("SELECT COUNT(*) FROM users")
        if cur.fetchone()[0] == 0:
            print("Dodawanie użytkownika 'admin'...")
            cur.execute(
                "INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)",
                ('admin', 'admin123', 1)
            )
        con.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user' in session:
        con = sqlite3.connect(DATABASE)

        # Pobranie danych z tabeli
        cur = con.cursor()
        cur.execute("select * from books")
        books = cur.fetchall()

        return render_template('main.html', books=books, is_admin=session['is_admin'])
    else:
        return render_template('login.html')


@app.route('/add', methods=['POST'])
def add():
        autor = request.form['autor']
        ksiazka = request.form['ksiazka']

        if not autor.strip() or not ksiazka.strip():
            return "Wprowadź poprawne dane!"

        # Dodanie użytkownika do bazy danych
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute("INSERT INTO books (autor,ksiazka) VALUES (?,?)", (autor, ksiazka) )
        con.commit()
        con.close()

        return "Dodano ksiażkę do bazy danych <br>" + index()

@app.route('/user/<identifier>', methods=['GET'])
def view_user(identifier):
    if 'user' not in session or session['user'] != 'admin':
        return "Brak dostępu: Musisz być administratorem! <br> <a href='/'>Powrót do strony głównej</a>", 403

    try:
        user_id = int(identifier)
        query = "SELECT * FROM users WHERE id = ?"
        params = (user_id,)
    except ValueError:
        query = "SELECT * FROM users WHERE username = ?"
        params = (identifier,)

    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(query, params)
        user = cur.fetchone()

    if not user:
        return f"Użytkownik o identyfikatorze '{identifier}' nie istnieje. <br> <a href='/manage_users'>Powrót do listy użytkowników</a>", 404

    return render_template('user.html', user=user)


@app.route('/manage_users', methods=['GET', 'POST'])
def manage_users():
    # Sprawdzenie, czy użytkownik jest zalogowany jako administrator
    if 'user' not in session or session['is_admin'] == 0:
        return "Brak dostępu: Musisz być administratorem! <br> <a href='/'>Powrót do strony głównej</a>", 403

    # Obsługa dodawania użytkownika
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_admin = request.form.get('is_admin') == 'on'  # Checkbox zwraca 'on', jeśli zaznaczony

        # Walidacja danych wejściowych
        if not username.strip() or not password.strip():
            return "Nazwa użytkownika i hasło są wymagane! <br> <a href='/manage_users'>Powrót</a>", 400

        # Dodanie użytkownika do bazy danych
        try:
            with sqlite3.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)",
                    (username, password, 1 if is_admin else 0)
                )
                con.commit()
        except sqlite3.IntegrityError:
            return "Użytkownik o tej nazwie już istnieje! <br> <a href='/manage_users'>Powrót</a>", 400

    # Pobranie listy użytkowników
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("SELECT id, username, is_admin FROM users")
        users = cur.fetchall()

    return render_template('admin_users.html', users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Połączenie z bazą danych
        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()

            # Sprawdzenie, czy użytkownik istnieje w bazie
            cur.execute("SELECT id, username, is_admin FROM users WHERE username = ?", (username,))
            user = cur.fetchone()

            if user:
                # Użytkownik istnieje - sprawdzamy hasło
                cur.execute("SELECT password FROM users WHERE username = ?", (username,))
                stored_password = cur.fetchone()[0]

                if stored_password == password:
                    session['user'] = username
                    session['is_admin'] = bool(user[2])
                    return redirect(url_for('index'))
                else:
                    return "Nieprawidłowe hasło! <br> <a href='/login'>Spróbuj ponownie</a>"
            else:
                # Użytkownik nie istnieje - dodajemy go do bazy
                cur.execute(
                    "INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)",
                    (username, password, 0)  # Domyślnie brak uprawnień administratora
                )
                con.commit()

                # Automatyczne logowanie nowego użytkownika
                session['user'] = username
                session['is_admin'] = False
                return "Nowy użytkownik został dodany i zalogowany! <br> <a href='/'>Przejdź do strony głównej</a>"

    return render_template('login.html')



@app.route('/logout', methods=['GET'])
def logout():
    # Jeżeli sesja klienta istnieje - usunięcie sesji
    if 'user' in session:
        session.pop('user')
    else:
        # Przekierowanie klienta do strony początkowej
        redirect(url_for('index'))

    return "Wylogowano <br>  <a href='/'> Powrót </a>"


if __name__ == '__main__':
    initialize_database()
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.config.from_object(__name__)
    app.run(debug=True)


