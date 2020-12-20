import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Senders Mail Id'
email['to'] = 'Recivers Mail Id'
email['subject'] = 'Subject of mail'
email.set_content(html.substitute({'name':'XYZ'}),'html')


with smtplib.SMTP(host='smtp.gmail.com', port = 587 ) as smtp:
  smtp.ehlo()0000000000
  smtp.starttls()
  smtp.login('SendermailID@gmail.com','Yoursecretpassword')
  smtp.send(email)
  
