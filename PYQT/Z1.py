from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QPushButton, QMessageBox, QGridLayout
from PyQt6.QtGui import QPixmap
class Zakladka1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Zakladka1')


        button = QPushButton("To jest przycisk")
        button.clicked.connect(self.wybierz_i_wyswietl)
        layout = QGridLayout()
        # Tworzenie prostego tekstu do wyświetlenia
        self.label1 = QLabel("")

        # Tworzenie drugiego tekstu do wyświetlenia
        # Dodanie pierwszego elementu do layoutu - do lewego górnego rogu
        layout.addWidget(self.label1, 1, 0)

        # Dodanie przycisku do layoutu
        layout.addWidget(button, 0, 0)
        self.setLayout(layout)

    def wybierz_i_wyswietl(self):
        fileName, selectedFilter = QFileDialog.getOpenFileName(self, "Wybierz plik obrazu", "Początkowa nazwa pliku",
                                                               "All Files (*);;Python Files (*.py);; PNG (*.png)")
        # Jeżeli nazwa została zwrócona (użytkownik wybrał plik), wyświetlenie obrazu za pomocą QPixmap
        if fileName:
            pixmap = QPixmap(fileName).scaled(self.size())
            self.label1.setPixmap(pixmap)


