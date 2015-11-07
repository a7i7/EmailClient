import sys
import imaplib
import getpass
import email
import datetime
import pickle
from simplecrypt import encrypt,decrypt
import getpass
from SendEmail import *
"""https://www.google.com/settings/security/lesssecureapps"""

IMAP_URL = "imap.gmail.com"
arguments = {}

def initializeArguments(arg):
	arguments["send"] = False
	arguments["read"] = False
	arguments["address"] = None
	arguments["attach"] = None
	arguments["content"] = None
	arguments["text"] = None
	arguments["subject"] = None
	for a in arg:
		addArgument(a)

def addArgument(arg):
	if(arg.startswith("-")==False):
		return 1
	arg = arg.replace('-','')
	options = arg.split('=')
	if options[0] in arguments.keys():
		if type(arguments[options[0]])==type(False):
			if(len(options)==1):
				arguments[options[0]]=True
				return 0
			else:
				return 1
		else:
			if(len(options)==2):
				arguments[options[0]]=options[1]
				return 0
			else:
				return 1
	else:
		return 1

def main(argv):
	initializeArguments(argv)
	username = raw_input("Email Address:")
	password = getpass.getpass()
	if(arguments["send"]):
		s = SendEmail(username,password,arguments['address'],arguments['subject'],arguments['content'])
		s.send_email()


if __name__ == "__main__":
   main(sys.argv[1:])