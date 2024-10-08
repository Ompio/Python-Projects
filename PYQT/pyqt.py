# 3.1
from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QStatusBar
from PyQt6.QtWidgets import QToolBar
from PyQt6.QtGui import QIcon, QAction

from PYQT.Z1 import Zakladka1
from PYQT.Z2 import Zakladka2


# Tworzenie klasy głównego okna aplikacji dziedziczącej po QMainWindow

class Window(QMainWindow):
    # Dodanie konstruktora przyjmującego okno nadrzędne
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt6 Lab')
        self.setGeometry(100, 100, 500, 500)
        self.createMenu()
        self.createTabs()

    # Funkcja dodająca pasek menu do okna
    def createMenu(self):
        # Stworzenie paska menu
        self.menu = self.menuBar()
        self.createFileMenu()
        self.createT1Menu()
        self.createT2Menu()
        self.createT3Menu()

    def createFileMenu(self):
        # Dodanie do paska listy rozwijalnej o nazwie File
        self.fileMenu = self.menu.addMenu("File")
        # Dodanie do menu File pozycji zamykającej aplikacje
        self.actionExit = QAction('Exit', self)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.triggered.connect(self.close)
        self.fileMenu.addAction(self.actionExit)

    def createT1Menu(self):
        self.t1Menu = self.menu.addMenu("Task1")

    def createT2Menu(self):
        self.t2Menu = self.menu.addMenu("Task2")

    def createT3Menu(self):
        self.t3Menu = self.menu.addMenu("Task3")

    # Funkcja dodająca wenętrzeny widżet do okna
    def createTabs(self):
        # Tworzenie widżetu posiadającego zakładki
        self.tabs = QTabWidget()

        # Stworzenie osobnych widżetów dla zakładek
        self.tab_1 = Zakladka1()
        self.tab_2 = Zakladka2()
        self.tab_3 = QWidget()

        # Dodanie zakładek do widżetu obsługującego zakładki
        self.tabs.addTab(self.tab_1, "Zakładka1")
        self.tabs.addTab(self.tab_2, "Zakładka2")
        self.tabs.addTab(self.tab_3, "Zakładka3")

        # Dodanie widżetu do głównego okna jako centralny widżet
        self.setCentralWidget(self.tabs)


# Uruchomienie okna
app = QApplication([])
win = Window()
win.show()
app.exec()

