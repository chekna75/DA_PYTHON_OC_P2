import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'    #crée une variable pour l'url
reponse = requests.get(url)

if reponse.ok:
    #tbody > tr:nth-child(1) > td
    soup = BeautifulSoup(reponse.text, 'html')
    title = soup.select_one('h1').text #chercher le titre
    upc = soup.select_one("table tr:nth-child(1) > td").text
    prixsansTaxe = soup.select_one("table tr:nth-child(3) > td").text
    prixTaxe = soup.select_one("table tr:nth-child(4) > td").text
    number_available = soup.select_one("table tr:nth-child(6) > td").text
    product_description = soup.select_one("article > p").text
    category = soup.select_one("#default > div > div > ul > li:nth-child(3) > a").text
    image_url = soup.select_one("#product_gallery > div > div > div > img")
    trs = soup.findAll('tr') # chercher tout les tr
    tds = soup.findAll('td')
    h1 = soup.find('h1')
resultat = {
    "url" : url,
    "titre" : title,
    "upc" : upc,
    "prixSansTaxe" : prixsansTaxe,
    "prixTaxe" : prixTaxe,
    "number_available" : number_available,
    "product_description" : product_description,
    "category" : category,
    "image_url" : image_url,
}
print (resultat)

#dict() pour renvoyer les valeurs
