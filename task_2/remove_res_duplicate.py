# coding = gbk
# author : Hao Dong
# time: 2016-8-24 20:51
# 给每个GO的功能去重 开始求fsim

import os,sys
import pandas as pd

#--------------stable---------------------------------
FILE_NAME = sys.argv[1]
#suffix = '.set'
col_names = ['DB','DB_ID','DB_SYM','QUA','GO_ID','DB_REF','EVI_CODE','WITH_FROM',
				 'ASP','DB_NAME','DB_SYN','DB_TYPE','TAXON','DATE','ASS','ANE','GENE_PRO']
				 
#--------------stable---------------------------------

def processFile():
		NAME = "norm_id.txt"
		data = pd.read_table(FILE_NAME,names = col_names)	
		data = data.drop_duplicates('DB_ID')
		data.to_csv(NAME, index = False, header = False, sep = "\t", columns = ['DB_ID'])		
			
						
if __name__ == '__main__':
		processFile()

