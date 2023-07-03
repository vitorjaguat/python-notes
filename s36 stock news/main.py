import requests
import os
import datetime as dt

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCKS_APIKEY = os.environ.get('ALPHAVANTAGE_STOCKS_APIKEY')
NEWS_APIKEY = os.environ.get('NEWS_APIKEY')







    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()] OK
response = requests.get(STOCK_ENDPOINT, {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCKS_APIKEY
})
data = response.json()['Time Series (Daily)']
yesterday_data = next(iter(data.values()))
yesterday_closing = float(yesterday_data['4. close'])
print(yesterday_closing)

#TODO 2. - Get the day before yesterday's closing stock price OK
data_bef_yesterday = list(data.values())[1]
bef_yesterday_closing = float(data_bef_yesterday['4. close'])
print(bef_yesterday_closing)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(yesterday_closing - bef_yesterday_closing)
print(positive_difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = positive_difference / bef_yesterday_closing * 100
print(percentage_difference)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_difference > 5:
    print('Get news.')

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if percentage_difference > 1:
    yesterday_date = dt.date.today() - dt.timedelta(days=1)
    response_news = requests.get(NEWS_ENDPOINT, {
        "qInTitle": 'deer',
        "from": yesterday_date,
        "apiKey": NEWS_APIKEY
    })
    articles = response_news.json()['articles']
    articles_first3 = articles[:3]
    

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation OK


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
articles_titles = [article['title'] for article in articles_first3]
articles_descriptions = [article['description'] for article in articles_first3]
articles_urls = [article['url'] for article in articles_first3]
#TODO 9. - Send each article as a separate message via Twilio. 
#https://stackoverflow.com/questions/29003305/sending-telegram-message-from-python
# telegram jaguat_weather_bot api:
telegram_token = os.environ.get("JAGUAT_TESTBOT_TOKEN")
chat_id = os.environ.get("JAGUAT_TESTBOT_CHATID")

def telegram_bot_sendtext(bot_message):
    global telegram_token, chat_id
    send_text = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

telegram_bot_sendtext(f' __{articles_titles[0]}__ \n{articles_descriptions[0]}\n{articles_urls[0]}')
telegram_bot_sendtext(f' __{articles_titles[1]}__ \n{articles_descriptions[1]}\n{articles_urls[1]}')
telegram_bot_sendtext(f' __{articles_titles[2]}__ \n{articles_descriptions[2]}\n{articles_urls[2]}')


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

