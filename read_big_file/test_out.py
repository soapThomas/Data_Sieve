import os,sys
import re

FILE_NAME = sys.argv[1]

def read_file():
	i = 0
	fr = open(FILE_NAME,"r")
	for line in fr:
		line = line.strip('\n')
		i = i + 1
		print ('%r' % line)
		if i == 5:
			break
		
if __name__ == "__main__":
	read_file()
			 