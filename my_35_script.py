#! /usr/bin/env python3



seqs = {}
gene_id = ''
with open ("python_08.fasta") as my_file:
		for line in my_file:
				line = line.rstrip()	
				if ">" in line:
						gene_id = line
						seqs[gene_id]={} #here we create a new empty dictinary that corresponds to the keys of gene_id
				else:
						for nt in line:
								if nt in seqs[gene_id]: # nt is a value.
										seqs[gene_id][nt]+=1 # if nt is already in the dictonaty add 1 to the values
								else:
										seqs[gene_id][nt]=1; # if it is not in there add new and assign values 1
print (seqs)

