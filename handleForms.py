import requests

params = {'firstname' : 'Naruu', 'lastname' : 'L'}
r= requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)