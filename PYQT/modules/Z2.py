from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QLabel, QFileDialog, QLineEdit


class Zakladka2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Zakladka2')
        self.fileName = ""

        button = QPushButton("Wybierz plik do odczytu")
        button.clicked.connect(self.wybierz_i_wyswietl)

        saveButton = QPushButton("Zapisz")
        saveButton.clicked.connect(self.zapisz)

        clearButton = QPushButton("Wyczyść")
        clearButton.clicked.connect(self.wyczysc)

        layout = QGridLayout()
        # Tworzenie prostego tekstu do wyświetlenia
        self.text_1 = QLineEdit()
        # Tworzenie drugiego tekstu do wyświetlenia
        # Dodanie pierwszego elementu do layoutu - do lewego górnego rogu
        layout.addWidget(self.text_1, 1, 0)
        # Dodanie przycisku do layoutu
        layout.addWidget(button, 0, 0)
        layout.addWidget(saveButton, 0, 1)
        layout.addWidget(clearButton, 0, 2)
        self.setLayout(layout)

    def wyczysc(self):
        self.text_1.clear()

    def zapisz(self):
        with open(self.fileName, 'w') as plik:
            plik.write(self.text_1.text())

    def zapisz_jako(self):
        self.fileName, selectedFilter = QFileDialog.getOpenFileName(self, "Wybierz plik obrazu",
                                                                    "Początkowa nazwa pliku",
                                                                    "All Files (*);;Python Files (*.py);; PNG (*.png)")

        with open(self.fileName, 'w') as plik:
            plik.write(self.text_1.text())

    def wybierz_i_wyswietl(self):
        self.fileName, selectedFilter = QFileDialog.getOpenFileName(self, "Wybierz plik obrazu", "Początkowa nazwa pliku",
                                                               "All Files (*);;Python Files (*.py);; PNG (*.png)")

        # Jeżeli nazwa została zwrócona (użytkownik wybrał plik) - wyświetlenie nazwy
        if self.fileName:
            with open(self.fileName, 'r') as plik:
                zawartosc = plik.read()

            self.text_1.setText(zawartosc)

