from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as s
from mysql.connector import Error
from tabulate import tabulate


def user_run(x):
    try:
        con2 = s.connect(host="127.0.0.1", user="root", passwd="dadoflols")
        if con2.is_connected():
            cursor2 = con2.cursor()
            cursor2.execute(x)
            con2.commit()
            rec = cursor2.fetchall()
            if str(rec)=="[]":
                rec=""
            return "SUCCESS"+"\n"+str(rec)
    except Error as e:
        return "ERROR"

def finalrun(query, head):
    try:
        con=s.connect(host="localhost",user="root",passwd="dadoflols")
        if con.is_connected():

            cursor=con.cursor()
            cursor.execute(query)

            rec=cursor.fetchall()

            final=[]
            for i in rec:
                final.append(list(i))

            print(tabulate(final,headers=head))
            return(tabulate(final,headers=head))
    except Error as e:
        return "Error"



class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1236, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1231, 877))
        self.label.setStyleSheet("border-image: url(360_F_130414382_O4tDxNpAVIBnCwOzI6YT3fiPSplEHbLW);\n"
"background-image: url(360_F_130414382_O4tDxNpAVIBnCwOzI6YT3fiPSplEHbLW);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.ShowDatabase = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.accounting_press())
        self.ShowDatabase.setGeometry(QtCore.QRect(140, 60, 301, 111))
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
        self.ShowDatabase_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.customer_press())
        self.ShowDatabase_2.setGeometry(QtCore.QRect(450, 60, 301, 111))
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
        self.ShowDatabase_3 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda:self.fruad_press())
        self.ShowDatabase_3.setGeometry(QtCore.QRect(760, 60, 301, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_3.setFont(font)
        self.ShowDatabase_3.setStyleSheet("QPushButton{\n"
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
        self.ShowDatabase_3.setObjectName("ShowDatabase_3")
        self.ShowDatabase_4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.transactions_press())
        self.ShowDatabase_4.setGeometry(QtCore.QRect(760, 190, 301, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_4.setFont(font)
        self.ShowDatabase_4.setStyleSheet("QPushButton{\n"
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
        self.ShowDatabase_4.setObjectName("ShowDatabase_4")
        self.ShowDatabase_5 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.gateway_press())
        self.ShowDatabase_5.setGeometry(QtCore.QRect(140, 190, 301, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_5.setFont(font)
        self.ShowDatabase_5.setStyleSheet("QPushButton{\n"
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
        self.ShowDatabase_5.setObjectName("ShowDatabase_5")
        self.ShowDatabase_6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.refund_press())
        self.ShowDatabase_6.setGeometry(QtCore.QRect(450, 190, 301, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_6.setFont(font)
        self.ShowDatabase_6.setStyleSheet("QPushButton{\n"
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
        self.ShowDatabase_6.setObjectName("ShowDatabase_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 320, 921, 311))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: rgba(0, 1, 1, 0.25);\n"
"color:white;\n"
"border:1px solid rgb(119, 0, 255);\n"
"font-family: 'Courier New', Courier, monospace;\n"
"border-radius : 15px;"
"padding : 47px;")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 650, 771, 131))
        self.lineEdit.setStyleSheet("background: rgba(0, 1, 1, 0.5);\n"
                                    "color:pink;\n"
                                    "border:1px solid rgb(119, 0, 255);\n"
                                    "border-radius : 15px;\n"
                                    "padding : 27px;")
        self.lineEdit.setObjectName("lineEdit")

        self.ShowDatabase_7 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.execute_press())
        self.ShowDatabase_7.setGeometry(QtCore.QRect(920, 650, 141, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_7.setFont(font)
        self.ShowDatabase_7.setStyleSheet("QPushButton{\n"
                                          "background: rgb(119, 0, 255);\n"
                                          "color:black;\n"
                                          "border:1px solid rgb(119, 0, 255);\n"
                                          "border-radius : 15px;\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "background: rgb(255, 2, 108);\n"
                                          "border:1px solid red;\n"
                                          "}")
        self.ShowDatabase_7.setObjectName("ShowDatabase_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1257, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1236, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.ShowDatabase_7.clicked.connect(self.execute_press())

    def fruad_press(self):
        q="SELECT * FROM fraud.fraud_db_new2"
        h=["Transaction ID","Customer ID","Merchant ID","Amount","Fraud Flag"]
        self.label_3.setText(finalrun(q,h))

    def customer_press(self):
        q = "SELECT * FROM customer.customer_db_new"
        h = ["ID", "Name", "Address", "Email", "Age", "Payment_Ref"]
        self.label_3.setText(finalrun(q, h))

    def gateway_press(self):
        q = "SELECT * FROM business.business_db_new"
        h = ["Merchant ID", "Business Address", "Name", "Email", "Phone"]
        self.label_3.setText(finalrun(q, h))

    def transactions_press(self):
        q = "SELECT * FROM transaction_db.transaction_db_new2"
        h = ["Transaction ID", "Customer ID", "Amount", "Date", "Time", "Merchant ID", "Payment Method"]
        self.label_3.setText(finalrun(q, h))

    def refund_press(self):
        q = "SELECT * FROM refund.refund_db_new"
        h = ["Refund ID", "Customer ID", "Merchant ID", "Amount","Reason","Date", "Status"]
        self.label_3.setText(finalrun(q, h))

    def accounting_press(self):
        q = "SELECT * FROM accounting.accounting_db_new"
        h = ["Merchant ID", "Revenue", "Expenses","Profits"]
        self.label_3.setText(finalrun(q, h))

    def execute_press(self):
        x=str(self.lineEdit.text())
        self.label_3.setText(user_run(x))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ShowDatabase.setText(_translate("MainWindow", "Accounting"))
        self.ShowDatabase_2.setText(_translate("MainWindow", "Customer"))
        self.ShowDatabase_3.setText(_translate("MainWindow", "Fraud"))
        self.ShowDatabase_4.setText(_translate("MainWindow", "Transaction_db"))
        self.ShowDatabase_5.setText(_translate("MainWindow", "Business"))
        self.ShowDatabase_6.setText(_translate("MainWindow", "Refund"))
        self.ShowDatabase_7.setText(_translate("MainWindow", "EXECUTE"))


# import back_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("DataBases")
    MainWindow.show()
    sys.exit(app.exec_())
