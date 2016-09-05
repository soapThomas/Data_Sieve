# -*- coding: utf-8 -*-
# @Date    	: 2016-07-06 08:52:40
# @Author  	: HaoDong

#从10.norm.norm_id.txt里面得到25924条序列，查看有多少条(5539)存在于data_30.fasta
from Bio import SeqIO

#--------------stable---------------------------------
FILE_NAME='norm_id.txt'
#FILE_NAME='..\SplitData\goa_uniport_afterMer_9to16'
#FILE_NAME='..\SplitData\goa_uniprot_afterMer_17to24'
FASTA_FILE_NAME='data_30.fasta'
OUTPUT_FILE_NAME='temp.out'
#OUTPUT_FILE_NAME='goa_uniprot_afterMer_1to8_out'
#OUTPUT_FILE_NAME='goa_uniprot_afterMer_9to16_out'
#OUTPUT_FILE_NAME='goa_uniprot_afterMer_17to24_out'
#--------------stable---------------------------------

def get_accession(record):
		parts = record.id.split("|")
		return parts[1]

def cal(dict_full):
		protein_infor = []
		with open(FILE_NAME,"r") as fr:
				lines = fr.readline().strip("\n")
				while lines:
						if lines in dict_full.keys():
								protein_infor.append(lines)
						lines = fr.readline().strip("\n")
		
		with open(OUTPUT_FILE_NAME,"w") as fw:
				for i in protein_infor:
						fw.write(i+'\n')


if __name__ == '__main__':
		pro_dict = SeqIO.to_dict(SeqIO.parse(FASTA_FILE_NAME, "fasta"), key_function=get_accession)
		cal(pro_dict)				