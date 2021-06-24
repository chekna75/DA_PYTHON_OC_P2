import requests
from scrap_book import scrap_book
from scrap_category import scrap_category
import csv


scrapping = {} 
for book_url in scrap_category():  # on cree la boucle pour pouvoir scrapper les livre, on va prendre un par un les url de scrap_categrory
    book = scrap_book(book_url)  # book egale le scrap d'un book
    book["image_url"]
    res = requests.get(book["image_url"])
    with open(f"csv/img/{book['upc']}.jpg", "wb") as file:
        file.write(res.content)
    if not book['category'] in scrapping:
        scrapping[book['category']] = []  # scrapping prend les valeur de book category
    scrapping[book['category']].append(book)  # alors on cree la categorie du livre dans scrapping
        # print(scrapping)
for category, books in scrapping.items():
    with open(f'csv/{category}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=[ 
            "url",
            "titre",
            "upc",
            "pt_price",
            "it_price",
            "number_available",
            "product_description",
            "category",
            "image_url",
            "chemin_url"])
        writer.writeheader()
        writer.writerows(books)