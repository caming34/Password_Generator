import sys
from PySide6.QtWidgets import QWidget, QCheckBox, QHBoxLayout, QVBoxLayout, QGroupBox, QPushButton, QButtonGroup, QTextBrowser, QApplication, QLineEdit
import random
import string
import secrets

class widget_main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generate")
        self.setFixedSize(400, 200)

        box = QGroupBox("")
        self.button1 = QPushButton("TextGenerate", self)
        box_layout = QVBoxLayout()
        box_layout.addWidget(self.button1)
        box.setLayout(box_layout)

        box2 = QGroupBox("")
        self.button2 = QPushButton("PasswordGenerate", self)
        box2_layout = QVBoxLayout()
        box2_layout.addWidget(self.button2)
        box2.setLayout(box2_layout)

        h_layout = QHBoxLayout()
        h_layout.addWidget(box)
        h_layout.addWidget(box2)
        self.setLayout(h_layout)
        self.button1.clicked.connect(self.text_st)
        self.button2.clicked.connect(self.password_st)
        self.widget_text = text_main()
        self.widget_password = password_main()
        
    def text_st(self):
        if self.button1.clicked:
            self.widget_text.show()
        else:
            pass

    def password_st(self):
        if self.button2.clicked:
            self.widget_password.show()
        else:
            pass

class password_main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PassWordGenerate")

        self.box = QGroupBox("Generate Settings")
        self.check1 = QCheckBox("A-Z")
        self.check2 = QCheckBox("1-9")
        self.check3 = QCheckBox("""!@#$%^&*()_+|~-=`{}[]:";'<>?,./""")
        self.check1.setChecked(True)
        
        self.box_layout = QVBoxLayout()
        self.box_layout.addWidget(self.check1)
        self.box_layout.addWidget(self.check2)
        self.box_layout.addWidget(self.check3)
        self.box.setLayout(self.box_layout)

        self.box2 = QGroupBox("Number Settings")

        self.num1 = QCheckBox("8")
        self.num2 = QCheckBox("10")
        self.num3 = QCheckBox("14")
        self.num1.setChecked(True)

        self.exclusive_button_group = QButtonGroup(self)
        self.exclusive_button_group.addButton(self.num1)
        self.exclusive_button_group.addButton(self.num2)
        self.exclusive_button_group.addButton(self.num3)
        self.exclusive_button_group.setExclusive(True)

        self.box2_layout = QVBoxLayout()
        self.box2_layout.addWidget(self.num1)
        self.box2_layout.addWidget(self.num2)
        self.box2_layout.addWidget(self.num3)
        self.box2.setLayout(self.box2_layout)

        self.box3 = QGroupBox("")
        self.button = QPushButton("Generate")
        self.button.clicked.connect(self.button_click_toggled)
        self.output = QTextBrowser()

        self.box3_layout = QVBoxLayout()
        self.box3_layout.addWidget(self.button)
        self.box3_layout.addWidget(self.output)
        self.box3.setLayout(self.box3_layout)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.box)
        self.h_layout.addWidget(self.box2)

        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.box3)
        self.setLayout(self.v_layout)

    def button_click_toggled(self): 
        if self.check1.isChecked() == True:
            if self.num1.isChecked() == True:
                chars = string.ascii_letters 
                password = ''.join(secrets.choice(chars) for _ in range(8))
                self.output.setText(password)
            elif self.num2.isChecked() == True:
                chars = string.ascii_letters 
                password = ''.join(secrets.choice(chars) for _ in range(10))
                self.output.setText(password)
            elif self.num3.isChecked() == True:
                chars = string.ascii_letters 
                password = ''.join(secrets.choice(chars) for _ in range(14))
                self.output.setText(password)
        
        if self.check2.isChecked() == True:
            if self.num1.isChecked() == True:
                chars = string.digits
                password = ''.join(secrets.choice(chars) for _ in range(8))
                self.output.setText(password)
            elif self.num2.isChecked() == True:
                chars = string.digits
                password = ''.join(secrets.choice(chars) for _ in range(10))
                self.output.setText(password)
            elif self.num3.isChecked() == True:
                chars = string.digits 
                password = ''.join(secrets.choice(chars) for _ in range(14))
                self.output.setText(password)
            
        if self.check3.isChecked() == True:
            if self.num1.isChecked() == True:
                chars = string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(8))
                self.output.setText(password)
            elif self.num2.isChecked() == True:
                chars = string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(10))
                self.output.setText(password)
            elif self.num3.isChecked() == True:
                chars = string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(14))
                self.output.setText(password)
                
        if self.check1.isChecked() == True and self.check2.isChecked() == True:
            if self.num1.isChecked() == True:
                chars = string.ascii_letters + string.digits
                password = ''.join(secrets.choice(chars) for _ in range(8))
                self.output.setText(password)
            elif self.num2.isChecked() == True:
                chars = string.ascii_letters + string.digits
                password = ''.join(secrets.choice(chars) for _ in range(10))
                self.output.setText(password)
            elif self.num3.isChecked() == True:
                chars = string.ascii_letters + string.digits
                password = ''.join(secrets.choice(chars) for _ in range(14))
                self.output.setText(password)
        
        if self.check1.isChecked() == True and self.check3.isChecked() == True:
            if self.num1.isChecked() == True:
                chars = string.ascii_letters + string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(8))
                self.output.setText(password)
            elif self.num2.isChecked() == True:
                chars = string.ascii_letters + string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(10))
                self.output.setText(password)
            elif self.num3.isChecked() == True:
                chars = string.ascii_letters + string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(14))
                self.output.setText(password)
                
        if self.check2.isChecked() == True and self.check3.isChecked() == True:
            if self.num1.isChecked() == True:
                chars = string.digits + string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(8))
                self.output.setText(password)
            elif self.num2.isChecked() == True:
                chars = string.digits + string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(10))
                self.output.setText(password)
            elif self.num3.isChecked() == True:
                chars = string.digits + string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(14))
                self.output.setText(password)
        
        if self.check1.isChecked() == True and self.check2.isChecked() == True and self.check3.isChecked() == True:
            if self.num1.isChecked() == True:
                chars = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(8))
                self.output.setText(password)
            elif self.num2.isChecked() == True:
                chars = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(10))
                self.output.setText(password)
            elif self.num3.isChecked() == True:
                chars = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(secrets.choice(chars) for _ in range(14))
                self.output.setText(password)
        
class text_main(QWidget):
    def __init__(self):
        super().__init__()
        self.message_password = ''
        self.setWindowTitle("TextGenerate")
        self.setFixedSize(500, 300)

        self.box = QGroupBox("Input Text")
        self.text_line = QLineEdit(self)
        self.text_line.setPlaceholderText("Enter your text")
        
        self.box_layout = QVBoxLayout()
        self.box_layout.addWidget(self.text_line)
        self.box.setLayout(self.box_layout)

        self.box2 = QGroupBox("Number Settings")

        self.num1 = QCheckBox("8")
        self.num2 = QCheckBox("10")
        self.num3 = QCheckBox("14")
        self.num1.setChecked(True)

        self.exclusive_button_group = QButtonGroup(self)
        self.exclusive_button_group.addButton(self.num1)
        self.exclusive_button_group.addButton(self.num2)
        self.exclusive_button_group.addButton(self.num3)
        self.exclusive_button_group.setExclusive(True)

        self.box2_layout = QVBoxLayout()
        self.box2_layout.addWidget(self.num1)
        self.box2_layout.addWidget(self.num2)
        self.box2_layout.addWidget(self.num3)
        self.box2.setLayout(self.box2_layout)

        self.box3 = QGroupBox("")
        self.button = QPushButton("Generate", self)
        self.output = QTextBrowser()

        self.box3_layout = QVBoxLayout()
        self.box3_layout.addWidget(self.button)
        self.box3_layout.addWidget(self.output)
        self.box3.setLayout(self.box3_layout)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.box)
        self.h_layout.addWidget(self.box2)

        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.box3)

        self.setLayout(self.v_layout)
        self.text_line.textEdited.connect(self.text_changed)
        self.button.clicked.connect(self.button_click_toggled)

    def button_click_toggled(self):
            if self.num1.isChecked() == True:
                char = self.message_password
                password = ''.join(random.choice(char) for _ in range(8))
                self.output.setText(password)
            if self.num2.isChecked() == True:
                char = self.message_password
                password = ''.join(random.choice(char) for _ in range(10))
                self.output.setText(password)
            if self.num3.isChecked() == True:
                char = self.message_password
                password = ''.join(random.choice(char) for _ in range(14))
                self.output.setText(password)
            
    def text_changed(self, s):
        self.message_password = s
        if s:
            self.output.setText("Empty")
        else:
            self.output.setText("Not empty")
    
app_main = QApplication(sys.argv)
widget = widget_main()
widget.show()
sys.exit(app_main.exec())
