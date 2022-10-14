i#! usr/bin/env python3

with open ("Python_06.fastq","r") as Seq:
		num_lines = sum(1 for line in Seq if line.rstrip())
    num_car = len((line) for line in Seq if line.rstrip())
		print("Total lines:", num_lines)
		print("Car per line:", num_car)




	
