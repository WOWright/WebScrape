# -*- coding: utf-8 -*-
"""
Web scraping example 2
"""

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/2-in-1-Laptops/SubCategory/ID-3090?Tpk=ultrabook'
        
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

containers = page_soup.findAll('div',{'class':'item-container'})


filename = 'products.csv'

with open(filename,'w') as f:

    headers = 'brand, product_name, shipping, price\n'
    f.write(headers)
    
    for container in containers[:8]:
        brand = container.div.div.a.img['title']
        #brand = 'None'
        
        title_container = container.findAll('a',{'class':'item-title'})
        product_name = title_container[0].text
        
        shipping_container = container.findAll('li',{'class':'price-ship'})
        shipping = shipping_container[0].text.strip()                            
        
        temp = container.findAll('li',{'class':'price-current'})[0].text.strip()
        price = temp[3:9]
        
        #print('brand:' + brand)
        #print('product name:' + product_name)
        #print('shipping cost:' + shipping)
        
        f.write(brand + ',' + product_name.replace(',','|') + ',' + shipping + ',' + price +'\n')
        
