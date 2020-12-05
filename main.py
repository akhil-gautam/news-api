import datetime
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.livemint.com/"
CSV_FILENAME = 'feeds.csv'

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'lxml')

data = soup.findAll('h2', attrs={'class': 'headline'})

with open(CSV_FILENAME, 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for feed in data:
        csvwriter.writerow([feed.text])
