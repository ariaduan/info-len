file1 = open('../corpora/replication_word_list','rb')
file2 = open('../corpora/syllable_len','rb')
file3 = open('../corpora/phoneme_len','rb')
fileout1 = open('../corpora/pho_syl_len_word_list','w',encoding = 'utf-8')
fileout2 = open('../corpora/pho_syl_word_list_for_POS','w',encoding = 'utf-8')

voca1 = []
for line in file1:
	line = line.decode('utf-8').split()
	voca1.append(line[0])

syl = {}
for line in file2:
	line = line.decode('utf-8').split()
	if line[0] in voca1 and line[1].isdigit():
		syl[line[0]] = line[1]

for line in file3:
	line = line.decode('utf-8').split()
	if line[0] in syl:
		fileout1.write(line[0] + '\t' + line[1] + '\t' + syl[line[0]] + '\n')
		if line[0] == "wanna" or line[0] == "gonna" or line[0] == "gotta" or line[0] == "dunno" or line[0] == "na":
			continue
		fileout2.write(line[0] + '\n')

file1.close()
file2.close()
file3.close()
fileout1.close()
fileout2.close()