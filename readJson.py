##### IMPORTS #####
import requests
from datetime import datetime
import pytz


###### CONSTANTS ######
news_api = "9b34898258214cc7be306cabdfbed128"
news_keyword = "india"
country_code = "in"
telegram_group = "testananta"
telegram_api = "5230528864:AAE0oT9CEjczbzSj4MGugvmmZzKEl5mXXGQ"
request_link = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={news_api}"

#request URL
news_response = requests.get(request_link)


newsJson = news_response.json()
message = ""
# print(jsonFile)
for article in newsJson["articles"]:
    # print(article["title"])
    message += article["title"]

    message += "\n\n"

telegram_api_url = (
    f"https://api.telegram.org/bot{api}/sendMessage?chat_id=@{group}&text={message}"
)
# https://api.telegram.org/bot5230528864:AAE0oT9CEjczbzSj4MGugvmmZzKEl5mXXGQ/sendMessage?chat_id=@testananta&text=xyz
response = requests.get(telegram_api_url)

# print(response.status_code)
if response.status_code == 200:
    print("Success")
else:
    print("failed")

