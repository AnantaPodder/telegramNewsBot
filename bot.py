###VERSION 1.0 for single user in a group everything predefined.


##### IMPORTS #####
import requests
import time
from os import environ

###### CONSTANTS ######
telegram_group = environ["telegram_group"]
telegram_api = environ["telegram_bot_api"]
message = ""
time_interval = 3
global latest_update_id
latest_update_id = 951159815

# test it again
global news_heads
news_heads = ["xyz"]  # array to avoid duplicate news


global news_api
news_api = (
    "9b34898258214cc7be306cabdfbed128"  # newsapi.org api to request for news updates.
)


def checkForNewMessage():
    global latest_update_id
    telegram_update_json = requests.get(
        f"https://api.telegram.org/bot{telegram_api}/getUpdates"
    ).json()

    for updateId in telegram_update_json["result"]:

        if updateId["update_id"] > latest_update_id:
            latest_update_id = updateId["update_id"]
            # print(updateId["message"]["text"])  #got the text of each message
            txt = updateId["message"]["text"]
            txt = txt.lower()

            if "headlines" in txt:
                return_headlines()

            elif "changeapi" in txt:
                print("Changing API")

        else:
            continue


# return headlines
def return_headlines():
    global news_api
    country_code = "in"
    request_link = (
        f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={news_api}"
    )
    news_response_json = requests.get(request_link).json()
    message = ""

    global news_heads
    for article in news_response_json["articles"]:
        # print(article["title"])
        if article["title"] not in news_heads:
            message += article["title"]
            message += "\n\n"
            news_heads.append(article["title"])
            # news_heads+=article["title"]

    telegram_api_url = f"https://api.telegram.org/bot{telegram_api}/sendMessage?chat_id=@{telegram_group}&text={message}"
    response_send_telegram = requests.get(telegram_api_url)

    if response_send_telegram.status_code == 200:
        print("Sent successfully.")
    else:
        print("Error occured.")


# def change_api():


while True:
    checkForNewMessage()
    time.sleep(time_interval)
