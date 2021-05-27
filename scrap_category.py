import requests

from bs4 import BeautifulSoup

def scrap_category():
    for u in generate_category_url():  # Boucle qui recupère l'url et génère les url
        reponse = requests.get(u) 
        if reponse.ok:
            soup = BeautifulSoup(reponse.content, "html.parser")
            for item in soup.select('section h3 a'):
                yield 'http://books.toscrape.com/catalogue/' + item.get('href')
            # On ajouter les url a books urls
        else:
            break
def generate_category_url():
    nb = 0
    while True:
        nb += 1
        yield f'http://books.toscrape.com/catalogue/page-{nb}.html'
# print(scrap_category('http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'))