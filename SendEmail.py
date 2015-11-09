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
	
	SMTP_MAIL_SERVER = None
	SMTP_MAIL_PORT = 587
	SMTP_MAIL_SERVER_HOTMAIL = "smtp.live.com"
	SMTP_MAIL_SERVER_GMAIL = "smtp.gmail.com"

	def send_email(self):

		if 'gmail.com' in self.username:
			self.SMTP_MAIL_SERVER = self.SMTP_MAIL_SERVER_GMAIL
		else:
			self.SMTP_MAIL_SERVER = self.SMTP_MAIL_SERVER_HOTMAIL
		
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
