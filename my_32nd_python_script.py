#! /usr/bin/env python3


import Bio
print(Bio.__version__)
from Bio import SeqIO
#seq_count = 0
#nt_count = 0
for seq_record in SeqIO.parse("Python_08.fasta", "fasta"):
	seqobj =seq_record.Seq()
	print(seqobj)
	#print(type(seq_record))
	#print('ID', seq_record.id)
	#print('Sequence', seq_record.seq)
	#print('Protein', seq_record.seq.translate(to_stop=False))
	#print('Length', len(seq_record))
#seq_dict = SeqIO.to_dict(SeqIO.parse("Python_08.fasta", "fasta"))
#	for sequence in seq_record:
#		count +=1
#print("Total number of nt: ",count)		
#convert fasta to dict
#print(id_dict)

