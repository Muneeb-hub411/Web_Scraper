import requests

url="https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=e00600e7-ac13-402c-bd72-1ea1a2d6a806"

response=requests.get(url)

with open("mobiles.html", "w", encoding="utf-8") as file:
    file.write(response.text)