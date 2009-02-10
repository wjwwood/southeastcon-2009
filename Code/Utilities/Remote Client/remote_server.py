#
#  remote_server.py
#  
#
#  Created by William Woodall on 1/14/09.
#  Copyright (c) 2009 Auburn University. All rights reserved.
#
import os
os.chdir('../../')
import sys
sys.path.append('./')

from robot import *

from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM

PORT_NUMBER = 5000
SENSITIVITY = .2

hostName = ''

soc = socket(AF_INET, SOCK_DGRAM)
soc.bind( (hostName, PORT_NUMBER) )

info("Server started on port: %i" % PORT_NUMBER)

# Loop
def loop():
	arm = None
	sorter = None
	gripper = None
	while True:
		(data, addr) = soc.recvfrom( 1024 )
		debug("Recieved Pack from %s: %s" % (addr, data))
		p = data.partition(' ')
		speed = float(p[0])
		p = p[2].partition(' ')
		direction = float(p[0])
		
		p = p[2].partition(' ')
		if abs(arm - float(p[0])) > SENSITIVITY:
			arm_bool = True
			arm = float(p[0])
		
		p = p[2].partition(' ')
		if abs(sorter - float(p[0])) > SENSITIVITY:
			sorter_bool = True
			sorter = float(p[0])
		
		p = p[2].partition(' ')
		if abs(gripper - float(p[0])) > SENSITIVITY:
			gripper_bool = True
			gripper = float(p[0])
		
		move(speed, direction)
		if arm_bool:
			arm_servo.move(arm)
			arm_bool = False
		if sorter_bool:
			sorter_servo.move(sorter)
			sorter_bool = False
		if gripper_bool:
			gripper_servo.move(gripper)
			gripper_bool = False
		
try:
	loop()
except KeyboardInterrupt:
	print
	info("Shutting Down.")
finally:
	shutdown()
	soc.close()
