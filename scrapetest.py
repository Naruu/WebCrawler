from urllib.request import urlopen
from bs4 import BeautifulSoup

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(textPage.read()), 'utf-8')

html = urlopen("http://www.en.wikipedia.org/wiki/Python_(programming_languages)")
bsObj = BeautifulSoup(html)
content = bsObj.find("div", {"id" : "mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")