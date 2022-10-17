#! /usr/bin/env/ python3

import re
seq ={}
gene_id=''
with open("Python_07_ApoI.fasta","r") as ApoI:
	for line in ApoI:
		line = line.rstrip()
		if '>'in line:
			gene_id = line
			seq[gene_id]=''
		else:
			sequence = line
			seq[gene_id]+=sequence
print(seq)
for gene_id in seq:
	found = re.findall(r"(.{10})([AG]AATT[CT])(.{10})", seq[gene_id])# idicate that the search needs to be done in values, not in the entire document # if you use #findall you find all the potential matches and they will be printed
	if found:
		print(found)
		print("Total number of sites :",(len(found)))
	#site = found.group(2)
	#print("cut site: ", found.group(2))
	#upstream = found.group(1)
	#print("upstream of the site: ", upstream)
	#downstream = found.group(3)
	#print("downsream of the site: ", downstream)
	#print(f" This is the cut region {upstream}{site}{downstream}")

