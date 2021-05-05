import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'    #crée une variable pour l'url
reponse = requests.get(url)

if reponse.ok:
    soup = BeautifulSoup(reponse.text, 'html')
    title = soup.find('title') #chercher le titre
    trs = soup.findAll('tr') # chercher tout les tr
    tds = soup.findAll('td')
    h1 = soup.find('h1')

print (url) # afficher l'url
print (title.text)
print (h1.text)
[print(str(tr) + '\n\n') for tr in trs] # boucle qui sert a afficher tout les tr
