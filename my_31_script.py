#! /usr/bin/env python3 

import re

genes={}
gene_id = ''
with open("Python_07.fasta", "r") as seq_read:
	for line in seq_read:
		line = line.rstrip()
		found = re.search(r"^>(\w+)", line) # i am searching only in a line, not in the entire files
		if found:
			gene_id = line
			genes[gene_id]=''
		else:
			sequence = line
			genes[gene_id]+=sequence
print(genes)
 
