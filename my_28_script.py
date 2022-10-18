#! /usr/bin/env/ python3

import re

with open("Python_07.fasta","r") as Python7:
	for line in Python7:
		line = line.rstrip()
		found = re.search(r"^>(\w+)", line) # i am searching only in a line, not in the entire files
		if found:
			print(line)
			print(found)
# try to use sub patterns
with open("Python_07.fasta","r") as Python7:
	for line in Python7:
  	line = line.rstrip()
  	found = re.search(r"(\S+)\s(.s)", line) # only first space is important to separate idetifier from description. () identify sub-patterns. So, I am looking for the pattern that is - (one or more non-space-character), one space, at least one any character or more.  
		ID = found.group(1)
		description = found.group(2)
		print("id :", ID)
		print("desc: ",dscription)
