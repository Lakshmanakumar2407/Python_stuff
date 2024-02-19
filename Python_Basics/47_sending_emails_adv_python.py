import smtplib, os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# from email.mime.audio import MIMEAudio # used for mpeg
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders

n = EmailMessage()

email_address = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')
smtp_server = 'smtp.gmail.com'
smtp_port = 465
email_subject = 'This is an attachemnet test email'
email_to = email_address

# with smtplib.SMTP('smtp.gmail.com',587) as smtp:
#     smtp.ehlo() # identifying ourselves with the server
#     smtp.starttls() # Encrypting our message
#     smtp.ehlo() #identify oursleves after encrypting

# using email message

# msg = EmailMessage()
# msg['Subject']  = 'Hello from the other side!'
# msg['From'] = email_address
# msg['To'] = email_address
# msg.set_content("Test email Baka")

# CREATING A MESSAGE
msg = MIMEMultipart() # it's a class
msg['Subject'] = email_subject
msg['From'] = email_address
contact_list = [email_address]
msg['To'] = ', '.join(contact_list)

# CREATING A TEXT
# msg.attach(MIMEText('This is a simple plain email', "plain"))
msg.attach(MIMEText('<h3>This is a simple plain email</h3>', "html"))

# # ATTACHING A IMAGE
# with open(r'C:\Users\laksh\OneDrive\Pictures\images.png','rb') as img:
#     msg.attach(MIMEImage(img.read(), name = 'Sample_pic.png'))

# # ATTCHING A AUDIO
# with open(r'C:\Users\laksh\Music\Anirudh Ravichander - Pathala Pathala.mp3', 'rb') as aud:
#     # It look like I can't send the message directly...
#     aud_attachement = MIMEBase('audio', 'mp3', name = 'pathala pathala') # the arguments are maintype and subtype which should be apssed as string
#     aud_attachement.set_payload(aud.read()) # passing the main file
#     encoders.encode_base64(aud_attachement)
#     msg.attach(aud_attachement)

# ATTACHING A DOCUMENT
# with open('extracted.md', encoding='utf-8') as md:
#     msg.attach(MIMEApplication(md.read(), name = 'Novel.md'))

# with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: # using context manager to close our connection automatically

#     # smtplib.SMTP_SSL().close() # closes the connection to server, context manager help us close this automatically

#     # NO NEED TO USE OTHER MESSAGES LIKE ABOVE EXAMPLE IF SMTP_SSL IS USED

#     smtp.login(email_address,password) # logging in to our email server

#     # subject = 'This is Python !!!'
#     # body = 'Test email dummy'

#     # msg = f'Subject:{subject}\n\n\n{body}'

#     # smtp.sendmail(email_address,'vtlakshman@gmail.com',msg) # arguments are SENDER, RECIEVER, MESSAGE

#     smtp.send_message(msg)
    
try:
    with smtplib.SMTP_SSL(smtp_server,smtp_port) as smtp:
        smtp.login(email_address,password)
        smtp.sendmail(email_address,email_to,msg.as_string())
    print('Email sent Successfully!!')
except Exception as e:
    print(f'Error : {e}')