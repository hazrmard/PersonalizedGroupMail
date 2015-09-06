__author__ = 'Ibrahim'


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import html2text


class Compose:
    def __init__(self):
        self.msg = None
        self.filepath = None
        self.ishtml = False

    def getmessage(self, filepath=None):
        print "Message received!"
