file1 = open('../corpora/epl.cd', 'rb')
fileout1 = open('../corpora/../corpora/syllable_list', 'w', encoding = 'utf-8')
fileout2 = open('../corpora/syllable_len', 'w', encoding = 'utf-8')

word = []
for line in file1:
	line = line.decode('utf-8').split('\\')
	if line[1].lower() not in word:
		word.append(line[1].lower())
		fileout1.write(line[1].lower() + '\t')
		fileout2.write(line[1].lower() + '\t')
		syl = line[-1][1:-1].split('][')
		fileout2.write(str(len(syl)) + '\n')
		for i in syl:
			fileout1.write(i + '\t')
		fileout1.write('\n')

file1.close()
fileout1.close()
fileout2.close()