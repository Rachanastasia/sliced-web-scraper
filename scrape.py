from bs4 import BeautifulSoup
import requests

source = requests.get(
    'https://www.thewholesomedish.com/the-best-pancake-recipe').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')

title = article.h1.text

ingredients = set()
li = soup.find_all('li')
#currently getting instruction
#currently getting comments too

for l in li:
    ingredients.add(l)
    print(l)
# this gave instructions
# how do I get only ingredients?
ulli = article.ul.li.text




   