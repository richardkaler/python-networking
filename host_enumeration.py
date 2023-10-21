#!/usr/bin/env python

#NOTE: The shebang is only necessary if you are running this on Linux and want to run the script without navigating to the directory it resides in first. For that, you also need to make sure this 
#script is placed into a directory that is in path. 

import logging
import paramiko
from datetime import datetime
import maskpass

ipinput = input("Enter the IP address for the host: ")

userinput = input("Enter the user name for ssh connection: ")

inputpasswd = maskpass.askpass(mask="")
print(inputpasswd)

print("Processing script with credential provided")

host = ipinput
username = userinput
password = inputpasswd
commands = ("uptime -p", "python --version", "uname -a", "netstat -lt | head -45", "ip addr show", "hostname", "groups", "sudo -l")
command_timeout = 15
logfile = "/home/richard/tmp/ssh-target-enum.log"
current_datetime = datetime.now()

# Configure the logging module
logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s - %(message)s')

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the SSH server
client.connect(host, username=username, password=password)

# Open the log file for writing
with open(logfile, 'w') as log_file:
    print("Piping results to " + logfile)
    print("=============================================================================")
    for command in commands:
        stdin, stdout, stderr = client.exec_command(command, timeout=command_timeout)
        log_file.write(f"Command: {command}\n")
        try:
            output = stdout.read().decode()
            log_file.write(output)
            log_file.write("\n")
            print(output)
        except paramiko.ssh_exception.SSHException as e:
            log_file.write(f"Error executing command: {e}\n")
        except Exception as e:
            log_file.write(f"An unexpected error occurred: {e}\n")

# Append the current date and time at the bottom of the log file
log_file = open(logfile, 'a')  # Open the file in append mode
log_file.write("=============================================================================\n")
log_file.write("Finished generating log at: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
log_file.close()
# Close the SSH connection
client.close()


