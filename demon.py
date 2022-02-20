##### IMPORTS #####
from hamcrest import contains
import requests
import time

###### CONSTANTS ######
telegram_group = "testananta"
telegram_api = "5230528864:AAE0oT9CEjczbzSj4MGugvmmZzKEl5mXXGQ"
message = ""
time_interval = 3
global latest_update_id
latest_update_id = 951159815

global news_heads
news_heads = ["xyz"]

global news_api
news_api = "9b34898258214cc7be306cabdfbed128"
# telegram_api_url = (
#     f"https://api.telegram.org/bot{api}/sendMessage?chat_id=@{group}&text={message}"
# )
# https://api.telegram.org/bot5230528864:AAE0oT9CEjczbzSj4MGugvmmZzKEl5mXXGQ/sendMessage?chat_id=@testananta&text=xyz

# response = requests.get(telegram_api_url)

# print(response.status_code)
# if response.status_code == 200:
#     print("Success")
# else:
#     print("failed")


# https://api.telegram.org/bot5230528864:AAE0oT9CEjczbzSj4MGugvmmZzKEl5mXXGQ/getUpdates
# telegram_update_json = requests.get(
#     "https://api.telegram.org/bot5230528864:AAE0oT9CEjczbzSj4MGugvmmZzKEl5mXXGQ/getUpdates"
# ).json()

# for updateId in telegram_update_json["result"]:

#     if updateId["update_id"] > latest_update_id:
#         latest_update_id = updateId["update_id"]


#     else:
#         continue
# if True:


def checkForNewMessage():
    global latest_update_id
    telegram_update_json = requests.get(
        "https://api.telegram.org/bot5230528864:AAE0oT9CEjczbzSj4MGugvmmZzKEl5mXXGQ/getUpdates"
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
