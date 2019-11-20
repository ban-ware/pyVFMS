# pyVFMS
Project for CY520 @ SEMO University

Html is displayed by using a header file that is included in the main arduino code.

Due to being flash memory only, the files in data must be flashed in their desired state.  Any alteration after flashing won't be possible.

To hold the value of the currently logged in username, it is sent to a textfile, as it is the only possible way without pure C/C++ libraries being usable.

To use:
  Launch login.py using "python login.py"
  enter 2
  login with any of the credentials in credentials.txt
  passwords are hashed and placed in passwords.txt, but they are simply the username of the relevant user
  while logged in, flash files to esp8266 memory
  upload arduino WiFiAP program after flashing is complete
  connect to 192.168.4.1 or enter 2 on the login program
  Click buttons to interact with lights assigned to currently logged in user
  Go to 192.168.4.1/bignum to view big number calculator #TODO
  Logout of python program with 3 and demonstrate the uselessness of flash memory as you 
  continually control lights under false pretenses.
  
  
