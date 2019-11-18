#Changelog:
#	moved signup and login to separate functions to help readability. 
#	After user completes signup they are asked to then login using their credentials
#	Once they enter their credentials, they are then logged in.  
#	Need to add method to hold the name of the current user (easy)
#	Need to add to current file connection to take current_user and their password. (easy-ish)
#	Need to add method to redirect the currently logged in user to the esp8266 server to control the light (medium)
#	Must make web pages (html & css) (easy, all it should do is open a website and control the light, a template website with our 	 #	group name and fancy css will do fine.

import sys; print(sys.version) 	#display python version in use on launch
import hashlib, binascii, os	#hashlib for secure hashing, binascii for hash encoding os urandom function for creating a random number of size n bytes
#import pyfirmata #use if you want to run commands to ESP8266
import webbrowser
import subprocess

login_status = 0

hostname = "banware-vm"


#	pinout guide:
#	NodeMCU pin:	Arduino Pin: (Write to arduino pin)
#		4		2	red
#		6		12	green
#		7		13	blue
		
#Commented code below this line is not useful anymore, but stands as a useful reference
#board = pyfirmata.Arduino('/dev/ttyUSB0')  #Uncomment to use esp board
#board.digital[2].write(1)   For testing purposes
#board.digital[12].write(1)
#board.digital[13].write(1)

#Login function:
#	Usage:
#	User enters their username and password.  username is plaintext and checked against existing usernames
#	Password is hashed and checked against all password hashes until a match is found.  If no match, we exit.
#	If login is successful, we set the login_status to 1 and return to main
def login():
	print("Please log in: ")
	username = raw_input("Username:  ")
	password = raw_input ("Password:  ")

	hpassword = (hashlib.sha512(password).hexdigest())
	
	fd = open("credentials.txt", "r")
	credentials = fd.read()
	
	fp = open("passwords.txt", "r")
	passwords = fp.read()

	if (username in credentials and hpassword in passwords):
		print("You are now logged into the system")
		#login_status = 1
		global logged_in_user
		logged_in_user = username
		return (logged_in_user)

	elif (username not in credentials or hpassword not in passwords):
		print("Username and password combination not found, closing...")
		exit()
	

#Signup function:
#	Usage: User enters desired username and password, which are storeed in separate files
#	Files are opened for appending and then opened for reading
#	This allows us to check entered credentials against stored credentials
#	password is hashed with SHA256, nothing is done with plaintext password.
#	

def signup():
	#open the credentials file for appending, this allows us to store multiple username and password combos
	fd = open("credentials.txt", "a+")
	username = raw_input("Enter a username:  ")
	credentials = fd.read()

	if(username in credentials):
		print("Username prohibited, please use your own name or ID#"); exit()
	
	fd.write(username); fd.write("\t")
	fd.close()

	fp = open("passwords.txt", "a")
	password = raw_input("Enter a password:  ")
	

	#prohibit users from entering symbols that could be used maliciously
	if(username == {"/",".","!","@","#","%","^","&","*","(",")","|","?",";",":","'"}):
		print("Prohibited Symbol Detected, closing..."); exit()

	hpassword = hashpassword(password)
	fp.write(hashlib.sha512(password).hexdigest()); fp.write("\n")
	fp.close()
	print("New credentials created.")
	login()


#sftpconnect usage:
#	connect to sftp server with currently logged in user
def sftpconnect(logged_in_user, hostname):
	sftpcall = str(logged_in_user + "@"+hostname).strip()
	subprocess.call(["sftp {0}".format(sftpcall)], shell = True)#.format(logged_in_user+"@"+hostname).strip()], shell=True)

def hashpassword(password):
	#function for creating the password hash
	salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
	hpassword = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
	hpassword = binascii.hexlify(password)
	return (salt + hpassword).decode('ascii')


#Main usage:
#	Driver function should take arguments from the user.  The end-all be-all of this function is in the menu.
#	Once the user chooses an option, they do that they want to do, and then they are returned to the menu.
#	Once they are done, they enter 3, and then they leave.

def main():
	
	choice = raw_input('Enter 1 to Sign up, 2 to Login  ')
	choice = int(choice)
	
	
	if (choice == 1):
		signup()

	if (choice == 2):
		login()
		
	print(logged_in_user + "!")	#tester for logged_in_user
	userhold = open("logged_in_user.txt", "w")
	userhold.write(logged_in_user); userhold.write("/t")
	userhold.close()

	while (logged_in_user != ""):
		print ("What would you like to do?")
		print ("1. View your files")
		print ("2. Continue to server")
		print ("3. Log Out")
		choice = int(raw_input())
		
		if(choice == 1): 
			sftpconnect(logged_in_user, hostname)
		elif(choice == 2):#open lightcontrol.py or equivalent
			print("TODO_ADDPAGE")
		elif(choice == 3): 
				login_status= 0
				userhold = open("logged_in_user.txt", "w")
				userhold.close(); exit()
				
		
	return
	
	
		
main()

