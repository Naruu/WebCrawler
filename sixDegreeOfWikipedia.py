from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

pages = set()
random.seed(datetime.datetime.now())

def getLinks(articleUrl) :
    global pages
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj= BeautifulSoup(html)
    try :
        print(bsObj.h1.get_text())
        print(bsObj.find(id = "mw-content-text").findAll("p")[0])
        print(bsObj.find(id = "ca-eidt").find("span").find("a").attrs["href"])
    except AttributeError :
        print("This page is missing something.")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")) :
        if 'href' in link.attrs :
            if link.attrs['href'] not in pages :
                newPage = link.atttrs['href']
                print("---------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")