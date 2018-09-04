file2 = open('corpora_and_texts_obtained/replication_POS_word_list', 'rb')
file3 = open('corpora_and_texts_obtained/pho_syl_len_word_list', 'rb')

POS = {}
pho_syl = {}
for line in file2:
	line = line.decode('utf-8').split()
	POS[line[0]] = line[1]
for line in file3:
	line = line.decode('utf-8').split()
	pho_syl[line[0]] = line[1:]


lst = ['2', '3', '4']
for num in lst:
	gaussian = {}
	file4 = open('corpora_and_texts_obtained/' + num + 'gm_gaussian.csv', 'rb')
	for line in file4:
		line = line.decode('utf-8').split(',')
		gaussian[line[0]] = line[1:]
	
	file1 = open('corpora_and_texts_obtained/' + num + 'gm_info_freq', 'rb')
	fileout = open('corpora_and_texts_obtained/' + num + 'gm_merge', 'w', encoding = 'utf-8')
	
	fileout.write('word\tinfo_int\tfreq_int\tinfo_float\tfreq_float\tlen\tcnt\tPOS\tpho\tsyl\td\tp\th\tfunc\n')
	file1.readline()
	for line in file1:
		line = line.decode('utf-8').split()
		for i in line:
			fileout.write(i + '\t')
		if line[0] in POS:
			fileout.write(POS[line[0]] + '\t')
		else:
			fileout.write('-1\t')
		if line[0] in pho_syl:
			fileout.write(pho_syl[line[0]][0] + '\t' + pho_syl[line[0]][1] + '\t')
		else:
			fileout.write('-1\t-1\t')
		if line[0] in gaussian:
			fileout.write(gaussian[line[0]][0] + '\t' + gaussian[line[0]][1] + '\t' + gaussian[line[0]][2] + '\t' + gaussian[line[0]][3][:-1] + '\n')
		else:
			fileout.write('-1\t-1\t-1\t-1\n')
	
	file1.close()
	file4.close()
	fileout.close()


file2.close()
file3.close()