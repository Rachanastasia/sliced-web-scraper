from bs4 import BeautifulSoup
import requests

source = requests.get(
    'https://www.thewholesomedish.com/the-best-pancake-recipe').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

title = article.h1.text

ulli = article.ul.li.text

print(ulli, title)
