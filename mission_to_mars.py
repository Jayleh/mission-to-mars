# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
import re

# Mars exploration program url
url = "https://mars.nasa.gov/news/"

# Retrieve page with the requests module
response = requests.get(url)

# Create BeautifulSoup object; parse with 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Retrieve news title
results = soup.find_all("li", class_="slide")
print(results)
