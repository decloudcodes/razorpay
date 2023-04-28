from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as s
from mysql.connector import Error
from tabulate import tabulate
# import pandas as pd
# from texttable import Texttable
# import subprocess
# from subprocess import call
# from prettytable import PrettyTable
# from terminaltables import AsciiTable

def run(query, head):
    try:
        con=s.connect(host="localhost",user="root",passwd="dadoflols")
        if con.is_connected():

            cursor=con.cursor()
            cursor.execute(query)

            final=[]
            rec=cursor.fetchall()
            # print(rec)
            final=[]
            for i in rec:
                final.append(list(i))
            # print(final)
            # print(final)
            print(tabulate(final,headers=head))
            return(tabulate(final,headers=head))

            # print(type(pd.DataFrame(final)))
            # return(pd.DataFrame(final))

            # t = Texttable()
            # t.add_rows(final)
            # print(t.draw())
            # return(t.draw())

            # t=PrettyTable()
            # for i in final:
            #     t.add_row(i)
            # print(t)
            # return(t)

            # table = AsciiTable(final)
            # print(table.table)
            # return(table.table)


    except Error as e:
        return "Error"




class Ui_MainWindow4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1428, 1017)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 110, 1461, 877))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("border-image: url(360_F_130414382_O4tDxNpAVIBnCwOzI6YT3fiPSplEHbLW);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.ShowDatabase = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q1())
        self.ShowDatabase.setGeometry(QtCore.QRect(140, 160, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase.setFont(font)
        self.ShowDatabase.setAutoFillBackground(False)
        self.ShowDatabase.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase.setObjectName("ShowDatabase")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, 160, 581, 671))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background: rgba(0, 1, 1, 0.25);\n"
"border:1px solid rgb(119, 0, 255);\n"
"color:white;\n"
"font-family: 'Courier New', Courier, monospace;\n"
"padding: 37px;\n"
"font-size: 17px\n"
"")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1461, 111))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("\n"
"background: black;\n"
"color: white;\n"
"font-size: 27px;\n"
"border-bottom-color: 7px solid white;")
        self.label_2.setObjectName("label_2")
        self.ShowDatabase_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q2())
        self.ShowDatabase_2.setGeometry(QtCore.QRect(140, 200, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_2.setFont(font)
        self.ShowDatabase_2.setAutoFillBackground(False)
        self.ShowDatabase_2.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_2.setObjectName("ShowDatabase_2")
        self.ShowDatabase_3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q3())
        self.ShowDatabase_3.setGeometry(QtCore.QRect(140, 240, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_3.setFont(font)
        self.ShowDatabase_3.setAutoFillBackground(False)
        self.ShowDatabase_3.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_3.setObjectName("ShowDatabase_3")
        self.ShowDatabase_4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q4())
        self.ShowDatabase_4.setGeometry(QtCore.QRect(140, 280, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_4.setFont(font)
        self.ShowDatabase_4.setAutoFillBackground(False)
        self.ShowDatabase_4.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_4.setObjectName("ShowDatabase_4")
        self.ShowDatabase_5 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q5())
        self.ShowDatabase_5.setGeometry(QtCore.QRect(140, 320, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_5.setFont(font)
        self.ShowDatabase_5.setAutoFillBackground(False)
        self.ShowDatabase_5.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_5.setObjectName("ShowDatabase_5")
        self.ShowDatabase_6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q6())
        self.ShowDatabase_6.setGeometry(QtCore.QRect(140, 400, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_6.setFont(font)
        self.ShowDatabase_6.setAutoFillBackground(False)
        self.ShowDatabase_6.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_6.setObjectName("ShowDatabase_6")
        self.ShowDatabase_8 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q8())
        self.ShowDatabase_8.setGeometry(QtCore.QRect(140, 360, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_8.setFont(font)
        self.ShowDatabase_8.setAutoFillBackground(False)
        self.ShowDatabase_8.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_8.setObjectName("ShowDatabase_8")
        self.ShowDatabase_9 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q9())
        self.ShowDatabase_9.setGeometry(QtCore.QRect(140, 440, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_9.setFont(font)
        self.ShowDatabase_9.setAutoFillBackground(False)
        self.ShowDatabase_9.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_9.setObjectName("ShowDatabase_9")
        self.ShowDatabase_10 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q10())
        self.ShowDatabase_10.setGeometry(QtCore.QRect(140, 600, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_10.setFont(font)
        self.ShowDatabase_10.setAutoFillBackground(False)
        self.ShowDatabase_10.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_10.setObjectName("ShowDatabase_10")
        self.ShowDatabase_11 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q11())
        self.ShowDatabase_11.setGeometry(QtCore.QRect(140, 720, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_11.setFont(font)
        self.ShowDatabase_11.setAutoFillBackground(False)
        self.ShowDatabase_11.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_11.setObjectName("ShowDatabase_11")
        self.ShowDatabase_12 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q12())
        self.ShowDatabase_12.setGeometry(QtCore.QRect(140, 480, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_12.setFont(font)
        self.ShowDatabase_12.setAutoFillBackground(False)
        self.ShowDatabase_12.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_12.setObjectName("ShowDatabase_12")
        self.ShowDatabase_13 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q13())
        self.ShowDatabase_13.setGeometry(QtCore.QRect(140, 680, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_13.setFont(font)
        self.ShowDatabase_13.setAutoFillBackground(False)
        self.ShowDatabase_13.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_13.setObjectName("ShowDatabase_13")
        self.ShowDatabase_14 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q14())
        self.ShowDatabase_14.setGeometry(QtCore.QRect(140, 760, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_14.setFont(font)
        self.ShowDatabase_14.setAutoFillBackground(False)
        self.ShowDatabase_14.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_14.setObjectName("ShowDatabase_14")
        self.ShowDatabase_15 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q15())
        self.ShowDatabase_15.setGeometry(QtCore.QRect(140, 560, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_15.setFont(font)
        self.ShowDatabase_15.setAutoFillBackground(False)
        self.ShowDatabase_15.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_15.setObjectName("ShowDatabase_15")
        self.ShowDatabase_16 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q16())
        self.ShowDatabase_16.setGeometry(QtCore.QRect(140, 520, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_16.setFont(font)
        self.ShowDatabase_16.setAutoFillBackground(False)
        self.ShowDatabase_16.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_16.setObjectName("ShowDatabase_16")
        self.ShowDatabase_17 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q17())
        self.ShowDatabase_17.setGeometry(QtCore.QRect(140, 640, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_17.setFont(font)
        self.ShowDatabase_17.setAutoFillBackground(False)
        self.ShowDatabase_17.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_17.setObjectName("ShowDatabase_17")
        self.ShowDatabase_18 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.q18())
        self.ShowDatabase_18.setGeometry(QtCore.QRect(140, 800, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowDatabase_18.setFont(font)
        self.ShowDatabase_18.setAutoFillBackground(False)
        self.ShowDatabase_18.setStyleSheet("QPushButton{\n"
"background: rgba(0, 1, 1, 0.25);\n"
"color:rgb(197, 149, 252);\n"
"border:1px solid rgb(119, 0, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(119, 0, 255, 0.5);\n"
"}")
        self.ShowDatabase_18.setObjectName("ShowDatabase_18")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 920, 351, 31))
        self.label_4.setStyleSheet("color :white;\n"
"font-size : 17px;\n"
"color:white;\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 880, 1451, 111))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("\n"
"background: black;\n"
"color: white;\n"
"font-size: 27px;\n"
"border-bottom-color: 7px solid white;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1250, 60, 91, 91))
        self.label_6.setStyleSheet("background-image:url(logo);\n"
"border-radius : 45%;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 110, 1461, 4))
        self.line.setStyleSheet("background-color : rgb(119,0,255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label.raise_()
        self.ShowDatabase.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.ShowDatabase_2.raise_()
        self.ShowDatabase_3.raise_()
        self.ShowDatabase_4.raise_()
        self.ShowDatabase_5.raise_()
        self.ShowDatabase_6.raise_()
        self.ShowDatabase_8.raise_()
        self.ShowDatabase_9.raise_()
        self.ShowDatabase_10.raise_()
        self.ShowDatabase_11.raise_()
        self.ShowDatabase_12.raise_()
        self.ShowDatabase_13.raise_()
        self.ShowDatabase_14.raise_()
        self.ShowDatabase_15.raise_()
        self.ShowDatabase_16.raise_()
        self.ShowDatabase_17.raise_()
        self.ShowDatabase_18.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.line.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1428, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def q1(self):
        query="select distinct address, (select count(*) from customer.customer_db_new where address=c.address and payment_ref='credit-card') as 'credit-card', (select count(*) from customer.customer_db_new where address=c.address and payment_ref='pay-pal') as 'pay-pal', (select count(*) from customer.customer_db_new where address=c.address and payment_ref='pay-tm') as 'pay-tm' from customer.customer_db_new as c;"
        head=["Address","Credit Card","PayPal","PayTM"]
        self.label_3.setText(run(query,head))

    def q2(self):
        query="select address as state, count(*) as total_customers from customer.customer_db_new c group by address order by total_customers desc;"
        head=["State","Total Customers"]
        self.label_3.setText(run(query,head))

    def q3(self):
        query="select address as state, count(*) as total_merchants from business.business_db_new b group by address order by total_merchants desc;"
        head=["State","Total Merchants"]
        self.label_3.setText(run(query,head))

    def q4(self):
        query="SELECT c.address, SUM(t.amount) AS 'Total Revenue' FROM transaction_db.transaction_db_new2 t INNER JOIN customer.customer_db_new c ON t.customer_id = c.customer_id GROUP BY c.address ORDER BY 'Total Revenue' DESC LIMIT 5;"
        head=["State","Total Revenue"]
        self.label_3.setText(run(query,head))

    def q5(self):
        query="select c.address, sum(r.amount) as 'Total Refund' from customer.customer_db_new as c inner join refund.refund_db_new as r on r.customer_id=c.customer_id group by c.address order by 'Total Refund' desc limit 5;"
        head=["State","Total Refunds"]
        self.label_3.setText(run(query,head))

    def q6(self):
        query="select customer_id, customer_name, (select count(*) from transaction_db.transaction_db_new2 t where t.customer_id=b.customer_id and year(t_date)=2023) as transactions, (select 2023) as _year_ from customer.customer_db_new b order by transactions desc;"
        head=["ID","Name","Transactions","Year"]
        self.label_3.setText(run(query,head))

    def q7(self):
        query=""
        head=[]
        self.label_3.setText(run(query,head))

    def q8(self):
        query="select merchant_id, b_name as merchant_name, (select count(*) from transaction_db.transaction_db_new2 t where t.merchant_id=b.merchant_id and year(t_date)=2023) as transactions, (select 2023) as _year_ from business.businesS_db_new b order by transactions desc;"
        head=["ID","Name","Transactions","Year"]
        self.label_3.setText(run(query,head))

    def q9(self):
        query="select merchant_id, b_name as merchant_name, (select sum(expenses) from accounting.accounting_db_new as f where f.merchant_id=b.merchant_id) as expenses from business.business_db_new as b order by expenses desc;"
        head=["ID","Name","Expenses"]
        self.label_3.setText(run(query,head))

    def q17(self):
        query="select merchant_id, b_name as merchant_name, (select count(*) from fraud.fraud_db_new2 as f where f.merchant_id=b.merchant_id and f.fraud_flag=1) as frauds from business.business_db_new as b;"
        head=["ID","Name","Frauds"]
        self.label_3.setText(run(query,head))

    def q11(self):
        query = "select merchant_id, b_name, (select count(*) from refund.refund_db_new r where r.merchant_id=b.merchant_id) as number_of_refunds from business.business_db_new b order by number_of_refunds desc;"
        head = ["ID", "Name", "Refunds"]
        self.label_3.setText(run(query, head))

    def q12(self):
        query="select merchant_id, b_name as merchant_name, (select sum(revenue) from accounting.accounting_db_new as a where a.merchant_id = b.merchant_id) as total_revenue from business.business_db_new as b order by total_revenue desc;"
        head=["ID","Name","Total Revenue"]
        self.label_3.setText(run(query,head))

    def q13(self):
        query="select (select count(*) from transaction_db.transaction_db_new2 where month(t_date)=04) as 'April', (select count(*) from transaction_db.transaction_db_new2 where month(t_date)=03) as 'March',(select count(*) from transaction_db.transaction_db_new2 where month(t_date)=02) as 'February', (select count(*) from transaction_db.transaction_db_new2 where month(t_date)=01) as 'Januaury';"
        head=["April","March","February","Januaury"]
        self.label_3.setText(run(query,head))

    def q14(self):
        query = "select customer_id, customer_name, (select count(*) from refund.refund_db_new r where c.customer_id=r.customer_id) as number_pf_refunds from customer.customer_db_new c;"
        head = ["ID","Name","Refunds"]
        self.label_3.setText(run(query, head))

    def q15(self):
        query="select merchant_id, b_name as merchant_name, (select sum(profits) from accounting.accounting_db_new a where a.merchant_id=b.merchant_id) as merchant_profit from business.business_db_new as b order by merchant_profit desc;"
        head=["ID","Name","Profit"]
        self.label_3.setText(run(query,head))

    def q16(self):
        query="select payment_ref, sum(amount) as 'Total Amount' from customer.customer_db_new c inner join transaction_db.transaction_db_new2 t on c.customer_id=t.customer_id group by payment_ref order by 'Total Amount' desc;"
        head=["Payment Reference","Amount"]
        self.label_3.setText(run(query,head))

    def q10(self):
        query="select customer_id, customer_name, (select count(*) from fraud.fraud_db_new2 as f where f.customer_id=c.customer_id and f.fraud_flag=1) as frauds from customer.customer_db_new c order by frauds desc;"
        head=["ID","Name","Frauds"]
        self.label_3.setText(run(query,head))

    def q18(self):
        query="select  distinct t_date as 'Date', (select sum(amount) from transaction_db.transaction_db_new2 as t2 where t.t_date=t2.t_date) as total_amount from transaction_db.transaction_db_new2 as t order by total_amount desc;"
        head=["Date","Total Amount"]
        self.label_3.setText(run(query,head))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ShowDatabase.setText(_translate("MainWindow", "Group number of customers with Payment Reference and State"))
        self.label_2.setText(_translate("MainWindow", "                 DATA QUERIES"))
        self.ShowDatabase_2.setText(_translate("MainWindow", "Rank states with the most customers"))
        self.ShowDatabase_3.setText(_translate("MainWindow", "Rank states with the most merchants"))
        self.ShowDatabase_4.setText(_translate("MainWindow", "States with the most Revenues"))
        self.ShowDatabase_5.setText(_translate("MainWindow", "States with the most Refunds"))
        self.ShowDatabase_6.setText(_translate("MainWindow", "Rank every customer with number of transactions in a specific year"))
        self.ShowDatabase_8.setText(_translate("MainWindow", "Rank every merchant with number of transactions in a specific year"))
        self.ShowDatabase_9.setText(_translate("MainWindow", "Rank merchants with most expenses"))
        self.ShowDatabase_10.setText(_translate("MainWindow", "Rank customers with most frauds"))
        self.ShowDatabase_11.setText(_translate("MainWindow", "Merchants with most refunds"))
        self.ShowDatabase_12.setText(_translate("MainWindow", "Rank merchants with most revenues"))
        self.ShowDatabase_13.setText(_translate("MainWindow", "Total transactions in a month"))
        self.ShowDatabase_14.setText(_translate("MainWindow", "Customers with most refunds"))
        self.ShowDatabase_15.setText(_translate("MainWindow", "Rank merchants with most profits"))
        self.ShowDatabase_16.setText(_translate("MainWindow", "Most used Payement Reference by amount"))
        self.ShowDatabase_17.setText(_translate("MainWindow", "Rank merchants with most frauds"))
        self.ShowDatabase_18.setText(_translate("MainWindow", "Rank the days with most Amount Transactions"))
        self.label_4.setText(_translate("MainWindow", ""))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Queries")
    MainWindow.show()
    sys.exit(app.exec_())
