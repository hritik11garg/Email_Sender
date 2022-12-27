from email.message import EmailMessage
import ssl
import smtplib

#Enter your/sender email-id below
email_sender = ''
#Enter the password after doing 2-factor for the email-id and then clicking on App passwords then click on select app and then on custom and name it python which will generate a password which you will copy and paste it below
email_password = ''
email_receiver = input("Enter the email:\n")

subject = input("\nEnter the subject:\n")
body = input("\nEnter the message(Note: pressing enter will end the message n")

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
