import smtplib
import pyinputplus as pyip
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


smtp_user = 'asiedusolo99@gmail.com'
server = 'smtp.gmail.com'
port = 587
msg = MIMEMultipart("alternative")
msg["Subject"] = 'Why,Oh why!'
msg["From"] = smtp_user
msg["To"] = "asiedusolo.sa@gmail.com"
msg.attach(MIMEText('\nsent via python', 'plain'))
password = pyip.inputPassword(prompt = 'Enter password: ', mask='*')
smtpObj = smtplib.SMTP(server, port)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(smtp_user, password)
s.sendmail(smtp_user, "asiedusolo.sa@gmail.com", msg.as_string())
s.quit()
print('Good so far')
