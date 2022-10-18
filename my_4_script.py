#!/usr/bin/env python3

import sys

my_num = int(sys.argv[1])
if my_num > 0:
	if my_num < 50:
		if my_num % 2 == 0:
			message = "it is positive, lower then 50 and even"
			print (my_num, message)
		else:
			message = "it is positive, lower then 50 and odd"
			print (my_num, message)
	elif my_num == 50:
		message = "it is 50!"
		print (my_num, message)
	else:
		if my_num%3 ==0:
			message = "it is positive and  greater than 50 and divisible by 3"
			print (my_num, message)
		else:
			message = "it is positive and either equal or greater than 50 and non-divisible by 3"
			print (my_num, message)
elif my_num <0 :
	message = "negative"
	print (my_num, message)
else:
	message = ("it is 0")
	print (my_num, message)

