from PyQt5 import QtCore, QtGui, QtWidgets
from databases import Ui_MainWindow2
from queries import Ui_MainWindow4
from PyQt5.QtCore import QTimer
from first import Ui_MainWindow3

class Ui_MainWindow(object):

    def opendatabase(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow2()
        self.ui.setupUi(self.window)
        self.window.show()

    def openqueries(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow4()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1231, 965)
        MainWindow.setStyleSheet(" background: linear-gradient(45deg,rgba(3, 147, 154, 0.9),rgba(57, 2, 130, 0.9));\n"
"background-size: 300% 300%;\n"
"animation: color 5s ease-in-out infinite;\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 180, 341, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(119, 0, 255);\n"
"box-shadow: 17px 17px #000000;")
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.ShowDatabase = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.opendatabase())
        self.ShowDatabase.setGeometry(QtCore.QRect(290, 310, 281, 411))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase.setFont(font)
        self.ShowDatabase.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(119, 0, 255);\n"
"border:1px solid rgb(119, 0, 255);\n"
"border-radius : 15px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(0, 1, 1, 0.5);\n"
"}")
        self.ShowDatabase.setObjectName("ShowDatabase")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 110, 1231, 711))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(360_F_130414382_O4tDxNpAVIBnCwOzI6YT3fiPSplEHbLW);")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1231, 111))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("\n"
"background: black;\n"
"color: white;\n"
"font-size: 27px;\n"
"border-bottom-color: 7px solid white;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 820, 1231, 111))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("\n"
"background: black;\n"
"color: white;\n"
"font-size: 27px;\n"
"border-bottom-color: 7px solid white;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 860, 351, 31))
        self.label_6.setStyleSheet("color :white;\n"
"font-size : 17px;\n"
"color:rgb(197, 149, 252);\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1710, 130, 91, 91))
        self.label_7.setStyleSheet("background-image:url(logo);\n"
"border-radius : 45%;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 110, 1230, 4))
        self.line.setStyleSheet("background-color : rgb(119,0,255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(580, 70, 91, 91))
        self.label_8.setStyleSheet("background-image:url(logo);\n"
"border-radius : 45%;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.ShowDatabase_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.openqueries())
        self.ShowDatabase_2.setGeometry(QtCore.QRect(580, 310, 361, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_2.setFont(font)
        self.ShowDatabase_2.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(119, 0, 255);\n"
"border:1px solid rgb(119, 0, 255);\n"
"border-radius : 15px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(0, 1, 1, 0.5);\n"
"}")
        self.ShowDatabase_2.setObjectName("ShowDatabase_2")
        self.ShowDatabase_3 = QtWidgets.QPushButton(self.centralwidget)
        self.ShowDatabase_3.setGeometry(QtCore.QRect(580, 520, 361, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_3.setFont(font)
        self.ShowDatabase_3.setStyleSheet("QPushButton{\n"
"background:rgb(119, 0, 255);\n"
"color:rgb(119, 0, 255);\n"
"border:1px solid rgb(119, 0, 255);\n"
"border-radius : 15px;\n"
"}\n"
"\n"
"")
        self.ShowDatabase_3.setText("")
        self.ShowDatabase_3.setObjectName("ShowDatabase_3")
        self.ShowDatabase_4 = QtWidgets.QPushButton(self.centralwidget)
        self.ShowDatabase_4.setGeometry(QtCore.QRect(140, 350, 141, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_4.setFont(font)
        self.ShowDatabase_4.setStyleSheet("QPushButton{\n"
"background:black;\n"
"color:rgb(119, 0, 255);\n"
"border:1px solid rgb(119, 0, 255);\n"
"border-radius : 15px;\n"
"}\n"
"\n"
"")
        self.ShowDatabase_4.setText("")
        self.ShowDatabase_4.setObjectName("ShowDatabase_4")
        self.ShowDatabase_5 = QtWidgets.QPushButton(self.centralwidget)
        self.ShowDatabase_5.setGeometry(QtCore.QRect(140, 450, 141, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_5.setFont(font)
        self.ShowDatabase_5.setStyleSheet("QPushButton{\n"
"background:black;\n"
"color:rgb(119, 0, 255);\n"
"border:1px solid rgb(119, 0, 255);\n"
"border-radius : 15px;\n"
"}\n"
"\n"
"")
        self.ShowDatabase_5.setText("")
        self.ShowDatabase_5.setObjectName("ShowDatabase_5")
        self.ShowDatabase_6 = QtWidgets.QPushButton(self.centralwidget)
        self.ShowDatabase_6.setGeometry(QtCore.QRect(950, 600, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_6.setFont(font)
        self.ShowDatabase_6.setStyleSheet("QPushButton{\n"
"background:black;\n"
"color:rgb(119, 0, 255);\n"
"border:1px solid rgb(119, 0, 255);\n"
"border-radius : 15px;\n"
"}\n"
"\n"
"")
        self.ShowDatabase_6.setText("")
        self.ShowDatabase_6.setObjectName("ShowDatabase_6")
        self.ShowDatabase_7 = QtWidgets.QPushButton(self.centralwidget)
        self.ShowDatabase_7.setGeometry(QtCore.QRect(950, 340, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_7.setFont(font)
        self.ShowDatabase_7.setStyleSheet("QPushButton{\n"
"background:black;\n"
"color:rgb(119, 0, 255);\n"
"border:1px solid rgb(119, 0, 255);\n"
"border-radius : 15px;\n"
"}\n"
"\n"
"")
        self.ShowDatabase_7.setText("")
        self.ShowDatabase_7.setObjectName("ShowDatabase_7")
        self.ShowDatabase_8 = QtWidgets.QPushButton(self.centralwidget)
        self.ShowDatabase_8.setGeometry(QtCore.QRect(950, 420, 141, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_8.setFont(font)
        self.ShowDatabase_8.setStyleSheet("QPushButton{\n"
"background:black;\n"
"color:rgb(119, 0, 255);\n"
"border:1px solid rgb(119, 0, 255);\n"
"border-radius : 15px;\n"
"}\n"
"\n"
"")
        self.ShowDatabase_8.setText("")
        self.ShowDatabase_8.setObjectName("ShowDatabase_8")
        self.label.raise_()
        self.label_2.raise_()
        self.ShowDatabase.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.line.raise_()
        self.label_8.raise_()
        self.ShowDatabase_2.raise_()
        self.ShowDatabase_3.raise_()
        self.ShowDatabase_4.raise_()
        self.ShowDatabase_5.raise_()
        self.ShowDatabase_6.raise_()
        self.ShowDatabase_7.raise_()
        self.ShowDatabase_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1231, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "R A Z O R P A Y"))
        self.ShowDatabase.setText(_translate("MainWindow", "Show DataBase"))
        self.label_6.setText(_translate("MainWindow", ""))
        self.ShowDatabase_2.setText(_translate("MainWindow", "Show Queries"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(window)
    window.show()

    QTimer.singleShot(3000, lambda: window.close())

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("RAZORPAY")
    QTimer.singleShot(3000, lambda: MainWindow.show())

    sys.exit(app.exec_())
