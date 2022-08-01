#!/usr/bin/python
#
# Paramiko
#
import paramiko
import sys
import subprocess
#
# we instantiate a new object referencing paramiko's SSHClient class
#
vm = paramiko.SSHClient()
vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
vm.connect('10.56.3.182', username='cs4843', password='')
#
vmtransport = vm.get_transport()
dest_addr = ('10.103.53.26', 22) #edited#
local_addr = ('10.56.3.182', 22) #edited#
vmchannel = vmtransport.open_channel("direct-tcpip", dest_addr, local_addr)
#
stdin, stdout, stderr = jhost.exec_command("bin/spark-submit --master spark://group3-1:7077 /home/cc/spotifyProject.py") #edited#
#
print stdout.read() #edited#
#
jhost.close()
vm.close()
# End
