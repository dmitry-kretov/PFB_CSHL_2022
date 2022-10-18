#! usr/bin/env python3

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
seq_iterator = iter(seqs)
for seq in seq_iterator:
	print(len(seq),seq,sep='\t')
