import requests

from bs4 import BeautifulSoup
def scrap_book(url):
    reponse = requests.get(url)
    if reponse.ok:
        soup = BeautifulSoup(reponse.content, 'html.parser')
        title = soup.select_one('h1').text #selectionner le titre
        upc = soup.select_one("table tr:nth-child(1) > td").text
        prixsansTaxe = soup.select_one("table tr:nth-child(3) > td").text
        prixTaxe = soup.select_one("table tr:nth-child(4) > td").text
        number_available = int(soup.select_one("table tr:nth-child(6) > td").text.removeprefix('In stock (').removesuffix(' available)'))
        product_description = soup.select_one("article > p").text
        category = soup.select_one("#default > div > div > ul > li:nth-child(3) > a").text
        image_url = soup.select_one("#product_gallery > div > div > div > img").get('src').replace('../..','http://books.toscrape.com')
        return { #Dictionnaire ou les valeur ci dessus seront ajoute 
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
###if __name__ == '__main__' :
    #print(scrap_book('http://books.toscrape.com/catalogue/the-black-maria_991/index.html')) 