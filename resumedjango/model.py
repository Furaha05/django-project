import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cgi

# Set up the SMTP server
smtp_server = 'smtp.listless17.top'
smtp_port = 587
smtp_username = 'jojo@listless17.top'
smtp_password = 'Furaha_05'

# Get the form data
form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
message = form.getvalue('message')

# Create the email message
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = smtp_username
msg['Subject'] = 'Contact Us Form Submission'
msg.attach(MIMEText(f"Name: {name}\nEmail: {email}\n\n{message}"))

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, smtp_username, msg.as_string())

# Redirect the user back to the contact page
print('Content-Type: text/html')
print('Location: /reachus.html')
print()
