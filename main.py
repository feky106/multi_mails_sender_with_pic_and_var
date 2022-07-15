# Import modules
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
### Add new subclass for adding attachments
from email.mime.application import MIMEApplication



def log_in(mail_from, password):
    global server

    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)
    server.login(mail_from, password)
    print('loged in')
    return mail_from


def mail_creation(mail_to,mail_from, name, dep):
    # Define the HTML document
    with open('html_file.html') as f:
        f1 = f.read()
        f2 = f1.replace('name_replace', name)
        html = f2.replace('dep_replace', dep)

    # Define a function to attach files as MIMEApplication to the email
    def attach_file_to_email(mail_body, filename, extra_headers=None):
        with open(filename, "rb") as f:
            file_attachment = MIMEApplication(f.read())
        file_attachment.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        # Set up the input extra_headers for img
            ## Default is None: since for regular file attachments, it's not needed
            ## When given a value: the following code will run
                ### Used to set the cid for image

        if extra_headers is not None:
            for name, value in extra_headers.items():
                file_attachment.add_header(name, value)
        mail_body.attach(file_attachment)

    # Create a MIMEMultipart class, and set up the From, To, Subject fields
    mail_body = MIMEMultipart()
    mail_body['From'] = mail_from
    mail_body['To'] = mail_to
    mail_body['Subject'] = 'subject of the mail'


    mail_body.attach(MIMEText(html, "html"))



    def attach_file_to_email(mail_body, filename, extra_headers=None):
        with open(filename, "rb") as f:
            file_attachment = MIMEApplication(f.read())
        file_attachment.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        if extra_headers is not None:
            for name, value in extra_headers.items():
                file_attachment.add_header(name, value)
        mail_body.attach(file_attachment)
    attach_file_to_email(mail_body, 'img.png', {'Content-ID': '<myimageid>'})
    mail_string = mail_body.as_string()   # Convert it as a string
    server.sendmail(mail_from, mail_to, mail_string)

    print(f'your mail sent to [ {mail_to} ] successfully')


def end():
    server.quit()
    print('Your connection End successfully')


