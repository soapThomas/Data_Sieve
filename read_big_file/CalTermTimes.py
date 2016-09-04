# -*- coding: utf-8 -*-
# @Date    	: 2016-07-06 08:52:40
# @Author  	: HaoDong
#失败版本
from Bio import SeqIO

#--------------stable---------------------------------
FILE_NAME='..\SplitData\goa_uniprot_afterMer_1to8'
#FILE_NAME='..\SplitData\goa_uniport_afterMer_9to16'
#FILE_NAME='..\SplitData\goa_uniprot_afterMer_17to24'
#FILE_NAME='test.txt'
FASTA_FILE_NAME='data_30.fasta'
#OUTPUT_FILE_NAME='test_out_put.txt'
#OUTPUT_FILE_NAME='goa_uniprot_afterMer_1to8_out'
#OUTPUT_FILE_NAME='goa_uniprot_afterMer_9to16_out'
#OUTPUT_FILE_NAME='goa_uniprot_afterMer_17to24_out'
OUTPUT_FILE_NAME='fasta_out'
#--------------stable---------------------------------
def calculate():
		protein_infor = {}
		with open(FILE_NAME,"r") as fr:
				lines = fr.readline().strip("\n")
				while lines:
						protein = list(map(str,lines.strip("\n").split("\t")))
						protein_id = protein[0]
						#go_id = protein[1]
						#print(protein)
						#print(go_id)
						if (protein_id in protein_infor):
								protein_infor[protein_id] += 1
						else:
								protein_infor[protein_id] = 1
						#protein_infor[protein_id] += 1
						lines = fr.readline().strip("\n")
						
		with open(OUTPUT_FILE_NAME,"w") as fw:
				for i in protein_infor.keys():
						fw.write(i+'\t'+str(protein_infor[i])+'\n')

def get_accession(record):
		parts = record.id.split("|")
		return parts[1]
		
if __name__ == '__main__':
		calculate()		
		pro_dict = SeqIO.to_dict(SeqIO.parse(FASTA_FILE_NAME, "fasta"), key_function=get_accession)						
		with open(OUTPUT_FILE_NAME,"w") as fw:
				for i in pro_dict.keys():
						fw.write(i+'\n')