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




    # "https://sallysbakingaddiction.com/crispy-chocolate-chip-cookies/",
    # "https://sallysbakingaddiction.com/all-butter-pie-crust/",
    # "https://www.allrecipes.com/recipe/22831/alfredo-sauce/",
    # "https://addapinch.com/broccoli-cheese-casserole-recipe/",
    # "https://www.simplyrecipes.com/recipes/chicken_paprikash/"
    # "https://www.delish.com/cooking/recipe-ideas/recipes/a57946/easy-white-chicken-chili-recipe/0"

