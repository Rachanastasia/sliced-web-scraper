import json
import re
from bs4 import BeautifulSoup
import requests



def get_web_content(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    return soup

def parse_li_tags(lis):
    valid_units = {'tsp', 'tbsp', 'tablespoon', 'tablespoons', 'teaspoons', 'cup', 'cups'}
    
    def is_digit(t):
        number = re.search(r'^\d', t)
        if number: return True

    digit = re.compile('\d')
    i=0
    for l in lis: 
        i+=1
        for unit in valid_units:
            has_unit = re.search(f'{unit}', l.text)
            if has_unit:
                if is_digit(l.text) == True:
                    print(f'INGREDIENT: {l.text}')

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


