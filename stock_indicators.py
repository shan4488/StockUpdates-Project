
import requests
import json
from datetime import date
from datetime import timedelta

url = "https://alpha-vantage.p.rapidapi.com/query"
company = "MSFT"
querystring = {"function":"TIME_SERIES_DAILY","symbol":company,"outputsize":"compact","datatype":"json"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "666efa009emshba1a762660894b3p19ad9cjsn95b450d38e97"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# calculate yesterday
today = date.today()
yesterday = today - timedelta(days=2) # yesterday was giving error because it is some type of datetime obj

result = json.loads(response.text)
print(response.text)
stock_symbol = result["Meta Data"]["2. Symbol"]
stock_refreshedDt = result["Meta Data"]["3. Last Refreshed"]
stk_open = result["Time Series (Daily)"][str(yesterday)]["1. open"]
stk_close = result["Time Series (Daily)"][str(yesterday)]["4. close"]
stk_low = result["Time Series (Daily)"][str(yesterday)]["3. low"]
stk_high = result["Time Series (Daily)"][str(yesterday)]["2. high"]
stk_vol = result["Time Series (Daily)"][str(yesterday)]["5. volume"]
print(stk_open)
