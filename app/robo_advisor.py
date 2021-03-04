import requests
import json
import csv
import os
from dotenv import load_dotenv

#formatting
def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71
 
#inputting  and validating
while True:
    ticker = input("Please input one stock or cryptocurrency symbol (between 1 and 5 non-numeric characters).")
    if len(ticker)<1 or len(ticker)>5 or ticker.isalpha() == False:
        print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
    else:
      break
        #it may also optionally prompt the user to specify additional inputs 
        #such as risk tolerance and/or other trading preferences, as desired and applicable.

#TODO "Sorry, couldn't find any trading data for that stock symbol" 

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

daily_highs = []
daily_lows = []
for day in market_days:
    daily_high = parsed_response["Time Series (Daily)"][day]["2. high"]
    daily_highs.append(float(daily_high))
    daily_low = parsed_response["Time Series (Daily)"][day]["3. low"]
    daily_lows.append(float(daily_low))
recent_high = max(daily_highs)
recent_low = min(daily_lows)


csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=["city", "name"])
    writer.writeheader() # uses fieldnames set above
    writer.writerow({"city": "New York", "name": "Yankees"})
    writer.writerow({"city": "New York", "name": "Mets"})
    writer.writerow({"city": "Boston", "name": "Red Sox"})
    writer.writerow({"city": "New Haven", "name": "Ravens"})

#output 
print("-------------------------")
print("SELECTED SYMBOL:", parsed_response["Meta Data"]["2. Symbol"].upper())
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:", now.strftime("%Y-%m-%d %H:%M %p"))
print("-------------------------")
print("LATEST DAY:", latest_day)
print("LATEST CLOSE:", to_usd(float(parsed_response["Time Series (Daily)"][latest_day]["4. close"])))
print("RECENT HIGH:",to_usd(recent_high))
print("RECENT LOW:", to_usd(recent_low))
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON:") #TODO
print("-------------------------")
print("WRITING DATA TO CSV:", csv_file_path, "...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
