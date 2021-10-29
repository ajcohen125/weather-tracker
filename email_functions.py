#Email connection & formatting
import smtplib
from email.message import EmailMessage
from datetime import date


#Email Login - #FIXME - Remove values before pushing
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""


def send_message(msg):
    #Sending email
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) #Email and APP Password(if using 2FA account)
        smtp.send_message(msg)
    
def send_broken_links(contacts, broken_links_list):
    msg = EmailMessage()
    msg["Subject"] = "Weather Program Broken Links ({0})".format(date.today().strftime("%m/%d/%Y"))
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = contacts
    
    message = ""
    for item in broken_links_list:
        message+= "\"{0}\" threw the error \"{1}\" with link {2}\n".format(item[0], item[1], item[2])
    
    msg.set_content(message)
    send_message(msg)

def send_no_internet(): #May not be able to use depending on how we setupt the email servers
    pass
