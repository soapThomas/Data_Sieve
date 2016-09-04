import os,sys
import re

FILE_NAME = sys.argv[1]
PAT_REC = sys.argv[2]
pat = '^UniProtKB.*\t' + str(PAT_REC) + '\t.*UniProt\t\t'
pattern = re.compile(pat)

def read_file():
	i = 0
	fr = open(FILE_NAME,"r")
	for line in fr:
		line = line.strip('\n')
		i = i + 1
		match = pattern.match(line)
		if match:
			print(line)
		if i == 30:
			break
		
if __name__ == "__main__":
	read_file()
			 