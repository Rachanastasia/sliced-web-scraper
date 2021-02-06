import json
import re
from bs4 import BeautifulSoup
import requests


def get_web_content(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    return soup

def parse_li_tags(lis):
    # could next be a number?
    for l in lis: 
        # check if number 
        # check if next is valid type
        # check against enum for units
        

def generate_recipes():
    d = open('recipe-links.json', )
    data = json.load(d)

    for url in data:
        soup = get_web_content(url)

        li = soup.find_all('li') #returns a list

        title = soup.find('h1').text
        print(title)

        if li == None:
            print('There are no <li> tags.')
            return
        
        parse_li_tags(li)
        #re.compile('[a-z]+')



generate_recipes()


