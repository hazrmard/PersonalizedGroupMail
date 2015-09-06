__author__ = 'Ibrahim'


from smtplib import SMTP
import csv


class Send:
    def __init__(self):
        self.host = None
        self.port = None

    def sendmessage(self):
        print "Messages Sent!"
