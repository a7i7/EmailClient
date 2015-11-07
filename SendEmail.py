import sys
import imaplib
import getpass
import email
import datetime
import pickle
from simplecrypt import encrypt,decrypt
import getpass
import smtplib
import smtplib

class SendEmail:
	
	SMTP_MAIL_SERVER = "smtp.gmail.com"
	SMTP_MAIL_PORT = 587
	
	def send_email(self):
	    TO = self.receiver if type(self.receiver) is list else [self.receiver]

	    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
	    """ % (self.username, ", ".join(TO), self.subject, self.content)

	    try:
	        server = smtplib.SMTP(self.SMTP_MAIL_SERVER, self.SMTP_MAIL_PORT)
	        server.ehlo()
	        server.starttls()
	        server.login(self.username , self.password)
	        server.sendmail(self.username, TO, message)
	        server.close()
	        print 'Successfully sent the mail'
	    except:
	        print "Failed to send mail"
	 

	def __init__(self,username,password,receiver,subject='No Subject',content=None,contentFile=None,attachFile=None):
		self.username = username
		self.password = password
		self.receiver = receiver
		self.subject = subject
		self.content = content
		self.contentFile = contentFile
		self.attachFile = attachFile

