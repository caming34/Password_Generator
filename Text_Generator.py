import secrets
import string
import random
import sys
from PySide6.QtWidgets import  QMainWindow , QApplication , QLabel , QWidget , QPushButton , QProgressBar , QFrame , QLineEdit
    
class Text_Generator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PASSWORD - GENERTOR')
        self.setGeometry(200,200,350,300)
        
        self.Tp1 = QLabel(self)
        self.Tp1.setText('Input Text of Random Password?')
        self.Tp1.move(10,15)

        self.Tp2 = QLabel(self)
        self.Tp2.setText('Output')
        self.Tp2.move(10,70)
    # def Genertor_Text_on(self):
    #     words = random.sample(self.widget)
    #     chars = ''.join(
    #             secrets.choice(string.ascii_letters + string.digits + string.punctuation)
    #             for i  in range(len(self.In1) // 2))
    #     password = ' '.join(words + list(chars))
    #     print(password)
    #     return password

class QMain_Text_Generator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = QLineEdit()
        self.widget.setMaxLength(10)
        self.widget.setPlaceholderText("Enter your text")
        # self.widget.setReadOnly(True)

        self.widget.returnPressed.connect(self.return_pressed)
        self.widget.selectionChanged.connect(self.selection_changed)
        self.widget.textChanged.connect(self.text_changed)
        self.widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(self.widget)


    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")


    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())


    def text_changed(self, s):
        print("Text changed...")
        print(s)


    def text_edited(self, s):
        print("Text edited...")
        print(s)


App = QApplication(sys.argv)
M =  Text_Generator()
Q = QMain_Text_Generator()
# M.Genertor_Text_on()
Q.show()
M.show()
App.exec()
