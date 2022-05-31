# Import modules
from email import encoders
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
### Add new subclass for adding attachments
##############################################################
from email.mime.application import MIMEApplication
##############################################################
from datetime import datetime

import shutil
import os

# Define the HTML document
html = '''
    <html>
        <body>
            <h1>Pytest report of test execution</h1>
            <p><=========This is an automatically generated email – please do not reply. ================><p>
        </body>
    </html>
    '''

# Define a function to attach files as MIMEApplication to the email
##############################################################
def attach_file_to_email(email_message, filename):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    # Add header/name to the attachments    
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Encode the payload using Base64
    encoders.encode_base64(file_attachment)
    # Attach the file to the message
    email_message.attach(file_attachment)
##############################################################    

# Set up the email addresses and password. Please replace below with your email address and password
email_from = 'code.tester2021@gmail.com'
app_password = 'awdtrwovjtbfkrgt'
# email_to = ['vivek.anand@veris.in', 'shailendra.tiranga@veris.in', 'amogh.banta@veris.in']
# email_to = ['vivek.anand@veris.in', 'shailendra.tiranga@veris.in']
email_to = ['vivek.anand@veris.in']

# Generate today's date to be included in the email Subject
date_str = datetime.today().strftime('%Y-%m-%d')

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = ', '.join(email_to)
email_message['Subject'] = f'Report email - {date_str}'

# Zipping screenshots
def zip_file():
    try:
        os.makedirs(os.path.join("screenshot_archives", os.path.dirname("screenshots_zip")), exist_ok=True)
        shutil.make_archive("./screenshot_archives/screenshots_zip", 'zip', "./screenshot")
    except Exception as e:
        print("e: ", e)


# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))

# Attach more (documents)
##############################################################
zip_file()
attach_file_to_email(email_message, 'report.html')
attach_file_to_email(email_message, 'screenshot_archives/screenshots_zip.zip')
# attach_file_to_email(email_message, 'report.xls')
##############################################################
# Convert it as a string
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email
def send_email():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, app_password)
        server.sendmail(email_from, email_to, email_string)

if __name__ == '__main__':
    send_email()
