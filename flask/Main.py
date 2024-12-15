from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, session
from flask_login import LoginManager
from flask_session import Session
import sqlite3


app = Flask("Flask - Lab")
sess = Session()
DATABASE = 'database.db'



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template('login.html')
@app.route('/create_database', methods=['GET', 'POST'])
def create_db():
    # Połączenie sie z bazą danych
    conn = sqlite3.connect(DATABASE)
    # Stworzenie tabeli w bazie danych za pomocą sqlite3
    conn.execute('CREATE TABLE books (ksiazka TEXT, autor TEXT)')
    # Zakończenie połączenia z bazą danych
    conn.close()

    return index()

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'user' in session:
        con = sqlite3.connect(DATABASE)

        # Pobranie danych z tabeli
        cur = con.cursor()
        cur.execute("select * from books")
        books = cur.fetchall()

        return render_template('main.html', books=books)
    else:
        return render_template('login.html')


@app.route('/add', methods=['POST'])
def add():
        autor = request.form['autor']
        ksiazka = request.form['ksiazka']


        # Dodanie użytkownika do bazy danych
        con = sqlite3.connect(DATABASE)
        cur = con.cursor()
        cur.execute("INSERT INTO books (autor,ksiazka) VALUES (?,?)", (autor, ksiazka) )
        con.commit()
        con.close()

        return "Dodano ksiażkę do bazy danych <br>" + index()


@app.route('/login', methods=['POST'])
def login():
    # Stworzenie sesji dla kilenta i dodanie pola user
    session['user']="username"
    return "Sesja została utworzona <br> <a href='/'> Dalej </a> "


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
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.config.from_object(__name__)
    app.run(debug=True)
