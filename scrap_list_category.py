import requests

from bs4 import BeautifulSoup

def scrap_list_category(url):
    reponse = requests.get(url)
    if reponse.ok:
        soup = BeautifulSoup(reponse.content, "html.parser")
        ins = 'http://books.toscrape.com/'
        return [ins + item.get('href') for item in soup.select('div.side_categories > ul > li > ul > li > a')]
        #replace sert a remplacer le texte (avec le premier parametre a changer, et le 2eme parametre avec quoi on veut modiufier)
if __name__ == '__main__' :
    print(scrap_list_category('http://books.toscrape.com/')) 
    #default > div > div > div > aside > div.side_categories > ul > li > ul > li:nth-child(1) > a