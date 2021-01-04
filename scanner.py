#!/bin/python3

import sys
import socket
from datetime import datetime

# validating the length of the arguments
if len(sys.argv) != 4:
	print('Invalid amount of arguments.')
	print('Syntax: ./scanner.py <ip> <starting port> <ending port>')
	sys.exit()

# creating constants
MIN_PORT = 1
MAX_PORT = 65534

try:
	TARGET = socket.gethostbyname(sys.argv[1]) # getting the ip address
except Exception as e:
	print(e)
	sys.exit()
	
STARTING_PORT = int(sys.argv[2]) # getting the starting port
ENDING_PORT = int(sys.argv[3]) # getting the ending port

# storing ports
PRESENT_PORTS = []

# validating port range
if((STARTING_PORT >= MIN_PORT and STARTING_PORT <= MAX_PORT) and (ENDING_PORT >= MIN_PORT and ENDING_PORT <= MAX_PORT)):
	try:
		# creating a banner
		print('#' * 50)
		print(f'Scanning Target {socket.gethostbyname(sys.argv[1])}')
		print(f'Time started: {str(datetime.now())[0: 10]}') # there might be a better way of subscripting
		print('#' * 50)

		# trying to make a conncection on each port
		for port in range(STARTING_PORT, ENDING_PORT + 1):
			# creating socket object
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# if there is no connection estabilished, then move on and do not try to reconnect
			socket.setdefaulttimeout(1)
			# checking the response
			response = s.connect_ex((TARGET, port))
			if response == 0:
				print(f'Port {port} is open.')
				PRESENT_PORTS.append(port)
			
			# closing the connection
			s.close()
		
		# if no ports were present
		if(len(PRESENT_PORTS) == 0):
			print('No ports were open.')
	except KeyboardInterrupt:
		print('\nexiting')
		sys.exit()
else:
	print('Please check the port range specified')
	print('Valid range {1..65534}')
	sys.exit()
