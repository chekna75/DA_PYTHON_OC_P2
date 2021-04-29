import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'    #crée une variable pour l'url
reponse = requests.get(url)

if reponse.ok:
    soup = BeautifulSoup(reponse.text, 'html')
    title = soup.find('title')

print (title)