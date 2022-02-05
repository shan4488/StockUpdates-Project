import requests
import json
import pprint
import dbms

class news:
    def __init__(self):
        url = "https://yh-finance.p.rapidapi.com/news/v2/list"

        querystring = {"region":"US","snippetCount":"20","s":"MSFT"}

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
        print("__"*20)
        # for i in range(10):
        #     print(result['data']['main']['stream'][i]['content']['title'])
        #     print(result['data']['main']['stream'][i]['content']['pubDate'][:10] + "\n")
        stock_symbol = 'MSFT'

        for i in range(10):
            stock_news = result['data']['main']['stream'][i]['content']['title']
            snPub_date = result['data']['main']['stream'][i]['content']['pubDate'][:10] + "\n"
            dbObj = dbms.DataBase()
            dbObj.insertToStockNews(i+1, stock_symbol, stock_news, snPub_date)