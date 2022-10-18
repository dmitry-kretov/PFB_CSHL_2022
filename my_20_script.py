#! usr/bin/env python3

genes={}
with open("Python_06.seq.txt") as my_file_06:
	for line in my_file_06:
		line = line.rstrip()#this removes the space from the end of the line (\n)
		seqName, sequence = line.split('\t')#this splits line based on the tabi
		complement = (sequence.replace('A','t').replace('T','a').replace('G','c').replace('C','g'))
		rev_com = complement[::-1]
		genes[seqName] = rev_com
print(genes)
for seqName in genes:
	print(">"+seqName+" rev-com")
	print(genes[seqName])
