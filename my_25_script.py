#! usr/bin/env python3


al_genes = []
cancer_genes = []
pigment_genes = []
with open("alpaca_all_genes.tsv","r") as alpaca_genes, open("alpaca_stemcellproliferation_genes.tsv","r") as Cancer_genes, open("alpaca_pigmentation_genes.tsv", "r") as Pigm_genes:
	for line in alpaca_genes:
		line = line.rstrip()
		al_genes.append(line) 
	for line in Cancer_genes:
		line = line.rstrip()
		cancer_genes.append(line)		
	for line in Pigm_genes:
		line = line.rstrip()
		pigment_genes.append(line)
AL_GENES = set(al_genes)
CANCER_GENES = set(cancer_genes)
PIGM_GENES = set(pigment_genes)
print(AL_GENES)
print(CANCER_GENES)
print(PIGM_GENES)
non_cancer_genes = AL_GENES - CANCER_GENES
print("These are non cancer genes: ",non_cancer_genes)
prol_pigm = CANCER_GENES & PIGM_GENES
print("These are cell prolif and pigmentation genes: ", prol_pigm)

