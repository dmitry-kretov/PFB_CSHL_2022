#1 usr/bin/env python3

dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

lengths = [ (len(dna),dna) for dna in dna_list]
print(lengths)
for tup in lengths:
	print(tup[0],tup[1], sep = '\t')
