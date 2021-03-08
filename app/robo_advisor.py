import requests
import json
import csv
import os
from dotenv import load_dotenv
from pandas import read_csv
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

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

#information 
load_dotenv()
ALPHAVANTAGE_API_KEY= os.getenv("ALPHAVANTAGE_API_KEY")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)

if "Error Message" in response.text:
    exit("Sorry, couldn't find any trading data for that stock symbol.")

parsed_response = json.loads(response.text) 

from datetime import datetime
now = datetime.now() 

market_days = list(parsed_response["Time Series (Daily)"])
latest_day = market_days[0]
latest_close = float(parsed_response["Time Series (Daily)"][latest_day]["4. close"])

daily_highs = []
daily_lows = []

for day in market_days:
    daily_high = parsed_response["Time Series (Daily)"][day]["2. high"]
    daily_highs.append(float(daily_high))
    daily_low = parsed_response["Time Series (Daily)"][day]["3. low"]
    daily_lows.append(float(daily_low))

recent_high = max(daily_highs)
recent_low = min(daily_lows)

#creating and writing data onto csv
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
with open(csv_file_path, "w") as csv_file: 
    writer = csv.DictWriter(csv_file, fieldnames=["timestamp", "open", "high", "low", "close", "volume"])
    writer.writeheader() 
    for day in market_days:
        daily_prices = parsed_response["Time Series (Daily)"][day]
        writer.writerow({
            "timestamp": day,
            "open": (daily_prices["1. open"]),
            "high": (daily_prices["2. high"]),
            "low":  (daily_prices["3. low"]),
            "close": (daily_prices["4. close"]),
            "volume": (daily_prices["5. volume"]),
        })

#recommendation 
recommendation = ""
risk_tolerance = input("Please input wether you have a low, medium, or high risk tolerance.")
low_risk = recent_high * .50
med_risk = recent_high * .70
high_risk = recent_high * .90
if risk_tolerance == "low" and latest_close >= low_risk:
  recommendation = "DON'T BUY"
elif risk_tolerance == "medium" and latest_close >= med_risk:
  recommendation = "DON'T BUY" 
elif risk_tolerance == "high" and latest_close >= high_risk:
  recommendation = "DON'T BUY"
else:
  recommendation = "BUY"

#reason
why_buy = "Condier a buy of " + ticker.upper() + " stock. After taking into consdieration the user's " + risk_tolerance + " risk tolerance, there is a lucrative difference between the stock's latest closing price and recent high." 
why_sell = "Do not buy " + ticker.upper() + " stock. After taking into consdieration the user's " + risk_tolerance + " risk tolerance, the stock's latest closing price is too high compared to its recent high."     
 
#output 
print("-------------------------")
print("SELECTED SYMBOL:", parsed_response["Meta Data"]["2. Symbol"].upper())
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:", now.strftime("%Y-%m-%d %I:%M %p"))
print("-------------------------")
print("LATEST DAY:", latest_day)
print("LATEST CLOSE:", to_usd(latest_close))
print("RECENT HIGH:",to_usd(recent_high))
print("RECENT LOW:", to_usd(recent_low))
print("-------------------------")
print("RECOMMENDATION:", recommendation)
print("RECOMMENDATION REASON:",why_buy if recommendation == "BUY" else why_sell)
print("-------------------------")
print("WRITING DATA TO CSV:", csv_file_path, "...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

#further exploration challenge: prices over time plot
prices_df = read_csv(csv_file_path)
prices_df.sort_values(by="timestamp", ascending=True, inplace=True)
line_graph = sns.lineplot(data= prices_df, x= "timestamp", y= "close")
line_graph.set(xlabel = "Date", ylabel = "Price ($)", title = ticker.upper() + " Price Over Time")
plt.xticks(rotation=90, fontsize = 5)
plt.show()
