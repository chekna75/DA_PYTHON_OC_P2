from scrap_book import scrap_book
from scrap_category import scrap_category


scrapping = {} 


for book_url in scrap_category():  # on cree la boucle pour pouvoir scrapper les livre, on va prendre un par un les url de scrap_categrory
    book = scrap_book(book_url)  # book egale le scrap d'un book
    if not book['category'] in scrapping:  # si il n'y a pas la  category du livre 
        scrapping[book['category']] = []  # scrapping prend les valeur de book category
    scrapping[book['category']].append(book)  # alors on cree la categorie du livre dans scrapping
