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
        def affiche_bouton1():
            self.lbl.insert("1")

        self.btn1=QPushButton(self.win)
        self.btn1.setText("1")
        self.btn1.setGeometry(0,300,100, 100)
        self.btn1.clicked.connect(affiche_bouton1)
        

        #bouton 2
        def affiche_bouton2():
            self.lbl.insert("2")

        self.btn2=QPushButton(self.win)
        self.btn2.setText("2")
        self.btn2.setGeometry(100,300,100, 100)
        self.btn2.clicked.connect(affiche_bouton2)

        #bouton 3
        def affiche_bouton3():
            self.lbl.insert("3")

        self.btn3=QPushButton(self.win)
        self.btn3.setText("3")
        self.btn3.setGeometry(200,300,100, 100)
        self.btn3.clicked.connect(affiche_bouton3)

        #bouton 4
        def affiche_bouton4():
            self.lbl.insert("4")

        self.btn4=QPushButton(self.win)
        self.btn4.setText("4")
        self.btn4.setGeometry(0,400, 100, 100)
        self.btn4.clicked.connect(affiche_bouton4)

        #bouton 5
        def affiche_bouton5():
            self.lbl.insert("5")

        self.btn5=QPushButton(self.win)
        self.btn5.setText("5")
        self.btn5.setGeometry(100, 400, 100, 100)
        self.btn5.clicked.connect(affiche_bouton5)

        #bouton 6
        def affiche_bouton6():
            self.lbl.insert("6")

        self.btn6=QPushButton(self.win)
        self.btn6.setText("6")
        self.btn6.setGeometry(200, 400, 100, 100)
        self.btn6.clicked.connect(affiche_bouton6)

        #bouton 7
        def affiche_bouton7():
            self.lbl.insert("7")

        self.btn7=QPushButton(self.win)
        self.btn7.setText("7")
        self.btn7.setGeometry(0,500, 100, 100)
        self.btn7.clicked.connect(affiche_bouton7)

        #bouton 8
        def affiche_bouton8():
            self.lbl.insert("8")
        self.btn8=QPushButton(self.win)
        self.btn8.setText("8")
        self.btn8.setGeometry(100, 500, 100, 100)
        self.btn8.clicked.connect(affiche_bouton8)

        #bouton 9
        def affiche_bouton9():
            self.lbl.insert("9")
        self.btn9=QPushButton(self.win)
        self.btn9.setText("9")
        self.btn9.setGeometry(200, 500, 100, 100)
        self.btn9.clicked.connect(affiche_bouton9)

        #bouton 0
        def affiche_bouton0():
            self.lbl.insert("0")

        self.btn0=QPushButton(self.win)
        self.btn0.setText("0")
        self.btn0.setGeometry(100, 600, 100, 100)
        self.btn0.clicked.connect(affiche_bouton0)
        
        #bouton +
        def affiche_boutonplus():
            self.lbl.insert("+")
        self.btnplus=QPushButton(self.win)
        self.btnplus.setText("+")
        self.btnplus.setGeometry(300, 300, 100, 100)
        self.btnplus.clicked.connect(affiche_boutonplus)

         #bouton -
        def affiche_boutonMoins():
            self.lbl.insert("-")
        self.btnMoins=QPushButton(self.win)
        self.btnMoins.setText("-")
        self.btnMoins.setGeometry(300, 400, 100, 100)
        self.btnMoins.clicked.connect(affiche_boutonMoins)

        #bouton =
        self.btnegal=QPushButton(self.win)
        self.btnegal.setText("=")
        self.btnegal.setGeometry(300, 600, 100, 100)


if __name__=='__main__':
    app=QApplication(sys.argv)
    root=QWidget()
    interface=calculatrice(root)
    interface.build("white")
    root.show()
    sys.exit(app.exec_())

    