
import sys; print(sys.version) 	#display python version in use on launch
import hashlib, binascii, os	#hashlib for secure hashing, binascii for hash encoding os urandom function for 				creating a random number of size n bytes
import pyfirmata
#board = Arduino('/dev/tty0') # change to name of in use serial port
#board.digital[15].write(1) #Test line to turn on an LED if this program is interfacing with device

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
			if (username not in credentials and hpassword not in passwords):
				print("Username and password combination not found, closing...")


def hashpassword(password):
	#function for creating the password hash
	salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
	hpassword = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
	hpassword = binascii.hexlify(password)
	return (salt + hpassword).decode('ascii')


def main():
	#global username, password
	choice = raw_input('Enter 1 to Sign up, 2 to Login  ')
	choice = int(choice)
	while (choice is not 1 or 2):
		if (choice == 1):
			signup(choice)
		elif (choice == 2):
			login(choice)
		else:
			print("Please choose between options 1 and 2.")
		
main()




