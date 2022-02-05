from PyQt5 import QtCore, QtGui, QtWidgets
import mainFrame
import sys
from login import *
import dbms

counter = 1

class Ui_Register(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 844)
        Dialog.setStyleSheet("background-color: rgb(85, 85, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 270, 251, 251))
        self.label.setStyleSheet("background-image: url(:/newPrefix/User.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(140, 40, 611, 751))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);font-size:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.accountheading = QtWidgets.QLabel(self.frame)
        self.accountheading.setGeometry(QtCore.QRect(160, 60, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.accountheading.setFont(font)
        self.accountheading.setStyleSheet("color: rgb(0, 85, 255);font-size:38px;")
        self.accountheading.setObjectName("label_2")
        self.Name = QtWidgets.QLineEdit(self.frame)
        self.Name.setGeometry(QtCore.QRect(90, 140, 421, 51))
        self.Name.setStyleSheet("background-color: rgb(213, 213, 213);font-size:20px;")
        self.Name.setInputMask("")
        self.Name.setText("")
        self.Name.setReadOnly(False)
        self.Name.setObjectName("lineEdit")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(90, 230, 421, 51))
        self.username.setStyleSheet("background-color: rgb(213, 213, 213);font-size:20px;")
        # self.username.setEchoMode(QtWidgets.QLineEdit.)
        self.username.setObjectName("lineEdit_2")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(90, 320, 421, 51))
        self.password.setStyleSheet("background-color: rgb(213, 213, 213);font-size:20px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("lineEdit_3")
        self.gender = QtWidgets.QLineEdit(self.frame)
        self.gender.setGeometry(QtCore.QRect(90, 410, 421, 51))
        self.gender.setStyleSheet("background-color: rgb(213, 213, 213);font-size:20px;")
        self.gender.setObjectName("lineEdit_4")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(100, 480, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")

        self.registerBtn = QtWidgets.QPushButton(self.frame)
        self.registerBtn.setGeometry(QtCore.QRect(90, 540, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.registerBtn.setFont(font)
        self.registerBtn.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                       "color: rgb(255, 255, 255);")
        self.registerBtn.setObjectName("registerBtn")
        self.registerBtn.clicked.connect(self.regIn)

        self.alreadysigned = QtWidgets.QPushButton(self.frame)
        self.alreadysigned.setGeometry(QtCore.QRect(90, 610, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.alreadysigned.setFont(font)
        self.alreadysigned.setStyleSheet("background-color: rgb(244, 35, 20);\n"
                                         "color: rgb(255, 255, 255);")
        self.alreadysigned.setObjectName("pushButton")
        self.alreadysigned.clicked.connect(self.openWindow)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Registration"))
        self.accountheading.setText(_translate("Dialog", "Create an account"))
        self.Name.setPlaceholderText(_translate("Dialog", "Name"))
        self.username.setPlaceholderText(_translate("Dialog", "User Name"))
        self.password.setPlaceholderText(_translate("Dialog", "Password"))
        self.gender.setPlaceholderText(_translate("Dialog", "Gender"))
        self.radioButton.setText(_translate("Dialog", "I Agree with Terms and Conditions"))
        self.alreadysigned.setText(_translate("Dialog", "Already Signed In"))
        self.registerBtn.setText(_translate("Dialog", "Sign Up"))

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window)
        self.window.show()
        Registeration.hide()

    def regIn(self):
        global counter  # counter for the reg_id  <<<<<<<<LOOK AT THIS >>>>>>>>>>>>>>>>>>
        radioFlag = 0
        uniqueUsrnameFlag = 0
        name = self.Name.text()
        userName = self.username.text()
        passwd = self.password.text()
        gender = self.gender.text()

        # check the radio button status
        if not self.radioButton.isChecked():
            self.msgBox("Please agree to our terms and condition", "Error!")
        else:
            radioFlag = 1

        # checking uniqueness of the username here
        db = dbms.DataBase()
        checkUnique = db.regUsernameCheck(userName)

        if checkUnique == "unique":
            # indication to the uniqueness
            uniqueUsrnameFlag = 1
        else:
            print("Registration failed, please enter unique username")
            self.msgBox("Please enter unique username", "Error!")

        # open new main Frame if both condition meets
        if radioFlag == 1 and uniqueUsrnameFlag == 1:
            db.insertToReg(counter, name, userName, passwd, gender)
            counter += 1
            # to clear the boxes
            self.clearRegBox()
            self.successMsgBox("Registered successfully!", "Success")
            # to open the login
            self.openWindow()

    def clearRegBox(self):
        self.Name.clear()
        self.username.clear()
        self.password.clear()
        self.gender.clear()

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Registeration = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupUi(Registeration)
    Registeration.show()
    sys.exit(app.exec_())
