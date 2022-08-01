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
vm.connect('192.168.115.103', username='osmanl', password='xxxxxx')
#
vmtransport = vm.get_transport()
dest_addr = ('10.103.53.26', 22) #edited#
local_addr = ('192.168.115.103', 22) #edited#
vmchannel = vmtransport.open_channel("direct-tcpip", dest_addr, local_addr)
#
stdin, stdout, stderr = jhost.exec_command("show version | no-more") #edited#
#
print stdout.read() #edited#
#
jhost.close()
vm.close()
# End
