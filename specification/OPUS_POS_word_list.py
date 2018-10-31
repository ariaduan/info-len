file1 = open('../corpora_and_texts_obtained/OPUS_POS','rb')
fileout1 = open('../corpora_and_texts_obtained/OPUS_POS_word_list','w',encoding = 'utf-8')




line = file1.readline().decode('utf-8').split()
for i in line:
	i = i.split('_')
	fileout1.write(i[0] + '\t' + i[1] + '\n')

file1.close()
fileout1.close()
