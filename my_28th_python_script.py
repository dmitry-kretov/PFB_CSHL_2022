#! /usr/bin/env/ python3

import re

with open("Python_07.fasta","r") as Python7:
	for line in Python7:
		line = line.rstrip()
		found = re.search(r"^>(\w+)", line) # i am searching only in a line, not in the entire files
		if found:
			print(line)
