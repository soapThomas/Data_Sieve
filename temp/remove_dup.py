# coding = gbk
# author : Hao Dong
# time: 2016-8-23 20:51
# 给seq_GO_5234.out去重

import pandas as pd

#--------------stable---------------------------------
FILE_NAME = 'res_bp.txt'
#--------------stable---------------------------------

def processFile(FILE_NAME):
		data = pd.read_table(FILE_NAME)
		print (len(data.index))
		i = 0
		while i < 5:
			print (data.iloc[i].values)
			data_series = data.iloc[i]
			print (data_series.values)
			data_series_2 = data_series.drop_duplicates()
			print (data_series_2.values)
			data.iloc[i] = data_series
			#print (data.iloc[i])
			i = i + 1
		#data.to_csv('sorted' + FILE_NAME,sep = '\t', index = False, header = False)
		
						
if __name__ == '__main__':
		processFile('res_bp.txt')
		processFile('res_bp.txt')
		processFile('res_bp.txt')

