
import sys; print(sys.version) 	#display python version in use on launch
import hashlib, binascii, os	#hashlib for secure hashing, binascii for hash encoding os urandom function for 				creating a random number of size n bytes
import pyfirmata
import getpass # to get information on currently logged in user on linux machine
import subprocess

#	pinout guide:
#	NodeMCU pin:	Arduino Pin: (Write to arduino pin)
#		4		2	red
#		6		12	green
#		7		13	blue
		
board = pyfirmata.Arduino('/dev/ttyUSB0')
#board.digital[2].write(1)   For testing purposes
#board.digital[12].write(1)
#board.digital[13].write(1)

def signup(choice):
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
	print("New credentials created")

def login(choice):
	username = raw_input("Enter a username:  ")
	password = raw_input ("Enter a password:  ")

	hpassword = (hashlib.sha512(password).hexdigest())
	
	fd = open("credentials.txt", "r")
	credentials = fd.read()
	
	fp = open("passwords.txt", "r")
	passwords = fp.read()

	if (username in credentials):
		#print("Username in file")
		if(hpassword in passwords):
			#print("Your password is in the file")
			print("You are now logged into the system")
			return (logged_in = 1)
			if (username not in credentials and hpassword not in passwords):
				print("Username and password combination not found, closing...")
				return(logged_in = 0)
def usercheck(logged_in):
	if (logged_in = 1):
		fd = open("credentials.txt", "r")
		credentials = fd.read()
		ux_username = getpass.getuser()
		if (ux_username not in credentials):
			print("Current user not authorized to access files on this account.")
			exit()
		elif(ux_username in credentials):
			print("Current user is authorized to access files on this account.")

def hashpassword(password):
	#function for creating the password hash
	salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
	hpassword = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
	hpassword = binascii.hexlify(password)
	return (salt + hpassword).decode('ascii')


def main():
	#global username, password
	logged_in = 0
	choice = raw_input('Enter 1 to Sign up, 2 to Login  ')
	choice = int(choice)
	
	if (choice == 1):
		signup(choice)
	while (logged_in is not 1):
		if (choice == 2):
			login(choice)
		else:
			print("Please choose between options 1 and 2.")
	
	
		
main()




