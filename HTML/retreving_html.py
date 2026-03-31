import requests

url="https://www.daraz.pk/mobile-cases-covers/?from=hp_categories&q=Mobile+Accessories&service=all_channel"

response=requests.get(url)

with open("response.html", "w", encoding="utf-8") as file:
    file.write(response.text)