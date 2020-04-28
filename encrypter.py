import os
import sys
import subprocess
import PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QInputDialog, QFileDialog
from PyQt5.QtWidgets import QPushButton, QRadioButton, QAction, QLineEdit, QMessageBox, QLabel


class Root(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setStyleSheet("background-color: #e0e0eb;")
        self.setFixedSize(600, 400)
        self.title = "File Encrypter"
        self.top = 400
        self.left = 100
        self.width = 400
        self.height = 600
        self.InitWindow()

    def InitWindow(self):

        self.setWindowIcon(QtGui.QIcon("flamingo.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.button = QPushButton('Select File', self)
        self.button.clicked.connect(self.select_file)
        self.button.move(100, 200)
        self.button.resize(100, 40)

        self.button2 = QPushButton('Launch', self)
        self.button2.clicked.connect(lambda:self.Launch(self.radio1.isChecked()))
        self.button2.move(400, 200)
        self.button2.setEnabled(False)
        self.button2.setStyleSheet("background-color: #808080; ")
        self.button2.resize(100, 40)

        self.button3 = QPushButton('', self)
        self.button3.setIcon(QtGui.QIcon("gear.png"))
        self.button3.clicked.connect(self.Info)
        self.button3.move(550, 20)
        self.button3.resize(30, 30)

        self.radio1 = QRadioButton('Encrypt', self)
        self.radio1.move(270, 140)
        self.radio1.resize(200, 50)

        self.radio2 = QRadioButton('Decrypt', self)
        self.radio2.move(270, 190)
        self.radio2.resize(80, 40)

        self.image = QLabel(self)
        self.image.setPixmap(QtGui.QPixmap("file.png"))
        self.image.resize(150, 100)
        self.image.move(120, 100)
        self.image.show()

        self.image2 = QLabel(self)
        self.image2.setPixmap(QtGui.QPixmap("crypt.png"))
        self.image2.resize(150, 100)
        self.image2.move(420, 100)
        self.image2.show()

        self.image3 = QLabel(self)
        self.image3.setPixmap(QtGui.QPixmap("gnu.png"))
        self.image3.resize(150, 160)
        self.image3.move(280, 280)
        self.image3.show()

        self.label = QLabel(self)
        self.label.setText("Encyption with GNU Privacy Guard")
        self.label.move(330, 350)
        self.label.resize(400, 20)

        self.show()

    def select_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Select a File", "/home/", "All Files (*.*)")[0]
        if (os.path.splitext(self.file) == "gpg"):
            self.radio2.setChecked(True)
        else:
            self.radio1.setChecked(True)
        self.button.setText(os.path.basename(self.file))
        if self.button.text() == '':
            self.button.setText("Select File")
            self.button2.setEnabled(False)
            self.button2.setStyleSheet("background-color: #808080; ")
        else:
            self.button2.setStyleSheet("background-color: red; ")
            self.button2.setEnabled(True)

    def Launch(self, check):
        if check:
            subprocess.call(['bash', 'check.sh', '-c', self.file])
        else:
            subprocess.call(['bash', 'check.sh', '-d', self.file])

    def Info(self):
        self.info = QMessageBox()
        self.top2 = 400
        self.left2 = 200
        self.width2 = 400
        self.height2 = 600
        self.info.setGeometry(self.top2, self.left2, self.width2, self.height2)
        self.info.setWindowTitle("Details")
        self.info.setText("\nThis tool is a free/open-source software \
that encrypts a user's file using GNU Privacy Guard. \
\n\n Version: 1.0 \n\n License: GPL v3.0")
        self.info.show()

App = QApplication(sys.argv)
root = Root()
sys.exit(App.exec())
