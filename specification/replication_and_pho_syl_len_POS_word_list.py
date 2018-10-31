file1 = open('../corpora_and_texts_obtained/pho_syl_POS','rb')
file2 = open('../corpora_and_texts_obtained/pho_syl_len_word_list','rb')
fileout1 = open('../corpora_and_texts_obtained/pho_syl_len_POS_word_list','w',encoding = 'utf-8')
file3 = open('../corpora_and_texts_obtained/replication_POS','rb')
fileout2 = open('../corpora_and_texts_obtained/replication_POS_word_list','w',encoding = 'utf-8')
file4 = open('../corpora_and_texts_obtained/replication_POS_50000','rb')
fileout3 = open('../corpora_and_texts_obtained/replication_POS_word_list_50000','w',encoding = 'utf-8')
file5 = open('../corpora_and_texts_obtained/replication_POS_75000','rb')
fileout4 = open('../corpora_and_texts_obtained/replication_POS_word_list_75000','w',encoding = 'utf-8')
file6 = open('../corpora_and_texts_obtained/replication_POS_100000','rb')
fileout5 = open('../corpora_and_texts_obtained/replication_POS_word_list_100000','w',encoding = 'utf-8')
file7 = open('../corpora_and_texts_obtained/OPUS_POS','rb')
fileout6 = open('../corpora_and_texts_obtained/OPUS_POS_word_list','w',encoding = 'utf-8')
file8 = open('../corpora_and_texts_obtained/book_1gm_POS','rb')
fileout7 = open('../corpora_and_texts_obtained/book_1gm_POS_word_list','w',encoding = 'utf-8')
POS = {}
line = file1.readline().decode('utf-8').split()
for i in line:
	i = i.split('_')
	POS[i[0]] = i[1]

for line in file2:
	line = line.decode('utf-8').split()
	if line[0] in POS:
		fileout1.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\t' + POS[line[0]] + "\n")

line = file3.readline().decode('utf-8').split()
for i in line:
	i = i.split('_')
	fileout2.write(i[0] + '\t' + i[1] + '\n')

line = file4.readline().decode('utf-8').split()
for i in line:
	i = i.split('_')
	fileout3.write(i[0] + '\t' + i[1] + '\n')

line = file5.readline().decode('utf-8').split()
for i in line:
	i = i.split('_')
	fileout4.write(i[0] + '\t' + i[1] + '\n')

line = file6.readline().decode('utf-8').split()
for i in line:
	i = i.split('_')
	fileout5.write(i[0] + '\t' + i[1] + '\n')

line = file7.readline().decode('utf-8').split()
for i in line:
	i = i.split('_')
	fileout6.write(i[0] + '\t' + i[1] + '\n')

line = file8.readline().decode('utf-8').split()
for i in line:
	i = i.split('_')
	fileout7.write(i[0] + '\t' + i[1] + '\n')


file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
fileout1.close()
fileout2.close()
fileout3.close()
fileout4.close()
fileout5.close()
fileout6.close()
fileout7.close()
