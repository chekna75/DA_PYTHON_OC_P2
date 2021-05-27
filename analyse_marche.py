from scrap_book import scrap_book
from scrap_category import scrap_category
import csv

scrapping = {} 


for book_url in scrap_category():  # on cree la boucle pour pouvoir scrapper les livre, on va prendre un par un les url de scrap_categrory
    books = scrap_book(book_url)  # book egale le scrap d'un book
    if not books['category'] in scrapping:
        scrapping[books['category']] = []  # scrapping prend les valeur de book category
        scrapping[books['category']].append(books)  # alors on cree la categorie du livre dans scrapping
        # print(scrapping)
    
    with open('some.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(books.items())
    with open('scraping.csv', 'a', newline='') as csvfile:
        ecrire = csv.writer(csvfile)
        for key, value in books.items():
            ecrire.writerow([str(key) + ' : ' + str(value)])