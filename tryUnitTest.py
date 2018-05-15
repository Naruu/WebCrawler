from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class TestWikipedia(unittest.TestCase) :
    bsObj = None
    def setUpClass():
        global bsObj
        url = 'http://en.wikipedia.org/wiki/Monty_Python'
        bsObj = BeautifulSoup(urlopen(url))

    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find("h1").get_text()
        self.assertEqual("Monty Python", pageTitle)
        
if __name__ == '__main__' :
    unittest.main()