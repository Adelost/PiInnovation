import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "rbpimailbox@gmail.com"
password = "rhubarbpie"

# Setup message text
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
    """Sends an arbitrary email to the specified email address."""
    # Create message container
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Pi email test"
    msg['From'] = sender
    msg['To'] = recipient
    msg.attach(MIMEText(html, 'html'))

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(sender, password)
    print("Sent mail to:", recipient)
    # s.sendmail(sender, recipient, msg.as_string())
    s.quit()


def sendToAll(recipients):


    for r in list:
        sendTo(r)

