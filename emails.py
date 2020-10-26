import smtplib
import getpass

mail_user = getpass.getpass("Podaj login: ")
mail_password = getpass.getpass("Podaj hasło: ")

sent_from = mail_user

sent_to = getpass.getpass("Podaj maila: ")

subject = "Taurus Mercatus - sygnal"

body = "To jest tresc maila"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, sent_to, subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(mail_user, mail_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()
    
    print("Wysłano!!!")
except:
    print("Coś nie działa!!!")