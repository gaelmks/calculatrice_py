import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

class calculatrice(QWidget):
    def __init__(self,win):
        super().__init__()
        self.win=win
    
    def build(self,color):

        #fenetre
        self.win.setWindowTitle("Calculatrice")
        self.win.setGeometry(100,100,400,800)
        self.win.setStyleSheet("background: " +color+ ";")

        #champ de saisi
        self.lbl=QLineEdit(self.win)
        self.lbl.setGeometry(0, 0, 400, 300)

        #bouton 1
        self.btn1=QPushButton(self.win)
        self.btn1.setText("1")
        self.btn1.setGeometry(0,300,100, 100)

        #bouton 2
        self.btn2=QPushButton(self.win)
        self.btn2.setText("2")
        self.btn2.setGeometry(100,300,100, 100)

        #bouton 3
        self.btn3=QPushButton(self.win)
        self.btn3.setText("3")
        self.btn3.setGeometry(200,300,100, 100)

        #bouton 4
        self.btn4=QPushButton(self.win)
        self.btn4.setText("4")
        self.btn4.setGeometry(0,400, 100, 100)

        #bouton 5
        self.btn5=QPushButton(self.win)
        self.btn5.setText("5")
        self.btn5.setGeometry(100, 400, 100, 100)

        #bouton 6
        self.btn6=QPushButton(self.win)
        self.btn6.setText("6")
        self.btn6.setGeometry(200, 400, 100, 100)

if __name__=='__main__':
    app=QApplication(sys.argv)
    root=QWidget()
    interface=calculatrice(root)
    interface.build("white")
    root.show()
    sys.exit(app.exec_())

    