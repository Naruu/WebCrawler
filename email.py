import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject, body) :
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'sender@gmail.com'
    msg['To'] = 'receiver@gmail.com'

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

bsObj = BeautifulSoup(urlopen("http://isitchristmas.com/"))
while(bsObj.find("a", {"id":"answer"}).attrs['title'] == 'NO') :
    print("It is not Christmas yet.")
    time.sleep(3600)
sendMail("It's Christmas", "According to the site. Let's celebrate. Hooray!")