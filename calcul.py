import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class calculatrice(QWidget):
    def __init__(self,win):
        super().__init__()
        self.win=win
    
    def build(self,color):
        self.win.setWindowTitle("Calculatrice")
        self.win.setGeometry(100,100,800,800)
        self.win.setStyleSheet("background: " +color+ ";")

if __name__=='__main__':
    app=QApplication(sys.argv)
    root=QWidget()
    interface=calculatrice(root)
    interface.build("gray")
    root.show()
    sys.exit(app.exec_())