from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def ngrams(input, n) :
    content = re.sub('\n+', " ", input)
    content = re.sub(' +', " ", content)
    content = bytes(content, "UTF-8")
    content = content.decode("ascii", "ignore")
    print(content)
    content = content.split(' ')
    output =[]
    for i in range(len(content) -n+1) :
        output.append(content[i:i+n])
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_programming_language")
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {"id" : "mw-content-text"}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print("2 -grams count is : " + str(len(ngrams)))