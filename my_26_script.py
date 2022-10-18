#! /usr/bin/env python3

#import regular expression
import re

with open ("Python_07_nobody.txt", "r") as Python7:
	for line in Python7:
		line = line.rstrip()
		# if you are expecting a single occurence of thing that you are searhing for use re.search if you expect multile occurence use re.findall
		found = re.findall(r"Nobody", line) #reguar expressions working on a string not on a file! Always indicate here a string - in this situation this is a line. 
		print(found)

