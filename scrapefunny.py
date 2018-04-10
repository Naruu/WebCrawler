from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from pprint import pprint


def writeIn(text) :
    f = open('parsed.txt', 'w', encoding='utf-8')
    f.write(str(text))
    f.close()

def getbsObj(url) :
    try :
        html = urlopen(url)
    except HTTPError as e :
        return None
    try :
        bsObj = BeautifulSoup(html.read())
    except AttributeError as e :
        return None
    return bsObj

bsObj = getbsObj("https://twitter.com/gagjidol")
if bsObj == None :
    print("Title could not be found")
else :
    writeIn(bsObj)
