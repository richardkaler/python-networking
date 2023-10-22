#!/usr/bin/env python

import paramiko
import maskpass
import time

ipinput = input("Enter the IP address for the host: ")
userinput = input("Enter the user name for SSH connection: ")

# Prompt for the password securely using maskpass
inputpasswd = maskpass.askpass(mask="#")

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
