import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = '--YOUR NAME--'
email['to'] = 'Enter the mailID of your recepint'
email['subject'] = 'Here you can enter the subject line of your mail '

email.set_content('Your Email body goes here ..............')

with smtplib.SMTP(host='smtp.gmail.com', port = 587 ) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('SendermailID@gmail.com','Yoursecretpassword')
  smtp.send(email)
  
