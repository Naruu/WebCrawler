import smtplib
from email.mime.text import MIMEText

msg = MIMEText("The body of the email is here")

msg['Subject'] = 'An email alert'
msg['From'] = 'sender@gmail.com'
msg['To'] = 'receiver@gmail.com'

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()