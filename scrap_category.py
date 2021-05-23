import requests

from bs4 import BeautifulSoup

def scrap_category(url):
    books_urls = [] #Création d'un dictionnaire
    for u in generate_category_url(url): # Boucle qui recupère l'url et génère les url
        reponse = requests.get(u) 
        if reponse.ok:
            soup = BeautifulSoup(reponse.content, "html.parser")
            books_urls += [item.get('href').replace('../../..','http://books.toscrape.com/catalogue') for item in soup.select('section h3 a')] 
            #On ajouter les url a books urls
        else:
            break
    return books_urls

        
        

def generate_category_url(url):
    nb = 1
    yield url
    while True:
        nb += 1
        yield url.replace('index',f'page-{nb}')
print(scrap_category('http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'))