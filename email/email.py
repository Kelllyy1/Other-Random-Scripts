# email.py Send an email
# import the necessary libraries
import os
import smtplib
import getpass

# Create a session - port 587 is used for Gmail
s = smtplib.SMTP('smtp.gmail.com', 587)

# Start the SMTP connection in TLS mode (Transport Layer Security)
s.starttls()

# Get the username and password of the sender and recipient
to_email = input("Enter email recipient:")
username = input("Enter email (sender):")
password = getpass.getpass("Enter password")

# Authenticate the sender
s.login(username, password)

# A 'subject' and 'msg' are necessary to send an email, so define those variables
subject = "Bath & Body Works Order"
msg = "Please order new Bath & Body Works items\n\n"
message = 'Subject: {}\n\n{}'.format(subject, msg)

# Now it's time to send the mail
s.sendmail(username, to_email, message)

# Be sure to terminate the session to avoid wasting resources
s.quit()
