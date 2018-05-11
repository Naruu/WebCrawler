import requests
"""
##submit forms
params = {'firstname' : 'Naruu', 'lastname' : 'L'}
r= requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)

##upload images
files = {'uploadFile' : open('./logo.jpg', 'rb')}
r=requests.post("http://pythonscraping.com/pages/processing2.php", files=files)
print(r.text)

## send cookies
params = {'firstname' : 'Naruu', 'lastname' : 'L'}
r= requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print(r.text)

print(r.cookies.get_dict())
print("----------\n Going to pofile page....")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)

#use sessions
session = requests.Session()

s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print(s.cookies.get_dict())

s =session.get("http://pythonscraping.com/pages/cookies/profile.php")
"""

##auth
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('Naruu', 'password')
r = requests.post(url = "http://pythonscraping.com/pages/auth/login.php", auth = auth)
print(r.text)