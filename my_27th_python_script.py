 #! /usr/bin/env python3
 
import re

with open ("Python_07_nobody.txt", "r") as Python7, open("Isha.txt", "w") as Python7_write:
	for line in Python7:
		line = line.rstrip()
		new_line = line.replace("Nobody", "Isha")#replace every single occurence of Nobody
		print(new_line)
		Python7_write.write(line+"\n")
