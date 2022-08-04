#!/usr/bin/python

import paramiko

# Our VM's information
host = "129.114.25.206" # Public key
username = "cc"
password = "csgroup3"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)

stdin, stdout, stderr = client.exec_command("./run_spark.sh")
print(stdout.read().decode())

stdin.close()
client.close()
