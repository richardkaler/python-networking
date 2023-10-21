!/usr/bin/env python

#NOTE: The shebang line above is only necessary if you want to run the script without typing "python ssh_input_connect.py" each time you need to run it 
#This script was created as a simple method to connect to a server without manually typing out the ssh syntax for a connection via the traditional method on the command line. 
#I will add another script that connects using ssh keys - and that is the preferred method but this is a convenient choice for those who do not have public key authentication set up yet 

import paramiko
import maskpass
import time

ipinput = input("Enter the IP address for the host: ")
userinput = input("Enter the user name for SSH connection: ")

# Prompt for the password securely using maskpass
inputpasswd = maskpass.askpass(mask="")
print(inputpasswd)
print("Type 'clear' once you enter the ssh session to refresh the terminal\nType ctrl+c to exit the session at any time\nInitiating session now...")
time.sleep(5)

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the remote host with username and password
    client.connect(ipinput, username=userinput, password=inputpasswd)

    # Start an interactive shell
    ssh_session = client.invoke_shell()


    while True:
        # Read data from the shell
        output = ssh_session.recv(1024).decode('utf-8')
        if not output:
            break
        print(output, end='')

        # You can also send data to the shell
        user_input = input()
        ssh_session.send(user_input + '\n')

        if user_input.strip().lower() == 'exit':
            break
finally:
    # Close the SSH connection when done
    client.close()
