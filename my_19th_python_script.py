#! usr/bin/env python3

#opening a file
with open("Python_06.txt", "r") as Python6_read, open("Python_06_uc.txt", "w") as Python6_write:
	for line in Python6_read:
		line = line.rstrip()
		line = line.upper()
		print(line)
	
		
