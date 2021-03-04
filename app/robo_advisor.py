import requests
import json
import os
from dotenv import load_dotenv

#inputting  and validating
while True:
    ticker = input("Please input input one stock or cryptocurrency symbol (between 1 and 5 non-numeric characters).")
    if len(ticker)<1 or len(ticker)>5:
        print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
    if ticker == "DONE":
        break
        #it may also optionally prompt the user to specify additional inputs 
        #such as risk tolerance and/or other trading preferences, as desired and applicable.
    else:
        if 1<=len(ticker)<=5:
          selected_tickers.append(str(ticker))

print(selected_tickers)

#infromation output
load_dotenv()
ALPHAVANTAGE_API_KEY= os.getenv("ALPHAVANTAGE_API_KEY")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHAVANTAGE_API_KEY}"

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
