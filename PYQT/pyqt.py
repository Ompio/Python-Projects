from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QAction

from PYQT.modules.Z1 import Zakladka1
from PYQT.modules.Z2 import Zakladka2
from PYQT.modules.Z3 import Zakladka3


# Tworzenie klasy głównego okna aplikacji dziedziczącej po QMainWindow

class Window(QMainWindow):
    # Dodanie konstruktora przyjmującego okno nadrzędne
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt6 Lab')
        self.setGeometry(100, 100, 500, 500)
        self.createTabs()
        self.createMenu()

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
        actionOpen = QAction('Open', self)
        actionOpen.triggered.connect(self.tab_1.wybierz_i_wyswietl)
        self.t1Menu.addAction(actionOpen)

    def createT2Menu(self):
        self.t2Menu = self.menu.addMenu("Task2")

        actionClear = QAction('Clear', self)
        actionClear.triggered.connect(self.tab_2.wyczysc)
        self.t2Menu.addAction(actionClear)

        actionOpen = QAction('Open', self)
        actionOpen.triggered.connect(self.tab_2.wybierz_i_wyswietl)
        self.t2Menu.addAction(actionOpen)

        actionSave = QAction('Save', self)
        actionSave.triggered.connect(self.tab_2.zapisz)
        self.t2Menu.addAction(actionSave)

        actionSaveAs = QAction('Save as', self)
        actionSaveAs.triggered.connect(self.tab_2.zapisz_jako)
        self.t2Menu.addAction(actionSaveAs)


    def createT3Menu(self):
        self.t3Menu = self.menu.addMenu("Task3")
        actionClear = QAction('Clear', self)
        actionClear.triggered.connect(self.tab_3.clear)
        self.t3Menu.addAction(actionClear)

    # Funkcja dodająca wenętrzeny widżet do okna
    def createTabs(self):
        # Tworzenie widżetu posiadającego zakładki
        self.tabs = QTabWidget()

        # Stworzenie osobnych widżetów dla zakładek
        self.tab_1 = Zakladka1()
        self.tab_2 = Zakladka2()
        self.tab_3 = Zakladka3()

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

