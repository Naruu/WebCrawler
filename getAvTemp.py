from bs4 import BeautifulSoup, NavigableString
from urllib.request import urlopen
import matplotlib.pyplot as plt

html = urlopen("http://www.weather.go.kr/weather/climate/past_table.jsp?stn=108&yy=2018&obs=07&x=21&y=8")
bsObj = BeautifulSoup(html)
table = bsObj.find("div", {'id': 'content_weather'}).find("tbody")
day = range(1,32)
temp = []
for tr in table :
    if isinstance(tr, NavigableString) :
        pass
    else :
        temp.append(float(tr.contents[3].get_text()))

plt.plot(day, temp[:31])
plt.title('2018 January Average Temperature of Seoul')
plt.xlabel('Date')
plt.ylabel('Average Temperature(°C)')
plt.show()
