#!/usr/bin/python3

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

def send_email(Subject,Result):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USERNAME = os.environ['SMTP_USER']
    SMTP_PASSWORD = os.environ['SMTP_PASSWORD']

    EMAIL_TO = os.environ['EMAIL_TO']
    EMAIL_CC = os.environ['EMAIL_CC']
    EMAIL_FROM = os.environ['EMAIL_FROM']
    EMAIL_SUBJECT = Subject
    EMAIL_BODY = Result
    
    msg = MIMEText(EMAIL_BODY)
    msg['Subject'] = EMAIL_SUBJECT
    msg['To'] = EMAIL_TO
    msg['Cc'] = EMAIL_CC
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

# if __name__=='__main__':
#     send_email()