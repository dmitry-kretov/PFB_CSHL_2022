#! usr/bin/env python3

#download file straight from git hub
# curl -0 https://raw.githubusercontent.com/prog4biol/pfb2022/master/files/Python_07.fasta
genes={}
gene_id = ''
with open("Python_07.fasta", "r") as seq_read:
	for line in seq_read:
		line = line.rstrip()
		if '>' in line: 
			gene_id = line
			genes[gene_id]=''
		else: 
			sequence = line
			genes[gene_id]+=sequence
print(genes)

