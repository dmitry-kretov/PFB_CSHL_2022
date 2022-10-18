#! /usr/bin/env python3
 
import Bio
from Bio import SeqIO
count_lines = 0
Blength = 1000000000000000
Slength =0
count_G=0
count_C=0
count_A=0
count_T=0
filename = "Python_08.fasta"
for seq_record in SeqIO.parse(filename, "fasta"):
		count_lines +=1
		length1 = len(seq_record.seq)
		if length1  < Blength:
			Blength = length1
			Shortest_seq = seq_record
		length2 = len(seq_record.seq)
		if length2 > Slength:
			Slength = length2
			Longest_seq = seq_record
			for nt in seq_record.seq:
				pr_count_G = seq_record.seq.count("G")
				count_G += pr_count_G
				pr_count_C = seq_record.seq.count("C")
				count_C += pr_count_C
				pr_count_A = seq_record.seq.count("A")
				count_A += pr_count_A
				pr_count_T = seq_record.seq.count("T")
				count_T += pr_count_T
print("ID:", Shortest_seq.id, "shortest:",Blength)
print("ID:", Longest_seq.id, "longest:", Slength)
print("Total number of seqeunces: ", count_lines)		
total_nt = count_G+count_C+count_A+count_T
total_GC = count_G+count_C
print("Total number of nucleotiotides: ", total_nt)
average = int(total_nt/count_lines)
average_GC = int((total_GC/total_nt)*100)
print("Average length of sequences: ",average) 
print("Average_GC: ", average_GC)
	
