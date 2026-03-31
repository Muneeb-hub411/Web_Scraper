import requests
from fake_useragent import UserAgent
import time

url="https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=e00600e7-ac13-402c-bd72-1ea1a2d6a806"

session=requests.Session()
headers={
    'User-Agent': UserAgent().random,
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://www.google.com/',
        
    
}

time.sleep(2)
response=session.get(url)
with open("mobiles.html", "w", encoding="utf-8") as file:
    file.write(response.text)