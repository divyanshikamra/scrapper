import requests, webbrowser
from bs4 import BeautifulSoup
import numpy as np
import csv

save_link = []
user_input = input("What do you wish to search?")

google_search= requests.get("https://www.google.com/search?q="+user_input)

soup = BeautifulSoup(google_search.text, 'html.parser')

search_results = soup.select('.kCrYT a')

for link in search_results[:20]:
    actual_link= link.get('href')
    complete_link=('https://www.google.com/' + actual_link)
    save_link.append(complete_link)

# file = open('mi_web_scrap1.csv', 'a+', newline ='')
# with file:
    # write = csv.writer(file)
  #   write.writerows(save_link)

print(save_link)