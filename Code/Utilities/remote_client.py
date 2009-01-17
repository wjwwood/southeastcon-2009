#
#  remote_client.py
#  
#
#  Created by William Woodall on 1/14/09.
#  Copyright (c) 2009 Auburn University. All rights reserved.
#

from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep, gmtime, strftime
import pygame
import pygame.event

SERVER_IP = '192.168.1.101'
PORT_NUMBER = 5000
SENSITIVITY = .1
DEAD_ZONE = .2
THROTTLE = 0

soc = socket( AF_INET, SOCK_DGRAM )

pygame.joystick.init()
pygame.display.init()
joy = pygame.joystick.Joystick(0)
joy.init()

def loop():
	speed = 0.0
	direction = 0.0
	e = None
	while True:
		try:
			e = pygame.event.wait()
			if e.axis == 1 and abs(speed - e.dict['value']) > SENSITIVITY:
				speed = e.dict['value']
			elif e.axis == 0 and abs(direction - e.dict['value']) > SENSITIVITY:
				direction = e.dict['value']
			elif e.axis == 1 or e.axis == 0:
				if abs(speed) < DEAD_ZONE:
					speed = 0
				if abs(direction) < DEAD_ZONE:
					direction = 0
				move = str(speed)+" "+str(direction)
				print move
				soc.sendto(move, (SERVER_IP, PORT_NUMBER))
				sleep(THROTTLE)
		except AttributeError:
			pass

try:
	loop()
except KeyboardInterrupt:
	print "\nShutting down."
finally:
	soc.close()