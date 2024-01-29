import requests
from bs4 import BeautifulSoup

resp = requests.get().text
soup = BeautifulSoup(resp,'lxml')
print(soup.prettify())