from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QSpinBox


class Zakladka3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Zakladka2')

        layout = QGridLayout()

        self.text_1 = QLineEdit()
        self.text_2 = QLineEdit()
        self.final_text = QLineEdit()


        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 100)  # Zakres od 0 do 100
        layout.addWidget(self.spin_box)

        layout.addWidget(self.text_1, 1, 0)
        layout.addWidget(self.text_2, 1, 0)
        layout.addWidget(self.spin_box, 1, 0)
        self.text_1.textChanged.connect(self.on_text_1_changed)
        self.text_2.textChanged.connect(self.on_text_1_changed)
        self.spin_box.textChanged.connect(self.on_text_1_changed)

        self.setLayout(layout)

    def on_text_1_changed(self):
        self.final_text.setText(f"{self.text_1.text()} {self.text_2.text()} {self.spin_box.text()}")
