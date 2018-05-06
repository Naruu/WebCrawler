from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint

baseUrl = "https://github.com/rechsteiner/Parchment/tree/master/Parchment/Classes"
html = urlopen(baseUrl)
bsObj = BeautifulSoup(html)

files = []
table = bsObj.find("div", role="main").find("table", {"class" : "files js-navigation-container js-active-navigation-container"}).find("tbody").find_all("tr", {"class" : "js-navigation-item"})

for tr in table :
    file = tr.find("a", {"class" : "js-navigation-open"}).get_text()
    files.append(file)
