import json

from bs4 import BeautifulSoup
import requests


def get_web_content(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    return soup


def generate_recipes():
    d = open('recipe-links.json', )
    data = json.load(d)

    for url in data:
        soup = get_web_content(url)
        article = soup.find('article')
        li = soup.find_all('li')

        title = article.h1.text
        print(title)
        for l in li:
            #parse xml
            print(l)


generate_recipes()