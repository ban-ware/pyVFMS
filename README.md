# pyVFMS
Project for CY520 @ SEMO University

Must have pyFirmata installed in order to interface with arduino device (NodeMCU ESP8266 in this case however)

# Notes on planned changes:

   	Implement subprocess routine to read output of ls-al | grep (desired filename) to  check ability for
  	user to open a file on device.  Allow user to input filename with extension.  From there, it will be
  	necessary to implement the website.  Console prompts will need to be changed to html buttons, and buttons will
  	need to be added to control each light.  When a light is chosen by a user, it should check the privilege
  	of the user before running the digitalwrite command.  If the privilege does not match, nothing should happen.
  	A root account should be created with access to all 3 with a complicated password.  
  	
  	As far as actual virtual file management, multiple pages should be created.  1 for login, 1 for light controls,
  	1 for file management.  The login system is complete, it just needs porting.  The lights system works through a hacked
  	Firmata running on arduino IDE.  This has been hacked around to allow support for the NodeMCU ESP8266
  	The next hurdle will be file management.  This will encompass much of what is already implemented in the login system. 
  	
  	The final hurdle, and the easiest, will be finding out how to host the websites as well as run the firmata process.
  	We may have to move hosting onto the VM, assuming it fits within the scope of the project.  I do not see
  	a way to run both processes at the same time, as the serial port can only be bound to one program.
  	I have a solution in mind but it may be hacky.  We could move the code for the server into firmata 
  	and execute it as a function, or possibly run firmata through wifi using the firmataWifi example code.
