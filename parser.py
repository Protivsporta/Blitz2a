import requests
from bs4 import BeautifulSoup

url = 'http://readrate.com/rus/ratings/top100'
t = requests.get(url)

soup = BeautifulSoup(t.text, features = 'html.parser')
books = soup.findAll('div', {'class' : 'info'})

for i in range(101):
    book = books[i].find('div', {'class' : 'title'}).find('a').text
    author = books[i].find('ul', {'class' : 'contributors-list list'}).find('a').text

    print(book, '-', author)
