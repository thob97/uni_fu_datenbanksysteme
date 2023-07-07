from bs4 import BeautifulSoup
import requests
from collections import Counter

url = 'https://www.heise.de/thema/https/seite-'
pages = 5

# returns the html code of a given url
def getPage(url):
    return BeautifulSoup(requests.get(url).text,'lxml')

# returns a list of all titles (in "Datenstruktur", jeder Eintrag is prim_key)
def get_titles():
    all_titles = []
    # goes through each page
    for seite in range(1,pages+1): 
        # getPage
        page = getPage(url+str(seite)) 
        # fing all titles
        titles = page.findAll('span',class_='a-article-teaser__title-text')
        #goes through each title and appends to a list, also strips unnecessary chars
        for title in titles: 
            all_titles.append(title.text.strip())
    return all_titles

# returns top n used words of all titles
def top_words(n, all_titles): 
    aio_list = ""
    # goes through all titles and combines them to one list
    for title in all_titles:
       aio_list +=title + ' '
    # splits each word in a new list
    words = aio_list.split()
    # counts all wourds and returns top n
    top_n_words = Counter(words).most_common(n) 
    return top_n_words
    
print(top_words(3,get_titles()))