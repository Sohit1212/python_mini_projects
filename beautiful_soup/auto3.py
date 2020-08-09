#import urllib.request
import requests
from bs4 import BeautifulSoup
url = "http://quotes.toscrape.com"
#weburl = urllib.request.urlopen(url)
#if weburl.getcode() == 200:
    #data = weburl.read()
    #print(data)
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
#print(soup)
quotes = soup.find_all('span',class_='text')
authors = soup.find_all('small',class_='author')
tags = soup.find_all('div',class_='tags')

#print(quotes)
for i in range(0,len(quotes)):
    print(quotes[i].text,end=" -")
    print(authors[i].text)
    quoteTags = tags[i].find_all('a',class_='tag')
    print("tags:",end=" ")
    for tag in quoteTags:
        print(tag.text,end=" ")
    print()
