# Sliced Web Scraping

This repository is the testground for a web scraper using Python and Beautiful Soup to implement with [Sliced](https://github.com/Rachanastasia/sliced-client).

## Codebase

### recipehtml.py

This file contains `generate_requests()` which loops through a list of urls from `recipe-links.json` and turns them into soup. 

`parse_li_tags()` takes in an array of `li` tags and finds items that contain both a valid unit and a digit. 

This is currently returning all ingredients that follow the pattern: digit unit ingredient name. 

### valid-types.py

An ENUM with the valid types. 

### scrape.py

Beautiful soup test and notes. 
