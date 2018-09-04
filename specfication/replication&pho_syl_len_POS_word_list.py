file1 = open('../corpora/pho_syl_POS','rb')
file2 = open('../corpora/pho_syl_len_word_list','rb')
fileout1 = open('../corpora/pho_syl_len_POS_word_list','w',encoding = 'utf-8')
file3 = open('../corpora/replication_POS','rb')
fileout2 = open('../corpora/replication_POS_word_list','w',encoding = 'utf-8')

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

file1.close()
file2.close()
file3.close()
fileout1.close()
fileout2.close()