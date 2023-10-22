#!/usr/bin/env python

#NOTE: I will try to make this more interactive so thatyou can input the port number for each given connection. For now, anyway, you do have to edit the script to get it to work 
#Once the specific info in the script is edited, it will work ... I will create an input feature so that the user can include his or her port, IP, username, password ... for each and every attempt 
#Ideally, the system admin or network engineer is always using the same system for repeated ssh connections - however in the case where multiple systems are used, all of which require 
#Unique informaiton - it's cool to have something that's more robust ... 

import maskpass
import os 

# Get the password from the user
inputpasswd = maskpass.askpass(mask="#") #Mask the input with maskpass - gotta love this darn library. It's great! 

# Define other variables
host = "192.168.0.1" #Insert your IP here 
username = "username" #Include unique username 
port = 22 #This is the default SSH port but feel free to enhance your security by picking something less obvious... I recommend something over say 500

# Create the sshpass command with the password included
command = f'sshpass -p "{inputpasswd}" ssh {username}@{host} -p {port}' 

# Execute the command
os.system(command)
