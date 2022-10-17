 #! /usr/bin/env python3

import Bio
import Bio.Seq
from Bio.Seq import Seq
from Bio import SeqIO
id_dict = SeqIO.to_dict(SeqIO.parse("Python_08.fasta", "fasta"))
#for seq_record in id_dict:
print(id_dict)



