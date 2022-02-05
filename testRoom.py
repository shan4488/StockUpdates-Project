# regp = ('shan4488',)
# print(regp)
# regp1 = list(regp)
# print(regp1)
# print(regp[0])

# tester for the regUsernameCheck()
# print(set(userNames))
# print(userNames[0][0])


# msg = QMessageBox()
# msg.setIcon(QMessageBox.Critical)
# msg.setText("Error")
# msg.setInformativeText('More information')
# msg.setWindowTitle("Error")
# msg.exec_()


# count = 0
# rows = [('hello world,'), ('hello bold,')]
# print(str(rows[count])[1:-2])

# import dbms
# dbObj = dbms.DataBase()
# rows = dbObj.fetch_news('TSLA')
# count = 4
# for newsno in range(1):
#     print(str(rows[count])[1:-2])
#     print(str(rows[count+1])[1:-2])
#     print(str(rows[count+2])[1:-2])
#     print(str(rows[count+3])[1:-2])

    # self.newsBox2.setText(str(rows[count + 1])[1:-2])
    # self.newsBox3.setText(str(rows[count + 2])[1:-2])
    # self.newsBox4.setText(str(rows[count + 3])[1:-2])
    # count += 4


# Note: remember to
# check the global variable count - connected to the reg_id
# check the colors
# check the login hide
# add to the login database, that contents

# To be taken care of:
# check network
# check the yesterday date

# *********************************************************
import prettytable
from prettytable import PrettyTable
import dbms

db = dbms.DataBase()
details = db.retrieveStock()
myTable = PrettyTable(["Id", "StockName", "Symbol"])
for tup in details:
    myTable.add_row([str(tup[0]), str(tup[1]).ljust(30), str(tup[2])])

print(myTable)


def addToStock(self):
    addStklayout = QtWidgets.QGridLayout()
    self.sidBox = QtWidgets.QLineEdit()
    self.sidBox.setMinimumSize(60, 300)
    self.sidBox.setPlaceholderText("Enter the Stock Id")

    self.SnameBox = QtWidgets.QLineEdit()
    self.SnameBox.setMinimumSize(60, 300)
    self.SnameBox.setPlaceholderText("Enter the Stock Name")

    self.SymBox = QtWidgets.QLineEdit()
    self.SymBox.setMinimumSize(60, 300)
    self.SymBox.setPlaceholderText("Enter the Stock Symbol")

    self.addButton = QtWidgets.QPushButton()
    self.addButton.setText("Add")
    self.addButton.setStyleSheet("background:#ff32452;")
    self.addButton.setMinimumSize(60, 300)

    self.addStkBox = QtWidgets.QDialog()
    self.addStkBox.setWindowTitle("Add Stock")
    self.addStkBox.setLayout(layout)
    self.addStkBox.setMinimumSize(600, 600)
    self.addStklayout.addWidget(sidBox, 0, 0)
    self.addStklayout.addWidget(SnameBox, 1, 0)
    self.self.addStklayout.addWidget(addButton, 3, 0)
    self.addStkBox.exec_()


if lpassFlag == 1:
    self.successMsgBox("Logged In successfully!", "Success")
    self.openMainFrame()
