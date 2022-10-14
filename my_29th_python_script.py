#! /usr/bin/env python3

import re

 # try to use sub patterns
with open("Python_07.fasta","r") as Python7:
	for line in Python7:
		line = line.rstrip()
		found = re.search(r"^>(\S+)\s(.+)", line) # only first space is important to separate idetifier from description. () identify sub-patterns. So, I am looking for the pattern that is - (one or more     non-space-character), one space, at least one any character or more.  
		if found: #you need to dcriminate if line is a header that is mathicng or not. And if not it should skip it or do sometig else
			ID = found.group(1)
			description = found.group(2)
			print("id :", ID)
			print("desc: ", description)
		else:
			print(line)
