import requests
import json
import os
from dotenv import load_dotenv

#formatting
def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71


#inputting  and validating
#while True:
ticker = input("Please input input one stock or cryptocurrency symbol (between 1 and 5 non-numeric characters).")
#    if len(ticker)<1 or len(ticker)>5:
#        print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
#    if ticker == "DONE":
#        break
        #it may also optionally prompt the user to specify additional inputs 
        #such as risk tolerance and/or other trading preferences, as desired and applicable.
#    else:
#        if 1<=len(ticker)<=5:
#          selected_tickers.append(str(ticker))
#print(selected_tickers)



#information 
load_dotenv()
ALPHAVANTAGE_API_KEY= os.getenv("ALPHAVANTAGE_API_KEY")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)
parsed_response = json.loads(response.text) 

from datetime import datetime
now = datetime.now() 

market_days = list(parsed_response["Time Series (Daily)"])
latest_day = market_days[0]

#output 
print("-------------------------")
print("SELECTED SYMBOL:", parsed_response["Meta Data"]["2. Symbol"])
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:", now.strftime("%Y-%m-%d %H:%M %p"))
print("-------------------------")
print("LATEST DAY:", latest_day)
print("LATEST CLOSE:", to_usd(float(parsed_response["Time Series (Daily)"][latest_day]["4. close"])))
print("RECENT HIGH:",to_usd(float(parsed_response["Time Series (Daily)"][latest_day]["2. high"])))
print("RECENT LOW:",to_usd(float(parsed_response["Time Series (Daily)"][latest_day]["3. low"])))
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
