import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

class Calculatrice(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculatrice")
        self.setGeometry(100, 100, 300, 400)
        self.setStyleSheet("background-color: #f0f0f0;")

        # Champ d'affichage
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; padding: 10px;")

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.display)

        # Grille pour les boutons
        buttons_layout = QGridLayout()

        # Boutons
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0), ('(', 4, 1), (')', 4, 2), ('⌫', 4, 3)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setStyleSheet("""
                QPushButton {
                    font-size: 18px;
                    padding: 15px;
                    background-color: #ffffff;
                    border: 1px solid #cccccc;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
                QPushButton:pressed {
                    background-color: #d0d0d0;
                }
            """)
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
            buttons_layout.addWidget(button, row, col)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

        self.current_expression = ""

    def on_button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.current_expression))
                self.display.setText(result)
                self.current_expression = result
            except:
                self.display.setText("Erreur")
                self.current_expression = ""
        elif text == 'C':
            self.current_expression = ""
            self.display.setText("")
        elif text == '⌫':
            self.current_expression = self.current_expression[:-1]
            self.display.setText(self.current_expression)
        else:
            self.current_expression += text
            self.display.setText(self.current_expression)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculatrice()
    calc.show()
    sys.exit(app.exec_())

    