from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from html2text import HTML2Text
import smtplib
import csv
import random
from time import strftime


class PersonalizedGroupMail:
    def __init__(self, subject, sender, message=None, recipients=[]):
        self.msg = message
        self.htmlmsg = None
        self.names = []
        self.common_pm = ''
        self.salutations = []
        self.personalmsgs = []
        self.recipients = recipients
        self.ishtml = False
        self.username = None
        self.password = None
        self.host = None
        self.port = None
        self.smtp = smtplib.SMTP()
        self.my_email_address = sender
        self.subject = subject
        self.html2text = HTML2Text()

    def get_message_from_text(self, filepath=None):
        f = open(filepath, 'rb')
        self.msg = ''.join(f.readlines())
        f.close()

    def get_message_from_html(self, filepath):
        f = open(filepath, 'rb')
        self.htmlmsg = ''.join(f.readlines()).decode('utf-8-sig')
        f.close()
        self.ishtml = True

    def get_recipients_from_csv(self, filepath, column=1):
        self.recipients = self._csv_reader(filepath, column)

    def get_names_from_csv(self, filepath, column=1):
        self.names = self._csv_reader(filepath, column)

    def get_salutations_from_csv(self,filepath, column=1):
        self.salutations = self._csv_reader(filepath, column)

    def get_personalized_messages_from_csv(self, filepath, column=1):
        self.personalmsgs = self._csv_reader(filepath, column)

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

    def set_default_salutation(self, s):
        self.salutations = [s for x in self.salutations if x == '']
        for i in range(len(self.recipients) - len(self.salutations)):
            self.salutations.append(s)

    def set_default_personalized_message(self, m):
        self.salutations = [m for x in self.personalmsgs if x == '']
        for i in range(len(self.recipients) - len(self.personalmsgs)):
            self.personalmsgs.append(m)

    def set_connection(self, host, port):
        if host is not None and port is not None:
            self.host = host
            self.port = port
        self.smtp.connect(self.host, self.port)
        pass

    def authenticate(self, username, password, tls=True):
        if tls:
            self.smtp.starttls()
        if username is not None and password is not None:
            self.username = username
            self.password = password
        self.smtp.login(self.username, self.password)
        pass

    def send(self):
        if self.ishtml:
            firstpara = self.htmlmsg.find('<p')
            for i in range(len(self.recipients)):
                self.smtp.sendmail(self.my_email_address, self.recipients[i], self._compose_html(i, firstpara))
        else:
            for i in range(len(self.recipients)):
                self.smtp.sendmail(self.my_email_address, self.recipients[i], self._compose_text(i))
        self.smtp.quit()

    def _csv_reader(self, filepath, column):
        f = open(filepath, 'rb')
        r = csv.reader(f)
        l = []
        for row in r:
            l.append(row[column-1])
        f.close()
        l = [x for x in l if x != '']
        return l

    def _compose_html(self, index, begin):
        msghtml = self.htmlmsg[:begin] + '<p>' + self.salutations[index] + ' ' + self.names[index] + ',' + '</p><p>' + self.common_pm + ' ' + self.personalmsgs[index] + '</p>' + self.htmlmsg[begin:]
        msgplain = self.html2text.handle(msghtml)
        msg = MIMEMultipart('alternative')
        textMIME = MIMEText(msgplain, 'plain')
        htmlMIME = MIMEText(msghtml, 'html')
        msg.attach(textMIME)
        msg.attach(htmlMIME)
        msg['Subject'] = self.subject
        msg['From'] = self.my_email_address
        msg['To'] = self.recipients[index]
        msg['Date'] = strftime('%B %d, %Y %I:%M:%S %p')
        return msg.as_string()

    def _compose_text(self, index):
        msg = MIMEText(self.salutations[index] + ' ' + self.names[index] + ',\n\n' + self.common_pm + ' ' + self.personalmsgs[index] + '\n\n' + self.msg)
        msg['Subject'] = self.subject
        msg['From'] = self.my_email_address
        msg['To'] = self.recipients[index]
        msg['Date'] = strftime('%B %d, %Y %I:%M:%S %p')
        return msg.as_string()


