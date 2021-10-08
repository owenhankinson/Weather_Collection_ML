from datetime import datetime, timedelta
from threading import Timer
import csv
from bs4 import BeautifulSoup
import requests


def collect_data():
    soup = BeautifulSoup(requests.get("https://weather.com/weather/tenday/l/7feaa8056643b17d7ecede79fa19896cd5c9c9a52d4d881782b9bc88610a7fac").content, features="html.parser")

    temps = []
    for i in range(1, 11):
        sect = soup.find("div",attrs={"id": f"titleIndex{i}"}).findAll("span", {"data-testid": "TemperatureValue"})
        for tag in sect:
            temps.append(tag.text.strip())

    with open('weather.csv', 'a+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(temps)

collect_data()