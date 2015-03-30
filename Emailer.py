import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "pi@ericsson.com"

# Setup message text
# TODO: Convert html to plain text to prevent duplication
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
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

    s = smtplib.SMTP('localhost')
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()