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
for site in re.finditer(r"([AG])(AATT)([CT])", seq[gene_id]):
	#if found in seq:
	#print(found)
	#print("Total number of sites :", (len(found)))
	#print("site; ", site.group(2))
	#print("upstream of the site: ", site.group(1))
	#print("downsream of the site: ", site.group(3))
	whole = site.group(0)
	print("entire site: ", whole)
	repl = re.sub(r"([AG])(AATT)([CT])", r"\1^\2\3", seq[gene_id]) # this substitutes patterm to another thing
	print (repl)
	fragments = repl.split('^')
	print (fragments)
	print(sorted(fragments, key=len, reverse=False))
	#print(f" This is the cut region {upstream}{site}{downstream}")

