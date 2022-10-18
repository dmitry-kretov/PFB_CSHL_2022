#! usr/bin/env python3

with open("alpaca_all_genes.tsv","r") as alpaca_genes:
	for line in alpaca_genes:
		line = line.rstrip()
		print(line)
setA = set(alpaca_genes)
print(setA)

with open("alpaca_stemcellproliferation_genes.tsv", "r") as alpaca_cancer_genes
with open("alpaca_pigmentation_genes.tsv", "r") as alpaca_pigmentation_genes

setA =set(alpaca_genes)
setB =set(alpaca_cancer_genes)
setC =set(alpaca_pigmentation_genes)

print(setA)
print(setB)
print(setC)


