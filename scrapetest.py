from urllib.request import urlopen
from pprint import pprint

html = urlopen("http://pythonscraping.com/pages/page1.html")
pprint(html.read())