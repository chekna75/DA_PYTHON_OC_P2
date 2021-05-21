import requests

from bs4 import BeautifulSoup

def scrap_category(url):
    reponse = requests.get(url)
    if reponse.ok:
        soup = BeautifulSoup(reponse.content, "html.parser")
        return [item.get('href').replace('../../..','http://books.toscrape.com/catalogue') for item in soup.select('section h3 a')]
        #replace sert a remplacer le texte (avec le premier parametre a changer, et le 2eme parametre avec quoi on veut modiufier)
