from PySide2.QtWidgets import QWidget, QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PySide2.QtGui import QIcon, QFont
from PySide2.QtCore import Qt, QEvent
from PySide2 import QtTest
import pongbot
import pong
import scoreboard
import sys


class window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.button1 = QPushButton("Play 1vBot", self)
        self.button2 = QPushButton("Play 1v1", self)
        self.button3 = QPushButton("Score", self)
        self.button4 = QPushButton("Quit", self)
        self.setWindowTitle("Pong 2D")
        self.setGeometry(700,300,280,600)
        self.setMaximumWidth(600)
        self.setMaximumHeight(600)
        self.setMinimumHeight(200)
        self.setMinimumWidth(200)
        self.set_icon()
        self.button_settings()
        self.game_label()


    def set_icon(self):
        app_ico = QIcon("Resources/Icon/icon.ico")
        self.setWindowIcon(app_ico)

    def button_settings(self):

        self.button1.setGeometry(10, 300, 200, 50)
        self.button1.clicked.connect(self.single_player_mode)
        # button1.move(10,300)
        # button1.setFixedHeight(50)
        # button1.setFixedWidth(200)

        self.button2.setGeometry(10, 360, 200, 50)
        self.button2.clicked.connect(self.multiplayer_play_mode)
        # button2.move(10,360)
        # button2.setFixedHeight(50)
        # button2.setFixedWidth(200)

        self.button3.setGeometry(10, 420, 200, 50)
        self.button3.clicked.connect(self.scoreboard)
        # button3.move(10,420)
        # button3.setFixedHeight(50)
        # button3.setFixedWidth(200)

        self.button4.setGeometry(10,480,200,50)
        self.button4.clicked.connect(self.close)
        # button4.move(10,480)
        # button4.setFixedHeight(50)
        # button4.setFixedWidth(200)

    def game_label(self):
        label = QLabel("PONG 2D", self)
        label.move(10,10)
        label.setFixedWidth(240)
        newfont = QFont("Times", 24, QFont.Bold)
        label.setFont(newfont)

    def single_player_mode(self, event):
        self.button1.setEnabled(False)
        self.button2.setEnabled(False)
        self.button3.setEnabled(False)
        try:
            pongbot.main()
        except:
            pass
        QtTest.QTest.qWaitForWindowActive(self, 5000)
        self.close()

    def multiplayer_play_mode(self):
        self.button1.setEnabled(False)
        self.button2.setEnabled(False)
        self.button3.setEnabled(False)
        try:
            sys.exit(pong.main())
        except:
            pass
        QtTest.QTest.qWaitForWindowActive(self, 5000)
        self.close()

    def scoreboard(self):
        self.button1.setEnabled(False)
        self.button2.setEnabled(False)
        self.button3.setEnabled(False)
        try:
            sys.exit(scoreboard.main())
        except:
            pass
        QtTest.QTest.qWaitForWindowActive(self, 5000)
        self.close()



myapp = QApplication([])
window = window()
window.show()
sys.exit(myapp.exec_())

