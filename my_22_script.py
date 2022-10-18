#! usr/bin/env python3

#you can open a file with this function
#curl-o https://raw.githubusercontent.com/prog4biol/pfb2022/master/files/Python_06.fastq
#define two counting parameters
total_characters = 0
total_lines = 0
with open ("Python_06.fastq","r") as Seq:
	for line in Seq:
		line = line.rstrip()
		total_lines +=1
		line_length = len(line)
		total_characters += line_length
print("Total characters:", total_characters)
print("Total lines:", total_lines)
print(total_characters/total_lines)

