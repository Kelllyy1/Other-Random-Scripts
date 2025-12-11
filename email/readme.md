# Steps to Run
1. Run ```python email.py```
2. Enter the recipient email
3. Enter the sender (your) email
4. Enter the sender (your) password
5. Verify with the recipient that the email was received

# Breakdown of code
Import the necessary libraries

```
import os
import smtplib
import getpass
```

Create a session - port 587 is used for Gmail
```
s = smtplib.SMTP('smtp.gmail.com', 587)
```

Start the SMTP connection in TLS mode (Transport Layer Security)
```
s.starttls()
```

Get the username and password of the sender and recipient
```
to_email = input("Enter email recipient:")
username = input("Enter email (sender):")
password = getpass.getpass("Enter password")
```

Login and authenticate the sender
>To do this, the sender's Gmail account would need to have 2-Factor Authentication enabled and it will be necessary to create an App Password, and enter this (instead of the password) during program runtime. I used this link for [steps on creating an App Password](https://support.google.com/accounts/answer/185833?sjid=239060409917481262-NA)
```
s.login(username, password)
```

A *subject* and *msg* are necessary to send an email, so define those variables
```
subject = "Bath & Body Works Order"
msg = "Please order new Bath & Body Works items\n\n"
message = 'Subject: {}\n\n{}'.format(subject, msg)
```

Now it's time to send the mail
```
s.sendmail(username, to_email, message)
```

Be sure to terminate the session to avoid wasting resources
```
s.quit()
```
[Guide to help with emails in Python](https://www.geeksforgeeks.org/python/send-mail-gmail-account-using-python/)
