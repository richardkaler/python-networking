#!/usr/bin/env python

#NOTE: I will try to make this more interactive so thatyou can input the port number for each given connection. For now, anyway, you do have to edit the script to get it to work 
#Once the specific info in the script is edited, it will work ... I will create an input feature so that the user can include his or her port, IP, username, password ... for each and every attempt 
#Ideally, the system admin or network engineer is always using the same system for repeated ssh connections - however in the case where multiple systems are used, all of which require 
#Unique informaiton - it's cool to have something that's more robust ... 

import maskpass
import os 

# Get the password from the user
inputpasswd = maskpass.askpass(mask="#")

# Define other variables
host = "192.168.1.15"
username = "MegaForce"
port = 700

# Create the sshpass command with the password included
command = f'sshpass -p "{inputpasswd}" ssh {username}@{host} -p {port}'

# Execute the command
os.system(command)
