#!/usr/bin/env python3

my_seq = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if 'ATG' in my_seq:
	print('there is a start codon')
else:
	print('there is no start codon')  
if 'TTT' in my_seq:
	print('but there is a TTT')
else:
	print('there is not even TTT')
