__author__ = 'Ibrahim'


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import html2text
import smtplib
import csv
import random


class PersonalizedGroupMail:
    def __init__(self):
        self.msg = None
        self.names = []
        self.salutations = []
        self.personalmsgs = []
        self.recipients = []
        self.filepath = None
        self.ishtml = False
        self.host = None
        self.port = None
        print "This is a test class."

    def get_message(self, message):
        self.msg = message
        print "Message received!"

    def get_message_from_text(self, filepath=None):
        f = open(filepath, 'rb')
        self.msg = ''.join(f.readlines())
        print "Message loaded!"

    def get_message_from_html(self, filepath=None):
        print "HTML Loaded"

    def get_recipients(self, rdata):
        self.recipients = rdata
        print "Recipients loaded!"

    def get_recipients_from_csv(self, filepath=None, column=0):
        self.recipients = self._csv_reader(filepath, column)
        print "Recipients from file loaded!"

    def get_names(self, ndata):
        self.names = ndata
        print "Names loaded!"

    def get_names_from_csv(self, filepath=None, column=0):
        self.names = self._csv_reader(filepath, column)
        print "Names from file loaded!"

    def get_salutations(self, sdata):
        self.salutations= sdata
        print "Salutations loaded!"

    def get_salutations_from_csv(self,filepath=None, column=0):
        self.salutations = self._csv_reader(filepath, column)
        print "Salutations from file loaded!"

    def get_personalized_messages(self, pmdata):
        self.personalmsgs = pmdata
        print "Personalized messages loaded!"

    def get_personalized_messages_from_csv(self, filepath=None, column=0):
        self.personalmsgs = self._csv_reader(filepath, column)
        print "Personalized messages from file loaded!"

    def randomize_salutations(self):
        if len(self.salutations) < len(self.recipients):
            while len(self.salutations) < len(self.recipients):
                self.salutations += self.salutations                    # exponential list growth
            self.salutations = self.salutations[:len(self.recipients)]  # truncating after last iteration
        random.shuffle(self.salutations)

    def randomize_personalized_messages(self):
        if len(self.personalmsgs) < len(self.recipients):
            while len(self.personalmsgs) < len(self.recipients):
                self.personalmsgs += self.personalmsgs                    # exponential list growth
            self.personalmsgs = self.personalmsgs[:len(self.recipients)]  # truncating after last iteration
        random.shuffle(self.personalmsgs)

    def _csv_reader(self, filepath, column):
        f = open(filepath, 'rb')
        r = csv.reader(f)
        l = []
        for row in r:
            l.append(row[column-1])
        f.close()
        l = [x for x in l if x != '']
        return l
