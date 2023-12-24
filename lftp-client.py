#!/usr/bin/env python3
#This is a very simple lftp client. I will edit this more later 
import ftplib 
import os 
import time
import subprocess

hostname = "x.x.x.x"
username = "pass"
password = "pass"
local_dir = "/home/user/dir/subdir"

with ftplib.FTP(host=hostname, user=username, passwd=password) as ftp: 
    status = ftp.getwelcome() 
    print(f'Connection status: {status}') 


subprocess.run([
    'lftp', '-u', f'{username},{password}', hostname])

