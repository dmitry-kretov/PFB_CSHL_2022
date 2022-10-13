#!/usr/bin/env python3


DNA = "ATGCAGGGGAAACATGATTCAGGAC"
reverse = DNA[::-1]
print(DNA)
print(DNA.replace('A','%temp%').replace('T','A').replace('%temp%','T'))
print(DNA.replace('G','%temp%').replace('C','G').replace('%temp%','C'))

print(f'Original sequence 5\' {DNA} 3\'')

DNA = "ATGCAGGGGAAACATGATTCAGGAC"
reverse = DNA[::-1]
print(DNA)
complement = (DNA.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper())i
print(complement)
print(DNA.replace('G','c').replace('C','g'))






