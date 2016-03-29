#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()

# if you are using port 587 you need to start TLS encryption
smtp_obj.starttls()

# now let's login using credentials
smtp_obj.login('username@gmail.com', 'password')

# now, let's send an email
smtp_obj.sendmail(' my_email_address@gmail.com ', ' recipient@example.com ',
                  'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')

# disconnect from SMTP server
smtp_obj.quit()



