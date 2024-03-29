import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()
api_key = os.getenv('api_key')
news_api_key = os.getenv("news_api_key")
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key
}

news_parameters = {
    "qinTitle": COMPANY_NAME,
    "from": "2022-07-10",
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": news_api_key
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

difference_closing_price = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference_closing_price > 0:
    up_down = "💹"
else:
    up_down = "📉"



percentage = (difference_closing_price/float(yesterday_closing_price)) * 100
print(percentage)

if abs(percentage) > .5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()['articles']
    articles = news_data[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down} {percentage}% \nHeadline: {article['title']}, \nBrief: {article['description']}" for article in articles]
    print(formatted_articles)

    client = Client(account_sid, auth_token)
    for msg in formatted_articles:
        message = client.messages.create(
            body=msg,
            from_='+15086918567',
            to='+233543677965'
        )

#TODO 9. - Send each article as a separate message via Twilio.



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

