﻿# -*- coding: utf-8 -*-
# @Date    	: 2016-08-24 08:52:40
# @Author  	: HaoDong

#evi_code_norm.txt是非冗余的从GOA爬出来的数据
#两个dict做search 求这个在55321中的交集
from Bio import SeqIO

#--------------stable---------------------------------
FILE_NAME='evi_code_norm.txt'
#FILE_NAME='..\SplitData\goa_uniport_afterMer_9to16'
#FILE_NAME='..\SplitData\goa_uniprot_afterMer_17to24'
FASTA_FILE_NAME='data_30.fasta'
OUTPUT_FILE_NAME='res_out.txt'
#OUTPUT_FILE_NAME='goa_uniprot_afterMer_1to8_out'
#OUTPUT_FILE_NAME='goa_uniprot_afterMer_9to16_out'
#OUTPUT_FILE_NAME='goa_uniprot_afterMer_17to24_out'
#--------------stable---------------------------------

def get_accession(record):
		parts = record.id.split("|")
		return parts[1]

def calculate():
		protein_infor = {}
		with open(FILE_NAME,"r") as fr:
				lines = fr.readline().strip("\n")
				while lines:
						protein = list(map(str,lines.strip("\n").split("\t")))
						protein_infor[protein[0]] = 0
						lines = fr.readline().strip("\n")
		return protein_infor
		'''with open(OUTPUT_FILE_NAME,"w") as fw:
				for i in protein_infor.keys():
						fw.write(i+'\t'+str(protein_infor[i])+'\n')'''

def search_res(dict_full,dict_sub):
		pro_res = {}
		for i in dict_sub.keys():
				#print("i=",i)
				for j in dict_full.keys():
						if(i == j):
								#print(dict_full[i])
								pro_res[i] = 1
								break;
		return pro_res
	

if __name__ == '__main__':
		obj_id = calculate()
		print('1')
		pro_dict = SeqIO.to_dict(SeqIO.parse(FASTA_FILE_NAME, "fasta"), key_function=get_accession)
		'''print(pro_dict['Q6GZX4'])
		print(pro_dict['Q197F8'])
		print(pro_dict['Q197F7'])
		Q197F7'''
		print('2')
		pro_dict = search_res(obj_id,pro_dict)
		print('3')
		with open(OUTPUT_FILE_NAME,"w") as fw:
				for i in pro_dict.keys():
						fw.write(i+'\n')



'''def calculate():
		protein_infor = {}
		with open(FILE_NAME,"r") as fr:
				lines = fr.readline().strip("\n")
				while lines:
						protein = list(map(str,lines.strip("\n").split("\t")))
						protein_id = protein[0]
						#go_id = protein[1]
						print(protein)
						#print(go_id)
						if (protein_id in protein_infor):
								protein_infor[protein_id] += 1
						else:
								protein_infor[protein_id] = 1
						#protein_infor[protein_id] += 1
						lines = fr.readline().strip("\n")
						
		with open(OUTPUT_FILE_NAME,"w") as fw:
				for i in protein_infor.keys():
						fw.write(i+'\t'+str(protein_infor[i])+'\n')'''				