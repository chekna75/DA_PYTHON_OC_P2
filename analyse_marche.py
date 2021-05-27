from scrap_book import scrap_book
from scrap_category import scrap_category
from scrap_list_category import scrap_list_category

scrapping = {}
nb = 0
for book_url in scrap_category():
    book = scrap_book(book_url)
    if not book['category'] in scrapping:
        scrapping[book['category']] = []
    scrapping[book['category']].append(book)



    
