from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import registration
from registration import *
from mainFrame import *
from prettytable import PrettyTable
import dbms


class Ui_Login(object):
    def setupUi(self, Dialog):  # setting up ui for login
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 844)
        Dialog.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 270, 251, 251))
        self.label.setStyleSheet("background-image: url(:/newPrefix/User.png);")
        # self.label.setStyleSheet("background-image: url(D:/152pypro/loginbg.jfif);")

        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(100, 100, 600, 600))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.loginsymbol = QtWidgets.QLabel(self.frame)  # setup of login symbol
        self.loginsymbol.setGeometry(QtCore.QRect(200, 100, 331, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.loginsymbol.setFont(font)
        self.loginsymbol.setStyleSheet("color: rgb(0, 215, 155);")
        self.loginsymbol.setObjectName("label_2")
        # setup of  username
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(90, 210, 421, 51))
        self.username.setStyleSheet("background-color: rgb(213, 213, 213);font-size:24px;")
        # self.username.setEchoMode(QtWidgets.QLineEdit.Password)
        self.username.setObjectName("lineEdit_2")

        # setup user credentials requirements
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(90, 300, 421, 51))
        self.password.setStyleSheet("background-color: rgb(213, 213, 213);font-size:24px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("lineEdit_3")

        self.submitpushButton = QtWidgets.QPushButton(self.frame)
        self.submitpushButton.setGeometry(QtCore.QRect(90, 400, 421, 51))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.submitpushButton.setFont(font)
        self.submitpushButton.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                            "color: rgb(255, 255, 255);font-size:22px;")
        self.submitpushButton.setObjectName("pushButton")
        # self.submitpushButton.clicked.connect(self.openMainFrame)
        self.submitpushButton.clicked.connect(self.signInUser)

        self.adminpushButton = QtWidgets.QPushButton(self.frame)
        self.adminpushButton.setGeometry(QtCore.QRect(90, 480, 421, 51))
        self.adminpushButton.setStyleSheet("background:#b23434;color:#ffffff;font-size:20px;")
        self.adminpushButton.setText("Login As Admin")
        self.adminpushButton.clicked.connect(self.signInAdmin)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.loginsymbol.setText(_translate("Dialog", "LOGIN"))

        self.username.setPlaceholderText(_translate("Dialog", "User Name"))
        self.password.setPlaceholderText(_translate("Dialog", "Password"))
        self.submitpushButton.setText(_translate("Dialog", "Submit"))

    def openMainFrame(self):
        # self.window = QtWidgets.QMainWindow()
        self.ui = App()
        self.ui.__init__()
        self.ui.show()  # See mainFrame show() method comment
        # self.ui.mainWidget()
        # self.window.show()
        # Login.hide()

    def signInSec(self):
        lpassFlag = 0
        userName = self.username.text()
        passwd = self.password.text()

        db = dbms.DataBase()
        loginReturn = db.loginCreds(userName, passwd)

        if loginReturn == "Lpass":
            lpassFlag = 1
        else:
            print("Login Failed!")
            self.msgBox("Enter the correct password", "Error!")
        return lpassFlag

    def signInUser(self):
        lpassFlag = self.signInSec()
        if lpassFlag == 1:
            self.successMsgBox("Logged In successfully!", "Success")
            self.openMainFrame()

    def signInAdmin(self):
        lpassFlag = self.signInSec()
        if lpassFlag == 1 and self.username.text() == 'admin':
            self.successMsgBox("Welcome Admin!", "Success")
            self.adminPanel()
        else:
            self.msgBox("You are not an Admin!", "Error")


    def msgBox(self, text, title):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()

    def successMsgBox(self, text, title):
        msg = QtWidgets.QMessageBox()
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()

    def adminPanel(self):
        db = dbms.DataBase()

        layout = QtWidgets.QGridLayout()
        self.stkDisplay = QtWidgets.QTextEdit()
        self.stkDisplay.setStyleSheet("background:#000000;color:#ffffff;font-size:30px;padding:10px 10px 10px 140px")
        self.stkDisplay.setPlaceholderText("We are concerned about Security... So limited access is provided in in this GUI")
        self.stkDisplay.setMinimumSize(250,100)

        self.displayStkBtn = QtWidgets.QPushButton()
        self.displayStkBtn.setText("Display the Stocks")
        self.displayStkBtn.setStyleSheet("background:#543532;color:#ffffff;")
        self.displayStkBtn.setMinimumSize(250, 60)
        self.displayStkBtn.clicked.connect(self.stockTable)

        self.addStkBtn = QtWidgets.QPushButton()
        self.addStkBtn.setText("Add To Stock")
        self.addStkBtn.setStyleSheet("background:#543532;color:#ffffff;")
        self.addStkBtn.setMinimumSize(250, 60)
        self.addStkBtn.clicked.connect(self.addToStock)

        self.deleteStkBtn = QtWidgets.QPushButton()
        self.deleteStkBtn.setText(" Delete from Stock")
        self.deleteStkBtn.setStyleSheet("background:#543532;color:#ffffff;")
        self.deleteStkBtn.setMinimumSize(250, 60)
        self.deleteStkBtn.clicked.connect(self.dltFromStock)

        self.updateStkBtn = QtWidgets.QPushButton()
        self.updateStkBtn.setText("Update the Stock")
        self.updateStkBtn.setStyleSheet("background:#543532;color:#ffffff;")
        self.updateStkBtn.setMinimumSize(250, 60)
        self.updateStkBtn.clicked.connect(self.updateStock)


        self.adminBox = QtWidgets.QDialog()
        self.adminBox.setWindowTitle("Admin Panel")
        self.adminBox.setLayout(layout)
        self.adminBox.setMinimumSize(800, 900)
        layout.addWidget(self.stkDisplay, 0, 0)
        layout.addWidget(self.displayStkBtn, 1, 0)
        layout.addWidget(self.addStkBtn, 2, 0)
        layout.addWidget(self.deleteStkBtn, 3, 0)
        layout.addWidget(self.updateStkBtn, 4, 0)
        self.adminBox.exec_()

    def stockTable(self):
        db = dbms.DataBase()
        details = db.retrieveStock()
        myTable = PrettyTable(["Id", "StockName", "Symbol"])
        for tup in details:
            myTable.add_row([str(tup[0]), str(tup[1]).ljust(20), str(tup[2]).ljust(
                10)])  # added ljust to fix the table presentation but doesnt seems to work
        self.stkDisplay.setText(str(myTable))

    def addToStock(self):
        db = dbms.DataBase()

        self.addStklayout = QtWidgets.QGridLayout()
        self.sidBox = QtWidgets.QLineEdit()
        self.sidBox.setMinimumSize(200, 60)
        self.sidBox.setPlaceholderText("Enter the Stock Id")

        self.SnameBox = QtWidgets.QLineEdit()
        self.SnameBox.setMinimumSize(200, 60)
        self.SnameBox.setPlaceholderText("Enter the Stock Name")

        self.SymBox = QtWidgets.QLineEdit()
        self.SymBox.setMinimumSize(200, 60)
        self.SymBox.setPlaceholderText("Enter the Stock Symbol")

        self.addButton = QtWidgets.QPushButton()
        self.addButton.setText("Add")
        self.addButton.setStyleSheet("background:#567432;")
        self.addButton.setMinimumSize(200, 60)
        self.addButton.clicked.connect(self.add)

        self.addStkBox = QtWidgets.QDialog()
        self.addStkBox.setWindowTitle("Add Stock")
        self.addStkBox.setLayout(self.addStklayout)
        self.addStkBox.setMinimumSize(600, 300)
        self.addStklayout.addWidget(self.sidBox, 0, 0)
        self.addStklayout.addWidget(self.SnameBox, 1, 0)
        self.addStklayout.addWidget(self.SymBox, 2, 0)
        self.addStklayout.addWidget(self.addButton, 3, 0)
        self.addStkBox.exec_()

    def dltFromStock(self):
        self.dltStklayout = QtWidgets.QGridLayout()
        self.sidBox = QtWidgets.QLineEdit()
        self.sidBox.setMinimumSize(200, 60)
        self.sidBox.setPlaceholderText("Enter the Stock Id")

        self.dltButton = QtWidgets.QPushButton()
        self.dltButton.setText("Delete")
        self.dltButton.setStyleSheet("background:#567432;")
        self.dltButton.setMinimumSize(200, 60)
        self.dltButton.clicked.connect(self.delete)

        self.dltStkBox = QtWidgets.QDialog()
        self.dltStkBox.setWindowTitle("Delete Stock")
        self.dltStkBox.setLayout(self.dltStklayout)
        self.dltStkBox.setMinimumSize(600, 250)
        self.dltStklayout.addWidget(self.sidBox, 0, 0)
        self.dltStklayout.addWidget(self.dltButton, 1, 0)
        self.dltStkBox.exec_()

    def updateStock(self):
        db = dbms.DataBase()
        self.udtStklayout = QtWidgets.QGridLayout()
        self.sidBox = QtWidgets.QLineEdit()
        self.sidBox.setMinimumSize(200, 60)
        self.sidBox.setPlaceholderText("Enter the Stock Id (You can't update this!)")

        self.SnameBox = QtWidgets.QLineEdit()
        self.SnameBox.setMinimumSize(200, 60)
        self.SnameBox.setPlaceholderText("Enter the Stock Name")

        self.SymBox = QtWidgets.QLineEdit()
        self.SymBox.setMinimumSize(200, 60)
        self.SymBox.setPlaceholderText("Enter the Stock Symbol")

        self.udtButton = QtWidgets.QPushButton()
        self.udtButton.setText("Update")
        self.udtButton.setStyleSheet("background:#567432;")
        self.udtButton.setMinimumSize(200, 60)
        self.udtButton.clicked.connect(self.update)

        self.udtStkBox = QtWidgets.QDialog()
        self.udtStkBox.setWindowTitle("Update Stock")
        self.udtStkBox.setLayout(self.udtStklayout)
        self.udtStkBox.setMinimumSize(600, 300)
        self.udtStklayout.addWidget(self.sidBox, 0, 0)
        self.udtStklayout.addWidget(self.SnameBox, 1, 0)
        self.udtStklayout.addWidget(self.SymBox, 2, 0)
        self.udtStklayout.addWidget(self.udtButton, 3, 0)
        self.udtStkBox.exec_()

    def add(self):    # part of addToStock() method
        db = dbms.DataBase()
        sid = self.sidBox.text()
        sname = self.SnameBox.text()
        sym = self.SymBox.text()
        db.insertToStock(sid, sname, sym)  # added to database
        self.successMsgBox("Added to database", "Success")

    def delete(self):           # part of dltFromStock() method
        db = dbms.DataBase()
        sid = self.sidBox.text()
        db.deleteFromStock(sid)  # delete from the stock
        self.successMsgBox("Deleted from database", "Success")

    def update(self):          #  # part of UpdateStock() method
        db = dbms.DataBase()
        sid = self.sidBox.text()
        sname = self.SnameBox.text()
        sym = self.SymBox.text()
        db.updateStock(sid, sname, sym)
        self.successMsgBox("Updated to database", "Success")


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     Login = QtWidgets.QDialog()
#     ui = Ui_Login()
#     ui.setupUi(Login)
#     Login.show()
#     sys.exit(app.exec_())
