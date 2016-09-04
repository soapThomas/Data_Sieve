import os,sys
import re

FILE_NAME = sys.argv[1]
pattern = re.compile(r'^UniProtKB.*\tEXP\t')

def read_file():
	i = 0
	fr = open(FILE_NAME,"r")
	for line in fr:
		#line = line.strip('\n')
		i = i + 1
		match = pattern.match(line)
		if match:
			print(line)
		
if __name__ == "__main__":
	read_file()
			 