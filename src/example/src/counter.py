#! /usr/bin/env python3
from time import sleep

n = 9
while n>-1 :
	if n == 0:
		sleep(1)
		print("Time up!!!!!!!!!!!!!!!!")
		n -= 1;	
	elif n > 0:	
		sleep(1)
		print(n)
		n -= 1;
