file1 = open('../corpora_and_texts_obtained/OPUS_word_list','rb')
file2 = open('../corpora_and_texts_obtained/google_25000','rb')
fileout1 = open('../corpora_and_texts_obtained/replication_word_list','w',encoding = 'utf-8')
fileout2 = open('../corpora_and_texts_obtained/replication_word_list_for_POS','w',encoding = 'utf-8')

voca1 = []
for line in file1:
	line = line.decode('utf-8').split()
	voca1.append(line[0])

for line in file2:
	line = line.decode('utf-8').split()
	if line[0] in voca1:
		fileout1.write(line[0] + '\n')
		if line[0] == "wanna" or line[0] == "gonna" or line[0] == "gotta" or line[0] == "dunno" or line[0] == "na":
				continue
		fileout2.write(line[0] + '\n')

file1.close()
fileout1.close()
fileout2.close()
