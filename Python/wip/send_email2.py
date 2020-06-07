#!/usr/bin/python3

from email.mime.text import MIMEText
import smtplib

def send_email(Subject,Result):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USERNAME = user
    SMTP_PASSWORD = passwd

    EMAIL_TO = [recipients]
    EMAIL_FROM = user
    EMAIL_SUBJECT = Subject
    EMAIL_SPACE = ", "
    EMAIL_BODY = Result
    
    msg = MIMEText(EMAIL_BODY)
    msg['Subject'] = EMAIL_SUBJECT
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

# if __name__=='__main__':
#     send_email()