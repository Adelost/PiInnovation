import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "rbpimailbox@gmail.com"
password = "rhubarbpie"

# Setup message text
# TODO: Convert html to plain text to prevent duplication
# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
text = "Hi!\nYou have new post in your connected post box\n\nBest Regards\nEricsson post box"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       You have new post in your connected post box<br><br>
    Best Regards<br>
    Ericsson post box<br>
    </p>
  </body>
</html>
"""


def sendTo(recipient):
    """ Sends an arbitrary email to the specified email address. """
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Pi email test"
    msg['From'] = sender
    msg['To'] = recipient
    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(sender,password)
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()