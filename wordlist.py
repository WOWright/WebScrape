# -*- coding: utf-8 -*-
"""
explore word list from duolingo inspect element

Created on Thu Aug 31 09:13:00 2017

@author: HanchaMS
"""
from bs4 import BeautifulSoup as soup

with open("wordlist2.txt") as f:
    
    htmlcode = f.read()

souped = soup(htmlcode, "html.parser")    


'''


containers = souped.findAll("span",{"class":"hoverable-word hover"})

for container in containers:
    print(container.text)
    

containers = souped.findAll('span',{'class':'hover'})


with open("words.csv", 'w') as f:
    for container in containers:
        f.write(container.text + '\n')
'''


temp = souped.findAll('td')

with open("words2.txt", 'w') as f:
    for q in temp:
        try:
            f.write(q['data-string'] + '\n')
        except:
            pass

