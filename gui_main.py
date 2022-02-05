
# Extra backup page for the mainFrame


import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QIcon
import sys

# API stock price
import requests
import json
from datetime import date
from datetime import timedelta

# Stock news API
import pprint

# DATABASE
import dbms


class App(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'AceTheRace'
        self.left = 10
        self.top = 10
        self.width = 1400
        self.height = 980
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # All window components comes here
        self.menu()
        self.mainWidget()
        # self.show()    # this was giving two instance while triggering from login, so commented
        # and added in login openMainFrame() function

    def menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')

        exitSubMenu = qtw.QAction(QIcon('exit24.png'), 'Exit', self)
        exitSubMenu.setShortcut('Ctrl+Q')
        exitSubMenu.setStatusTip('Exit application')
        exitSubMenu.triggered.connect(self.close)
        fileMenu.addAction(exitSubMenu)

        newFileMenu = qtw.QAction('New', self)
        newFileMenu.setShortcut('Ctrl+N')
        newFileMenu.triggered.connect(self.__init__)
        fileMenu.addAction(newFileMenu)

    def mainWidget(self):
        # All frames are here

        self.central_widget = qtw.QWidget()
        self.setCentralWidget(self.central_widget)
        gridL = qtw.QGridLayout()
        self.centralWidget().setLayout(gridL)
        self.centralWidget().setStyleSheet("background:#000678;")

        sInputFrame, sOutputFrame = qtw.QFrame(), qtw.QFrame()

        # All Widgets comes here

        # All widgets of the left top frame
        self.stockLbl = qtw.QLabel(self)
        self.stockLbl.setStyleSheet("color:#146356;font-size:24px;")
        self.stockLbl.setText("Let's Hear About Your Stocks!")
        self.stockLbl.setFixedWidth(360)
        self.stockLbl.move(160, 140)

        self.stockNameBox = qtw.QLineEdit(self)
        self.stockNameBox.setStyleSheet("background:#ffff02; padding:5px 0px 5px 20px")
        self.stockNameBox.setPlaceholderText("Enter the stock name...")
        self.stockNameBox.setFixedWidth(350)
        self.stockNameBox.setMinimumSize(350, 70)
        self.stockNameBox.move(160, 200)

        self.stockSubmitBtn = qtw.QPushButton(self)
        self.stockSubmitBtn.setStyleSheet("background:#ff3454")
        self.stockSubmitBtn.setMinimumSize(350, 60)
        self.stockSubmitBtn.setFixedWidth(350)
        self.stockSubmitBtn.setText("Submit")
        self.stockSubmitBtn.move(160, 300)
        self.stockSubmitBtn.clicked.connect(self.onSubmit)
        print("Passed")

        # All widgets of top right frame

        self.infoLbl1 = qtw.QLabel(self)
        self.infoLbl1.setText("Time Series : Info Stock")
        self.infoLbl1.setStyleSheet("font-size:24px;")
        self.infoLbl1.setFixedWidth(400)
        self.infoLbl1.move(900, 100)

        self.openLbl = qtw.QLabel(self)
        self.openLbl.setText("Open")
        self.openLbl.setStyleSheet("font-size:24px;")
        self.openLbl.setFixedWidth(200)
        self.openLbl.move(800, 160)

        self.CloseLbl = qtw.QLabel(self)
        self.CloseLbl.setText("Close")
        self.CloseLbl.setStyleSheet("font-size:24px;")
        self.CloseLbl.setFixedWidth(200)
        self.CloseLbl.move(1080, 160)

        self.lowLbl = qtw.QLabel(self)
        self.lowLbl.setText("Low")
        self.lowLbl.setStyleSheet("font-size:24px;")
        self.lowLbl.setFixedWidth(200)
        self.lowLbl.move(800, 255)

        self.highLbl = qtw.QLabel(self)
        self.highLbl.setText("High")
        self.highLbl.setStyleSheet("font-size:24px;")
        self.highLbl.setFixedWidth(200)
        self.highLbl.move(1080, 255)

        self.volLbl = qtw.QLabel(self)
        self.volLbl.setText("Volume")
        self.volLbl.setStyleSheet("font-size:24px;")
        self.volLbl.setFixedWidth(200)
        self.volLbl.move(980, 320)

        self.openBox = qtw.QLineEdit(self)
        self.openBox.setFixedWidth(150)
        self.openBox.move(800, 200)

        self.closeBox = qtw.QLineEdit(self)
        self.closeBox.setFixedWidth(150)
        self.closeBox.move(1080, 200)

        self.lowBox = qtw.QLineEdit(self)
        self.lowBox.setFixedWidth(150)
        self.lowBox.move(800, 290)

        self.highBox = qtw.QLineEdit(self)
        self.highBox.setFixedWidth(150)
        self.highBox.move(1080, 290)

        self.volBox = qtw.QLineEdit(self)
        self.volBox.setFixedWidth(150)
        self.volBox.move(950, 360)

        # All the widgets of the bottom frame comes here

        self.stockNewsLbl = qtw.QLabel(self)
        self.stockNewsLbl.setText("STOCK NEWS")
        self.stockNewsLbl.setFixedWidth(300)
        self.stockNewsLbl.setStyleSheet("padding:4px 4px; color:#146356;font-size:24px;")
        self.stockNewsLbl.move(100, 490)

        self.newsBox1 = qtw.QTextEdit(self)
        self.newsBox1.setStyleSheet("padding:5px;background:#F2FFE9;font-size:22px;")
        self.newsBox1.setFixedWidth(1200)
        self.newsBox1.setFixedHeight(70)
        self.newsBox1.move(100, 540)

        self.newsBox2 = qtw.QTextEdit(self)
        self.newsBox2.setStyleSheet("padding:5px;background:#F9C5D5;font-size:22px;")
        self.newsBox2.setFixedWidth(1200)
        self.newsBox2.setFixedHeight(70)
        self.newsBox2.move(100, 630)

        self.newsBox3 = qtw.QTextEdit(self)
        self.newsBox3.setStyleSheet("padding:5px;background:#F2FFE9;font-size:22px;")
        self.newsBox3.setFixedWidth(1200)
        self.newsBox3.setFixedHeight(70)
        self.newsBox3.move(100, 720)

        self.newsBox4 = qtw.QTextEdit(self)
        self.newsBox4.setStyleSheet("padding:5px;background:#F9C5D5;font-size:22px;")
        self.newsBox4.setFixedWidth(1200)
        self.newsBox4.setFixedHeight(70)
        self.newsBox4.move(100, 810)

        self.newsRefreshBtn = qtw.QPushButton(self)
        self.newsRefreshBtn.setText("Refresh For Some More!")
        self.newsRefreshBtn.setStyleSheet("background:#7C99AC;")
        self.newsRefreshBtn.setFixedWidth(1200)
        self.newsRefreshBtn.setFixedHeight(70)
        self.newsRefreshBtn.move(100, 900)
        self.newsRefreshBtn.clicked.connect(self.onRefresh)

        # The input section frame comes here ***************************
        sInputLayout = qtw.QGridLayout()
        sInputFrame.setLayout(sInputLayout)
        sInputFrame.setStyleSheet("background:#124566;text-align:center;")
        sInputFrame.setFixedHeight(400)

        # Inner Frames are here
        sInputLeftFrame, sInputRightFrame = qtw.QFrame(), qtw.QFrame()
        sInputInnerLayout_L = qtw.QGridLayout()
        sInputInnerLayout_R = qtw.QGridLayout()

        sInputLeftFrame.setLayout(sInputInnerLayout_L)
        sInputLeftFrame.setGeometry(0, 0, 400, 380)
        sInputLeftFrame.setStyleSheet("background:#63d8d6")

        sInputRightFrame.setLayout(sInputInnerLayout_R)
        sInputRightFrame.setGeometry(0, 0, 400, 380)
        sInputRightFrame.setStyleSheet("background:#43d875")
        # Add to InputLayout
        sInputLayout.addWidget(sInputLeftFrame, 1, 1)
        sInputLayout.addWidget(sInputRightFrame, 1, 2)

        # output frame comes here **********************************
        sOutputLayout = qtw.QGridLayout()
        sOutputFrame.setLayout(sOutputLayout)
        sOutputFrame.setStyleSheet("background:#ff0345")
        sOutputFrame.setFixedHeight(560)

        # Add everything to the InputLeftFrame

        # Add everything to the InputrRightFrame

        # Add everything to the main InputFrame

        # Add everything to the OutputFrame

        # Add everything to the central widget **********************

        gridL.addWidget(sInputFrame, 1, 1)
        gridL.addWidget(sOutputFrame, 2, 1)

    def onSubmit(self):
        print("Inside fun")
        company = self.stockNameBox.text()
        url = "https://alpha-vantage.p.rapidapi.com/query"

        querystring = {"function": "TIME_SERIES_DAILY", "symbol": company, "outputsize": "compact", "datatype": "json"}

        headers = {
            'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
            'x-rapidapi-key': "666efa009emshba1a762660894b3p19ad9cjsn95b450d38e97"
        }
        print("after price api1")

        response = requests.request("GET", url, headers=headers, params=querystring)
        # calculate yesterday
        today = date.today()  # NOTE TO CHANGE days=1 JUST CHANGED BECAUSE OF NIGHT WORKS
        yesterday = today - timedelta(days=4)  # yesterday was giving error because it is some type of datetime obj

        result = json.loads(response.text)
        self.stock_symbol = result["Meta Data"]["2. Symbol"]
        stock_refreshedDt = result["Meta Data"]["3. Last Refreshed"]

        stk_open = result["Time Series (Daily)"][str(yesterday)]["1. open"]
        stk_close = result["Time Series (Daily)"][str(yesterday)]["4. close"]
        stk_low = result["Time Series (Daily)"][str(yesterday)]["3. low"]
        stk_high = result["Time Series (Daily)"][str(yesterday)]["2. high"]
        stk_vol = result["Time Series (Daily)"][str(yesterday)]["5. volume"]
        print("price_api2")

        self.openBox.setText(str(stk_open))
        self.closeBox.setText(str(stk_close))
        self.lowBox.setText(str(stk_low))
        self.highBox.setText(str(stk_high))
        self.volBox.setText(str(stk_vol))
        print("price_api3")

        # adding to database: prices

        db = dbms.DataBase()
        db.insertToStockPrice(self.stock_symbol, stock_refreshedDt, stk_open, stk_close, stk_high, stk_low, stk_vol)

        print("Success Submit function")

        # ________________The News Code___________________________
        # The api for the news data collection

        url = "https://yh-finance.p.rapidapi.com/news/v2/list"

        querystring = {"region": "US", "snippetCount": "20", "s": "MSFT"}

        payload = "\"Pass in the value of uuids field returned right in this endpoint to load the next page, or leave empty to load first page\""
        headers = {
            'content-type': "text/plain",
            'x-rapidapi-host': "yh-finance.p.rapidapi.com",
            'x-rapidapi-key': "666efa009emshba1a762660894b3p19ad9cjsn95b450d38e97"
        }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        # print(response.text)
        result = json.loads(response.text)
        pprint.pprint(result)
        print("__" * 20)

        for i in range(10):
            stock_news = result['data']['main']['stream'][i]['content']['title']
            snPub_date = result['data']['main']['stream'][i]['content']['pubDate'][:10] + "\n"
            dbObj = dbms.DataBase()
            dbObj.insertToStockNews(self.stock_symbol, stock_news, snPub_date)

        # fetching four values to the news section
        print("Till here 1")
        dbObj = dbms.DataBase()
        rows = dbObj.fetch_news(self.stock_symbol)
        print("Till here 2")

        print(rows[0])
        self.newsBox1.setText(str(rows[0]))
        self.newsBox2.setText(str(rows[1]))
        self.newsBox3.setText(str(rows[2]))
        self.newsBox4.setText(str(rows[3]))
        print("Till here 3")

    def onRefresh(self):
        dbObj = dbms.DataBase()
        rows = dbObj.fetch_news(self.stock_symbol)
        count = 4
        for newsno in range(1):
            self.newsBox1.setText(str(rows[count]))
            self.newsBox2.setText(str(rows[count + 1]))
            self.newsBox3.setText(str(rows[count + 2]))
            self.newsBox4.setText(str(rows[count + 3]))
            count += 4

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
