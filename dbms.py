import sqlite3


class DataBase:

    def __init__(self):
        self.conn = sqlite3.connect("stockDatabase.db")

    def tableCreation(self):
        cur = self.conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS Stock
        (Stock_ID INTEGER,
        Stock_Name TEXT NOT NULL,
        Symbol TEXT NOT NULL,
        PRIMARY KEY(Stock_Id, Symbol))''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Stock_News
        (StockNewsId INTEGER PRIMARY KEY AUTOINCREMENT,
        Symbol TEXT,
        News TEXT,
        Pub_Date TEXT,
        FOREIGN KEY (Symbol) REFERENCES STOCK (Symbol) ON DELETE CASCADE)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Stock_Price
        (StockPriceId INTEGER PRIMARY KEY AUTOINCREMENT,
        Symbol TEXT,
        Refresh_Date TEXT,
        open INTEGER,
        close INTEGER,
        low INTEGER,
        high INTEGER,
        volume INTEGER,
        FOREIGN KEY (Symbol) REFERENCES STOCK (Symbol) ON DELETE CASCADE)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Registration
               (R_Id INTEGER,
               Name TEXT,
               User_Name TEXT NOT NULL,
               Password TEXT,
               Gender CHARACTER(1),
               PRIMARY KEY(R_Id, User_Name)
               )''')

        cur.execute('''CREATE TABLE IF NOT EXISTS Login
               (Login_Id INTEGER PRIMARY KEY AUTOINCREMENT,
               User_Name TEXT,
               Login_Date TEXT,
               Login_Time TEXT,
               FOREIGN KEY (User_Name) REFERENCES REGISTRATION (User_Name) ON DELETE SET NULL)''')

    def insertToStock(self, sid, sname, sym):
        self.conn.execute("INSERT INTO Stock (Stock_ID, Stock_Name, Symbol) VALUES (?, ?, ?)", (sid, sname, sym))
        self.conn.commit()
        self.conn.close()

    def deleteFromStock(self, sid):
        self.conn.execute("DELETE FROM Stock where Stock_ID=?", (sid,))
        self.conn.commit()
        self.conn.close()

    def updateStock(self, sid, sname, sym):
        self.conn.execute("UPDATE Stock SET Stock_Name=?, Symbol=? where Stock_Id=?",(sname, sym, sid))
        self.conn.commit()
        self.conn.close()

    def insertToStockNews(self, sym, news, pub_date):
        self.conn.execute("INSERT INTO Stock_News (Symbol, News, Pub_Date) VALUES (?,?,?)", (sym, news, pub_date))
        self.conn.commit()
        self.conn.close()

    def insertToStockPrice(self, sym, rdate, open, close, high, low, vol):
        self.conn.execute("INSERT INTO Stock_Price (Symbol, Refresh_Date, open, close, high, low, volume) VALUES (?,?,?,?,?,?,?)", (sym, rdate, open, close, high, low, vol))
        self.conn.commit()
        self.conn.close()

    def insertToReg(self, rid, rname, username, passwd, gender):
        self.conn.execute("INSERT INTO Registration (R_Id, Name, User_Name, Password, Gender) VALUES (?,?,?,?,?)",
                          (rid, rname, username, passwd, gender))
        self.conn.commit()
        self.conn.close()

    def insertToLogin(self, uname, ldate, ltime):
        self.conn.execute("INSERT INTO Login (User_Name, Login_Date, Login_Time) VALUES (?,?,?)", (uname, ldate, ltime))
        self.conn.commit()
        self.conn.close()

    def fetch_news(self, sym):
        cur = self.conn.cursor()
        cur.execute("SELECT News from Stock_News where Symbol=?",(sym,))
        rows = cur.fetchall()
        return rows

    def loginCreds(self, user_name, passwd):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT Password FROM Registration where User_Name=?", (user_name,))
            regPasswd = cur.fetchone()  # saves as a tuple like ('pass',) to retrieve use indexing

            if str(regPasswd[0]) == str(passwd):
                print("Passed the Login security")
                return "Lpass"
            else:
                print("Failed the Login security")
                return "Lfail"
        except Exception as ex:
            print("error logging db: %s" % (ex))

    def regUsernameCheck(self, user_name):
        flag = 0
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT User_Name FROM Registration")
            userNames = cur.fetchall()  # list of tuples

            for usrname in set(userNames):    # converting into set to reduce the redundancy (happy to find that)
                if str(user_name) == str(usrname[0]):
                    print("username already exists")
                    flag = 1
                    return "Notunique"
            if flag == 0:
                print("User name is unique!")
                return "unique"
        except Exception as exa:
            print("error logging db: %s" % (exa))

    def retrieveStock(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * from Stock")
        stockDetails = cur.fetchall()
        return stockDetails



db = DataBase()

# db.tableCreation()
# db.insertToStock(5, 'Coca Ltd', 'COCA')
# db.insertToStockNews('TSLA', 'News1 Hello Shan', '2022-02-28')
# db.insertToStockPrice('TSLA', 200.203, 300.389, 4000.892, 400.773, 5000.87823)
# db.insertToReg(1, 'sharan', 'shan', 'sh', 'M')
# db.insertToLogin('shan', '2024-02-02', '20:20:40')
# rows = db.fetch_news('TSLA')
# print(rows)
# db.regUsernameCheck("shanss")
# details = db.retrieveStock()
# print(details)
# for tup in details:
#     # print(str(tup)[1:-1])
#     print(str(tup[0]) + "\t\t\t" + str(tup[1]) + "\t\t\t" + str(tup[2]))

# db.deleteFromStock(5)
# db.updateStock(5, 'Coca Cola', 'COCA')