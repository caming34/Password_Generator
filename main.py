import sys
from Text_Generator import Text_Generator
from Password_Generator import Password_Generator
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QMainWindow , QApplication , QLabel , QCheckBox , 
    QComboBox , QWidget , QPushButton , QProgressBar , 
    QFrame
    )

class Main(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.button_is_checked = False
        self.B2 = None
        self.B1 = None
        self.setWindowTitle('PASSWORD - GENERATOR')
        self.setGeometry(200,200,350,300)

    def co_Gul (self):
        self.B1 = QPushButton("Text - Generator" , self)
        self.B1.setCheckable(False)
        self.B1.released.connect(self.On_Click_B1)

        self.B1.move(65,135)


        self.B2 = QPushButton("Generator - Now" , self)
        self.B2.setCheckable(False)
        self.B2.released.connect(self.On_Click_B2)


        self.B2.move(185, 135)
        # self.pbr = QProgressBar(self)
        # self.pbr.setGeometry(10,10,250,20)

    def On_Click_B1(self):
        self.B1.clicked.connect(Text_Generator.Generator_Text_on)
        print('Text-Generator')

    def On_Click_B2(self):
        self.B2.clicked.connect(Password_Generator.generate_password)
        print('PassWord_Generator')

App = QApplication(sys.argv)
M = Main()
M.co_Gul()
M.show()
App.exec()
