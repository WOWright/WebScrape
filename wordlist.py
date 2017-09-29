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
parts = ( 
 'Adjective',
 'Adverb',
 'Conjunction',
 'Determiner',
 'Interjection',
 'Noun',
 'Numeral',
 'Preposition',
 'Pronoun',
 'Proper noun',
 'Verb')

temp = souped.findAll('td')

with open("words2.txt", 'w') as f:
    for i,q in enumerate(temp):
        
        try:
            # try to print the word and the part of speech (usually one later)
            f.write(q['data-string'])
            w = temp[i+1].text
            
            if w in parts:
                f.write(',' + w + '\n')
            else:
                f.write(',\n')
                
        except:
            pass

