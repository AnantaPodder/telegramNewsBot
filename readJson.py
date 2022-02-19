import requests
from datetime import datetime
import pytz

api = "9b34898258214cc7be306cabdfbed128"
keyword = "tesla"

IST = pytz.timezone("Asia/Kolkata")

raw_TS = datetime.now(IST)
today = raw_TS.strftime("%Y-%m-%d")
country_code = "in"

api = "5230528864:AAE0oT9CEjczbzSj4MGugvmmZzKEl5mXXGQ"
group = "testananta"


# print(today)
# print(today)
request_link = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey=9b34898258214cc7be306cabdfbed128"
# header = {"User-Agent": "Chrome/84.0.4147.105 Safari/537.36"}
# print(request_link)
# response = requests.get(request_link, headers=header)
response = requests.get(request_link)

jsonFile = response.json()
message = ""
# print(jsonFile)
for article in jsonFile["articles"]:
    # print(article["title"])
    message += article["title"]

    message += "\n\n"

telegram_api_url = (
    f"https://api.telegram.org/bot{api}/sendMessage?chat_id=@{group}&text={message}"
)
response = requests.get(telegram_api_url)

# print(response.status_code)
if response.status_code == 200:
    print("Success")
else:
    print("failed")


# for centn in jsonFile["centers"]:
#     # print(centn)
#     for sess in centn["sessions"]:
#         # print(sess)
#         # sess_date = sess["date"]
#         print(sess["date"], sess["vaccine"])
