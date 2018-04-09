from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint

try :
    html = urlopen("http://pythonscraping.com/pages/page1.html")
except HTTPError as e :
    print(e)
else :
    bsObj = BeautifulSoup(html.read(), "lxml")
    pprint(bsObj)


html = urlopen("http://pythonscraping.com/pages/page1.html")
if html is None :
    print("URL is not found")
else :
    bsObj = BeautifulSoup(html.read(), "lxml")
    pprint(bsObj)