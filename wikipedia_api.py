'''
Simple Wikipedia Web Crawler using json and beautiful soup

The first part searchs wikipedia for your term using their API (returns json)

The second part picks a link and crawls randomly through subsequent pages

M. Hanchak
06OCT17
'''

import random
from bs4 import BeautifulSoup
import json
import requests

# this is the wikipedia API:
searchUrl = 'http://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch='

# ###################### Enter your search term ################################
searchTerm = 'science'
# ##############################################################################

print(searchTerm)

# get wikipedia's search results from your term
page = requests.get(searchUrl + searchTerm)
parsed = json.loads(page.text)

# json stuff to get the actual links:
links = [item['title'] for item in parsed['query']['search'] ]

# get one of them at random and get its wikipedia page
pageUrl = 'http://en.wikipedia.org/wiki/'
getOne = random.choice(links).replace(' ','_')
print(getOne)
page = requests.get(pageUrl + getOne)

# loop through other random links in the subsequent pages
for i in range(10):
    try:
        soup = BeautifulSoup(page.text, 'html.parser')  # soupify the html
        
        content = soup.find(id="mw-content-text")  # get links only in this structure
        
        newlinks = [a['title'] for a in content.findAll('a') if a.has_attr('title')]  
        # get only good links
        
        getOne = random.choice(newlinks)  # pick one
        
        while getOne.find(':') != -1:
            getOne = random.choice(newlinks)  # make sure it doesnt have a colon in it.
        
        
        pageUrl = 'http://en.wikipedia.org/wiki/' + getOne.replace(' ','_')  # form new url
    
        page = requests.get(pageUrl)  # get new page (try to anyway)
        print(getOne)

    except:
        pass
    
    
