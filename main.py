#!/usr/bin/python

import paramiko
import sys

# Our VM's information
host = "129.114.25.206" # Public key
username = "cc"
password = " "

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command("bin/spark-submit --master spark://group3-1:7077 /home/cc/spotifyProject.py")
print(stdout.read().decode())
client.close()




