import requests
from fake_useragent import UserAgent
from dotenv import load_dotenv
import os
import time
import random

load_dotenv()
API_KEY = os.getenv("SCRAPER_API_KEY")

url = "https://www.flipkart.com/search?q=mobiles"

payload = {
    'api_key': API_KEY,
    'url': url,
    'country_code': 'in',
    'render': 'true'
}

ua = UserAgent()
headers = {
    'User-Agent': ua.random,
}

time.sleep(random.uniform(2, 5))

response = requests.get('https://api.scraperapi.com/', params=payload, headers=headers)

print("Status Code:", response.status_code)

with open("mobiles.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Done! Check mobiles.html")