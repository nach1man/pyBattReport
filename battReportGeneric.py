import subprocess as s
import os
import email
import smtplib
import easygui as g
from time import sleep
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Image for message boxes
image = "exampleImage.ico"
msg = "Would you like to run the battery report?"
title = "Battery Report"
choices = ["Yes", "No"]
reply = g.ynbox(msg=msg, image=image, title=title)

# Check to see if the user selected yes
if reply == False:
    print("Exiting...")
    sleep(2)
    exit()
else:
    pass

# # Current user's username
username = os.environ['USERNAME']
computername = os.environ['COMPUTERNAME']

# Run powercfg and create report
filepath = "C:/Users/" + username + "/Documents"
batteryReport = s.run(['powercfg','/batteryreport', '/output', filepath +'/battReport_' + computername + '.html'], check=True)

# # Email with attachment will go here
# # Email variables needed
subject = "Battery report from user: " + username + "."
whereEmail = "Enter an email to send the report to: "
receivingEmail = "[example@receivingemail.com]"
senderEmail = "[example@senderemail.com]"
body = "Battery Report for user: " + username + " on computer: " + computername + "."

# # SMTP server and port
port = '[port]'
smtpServer = '[smtpIp]'

# # Create email and add attachment
message = MIMEMultipart()
message["From"] = senderEmail
message["To"] = receivingEmail
message["Subject"] = subject

# # Add the message to the body
message.attach(MIMEText(body, 'plain'))

# # File needed to be attached
filename = "C:/Users/" + username + "/Documents/battReport_" + computername + ".html"

# # Open and read file
with open (filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# # Encode the file as ASCII
encoders.encode_base64(part)

# # Add headers as key/value pair to attachment part
part.add_header(
    "Content-Disposition", f"attachment; filename = {filename}",
)

# # Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# # Try to connect to the server and send an email
try:
    server = smtplib.SMTP(smtpServer, port)
    server.sendmail(senderEmail, receivingEmail, text)
    print("Battery Report was emailed to batteryreport@essenceglobal.com !")
except Exception as e:
    print(e)
finally:
    server.quit()

# # Deleting the report will go here
# Check to see if the battReport.html file exists
if os.path.isfile(filename) == True:
    os.remove(filename)
    g.msgbox(msg="All done!", title="Finished Successfully", image=image)
else:
    print("Nope")


exit()





