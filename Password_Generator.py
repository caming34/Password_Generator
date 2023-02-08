import secrets
import string
import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QMainWindow , QApplication , QLabel , QCheckBox ,
    QComboBox , QWidget , QPushButton , QProgressBar ,
    QFrame
    )
class Password_Generator(QWidget):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle('PASSWORD - GENERTOR')
        self.setGeometry(200,200,350,300)
        
    def Generate_password(length):
        print('\n-------------Run Code in Random PASSWORD??+/---------------\n')
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(chars) for i in range(length))
        return password


    length = int(input("Enter password length: "))
    print("Random password:", Generate_password())
    word  =  input()
M =  Password_Generator()  
App = QApplication(sys.argv)
M.show()
App.exec()