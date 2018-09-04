file1 = open('../corpora/phoneme_list', 'rb')
fileout = open('../corpora/phoneme_len', 'w', encoding = 'utf-8')

word = []
for line in file1:
	line = line.decode('utf-8').split()
	#only lower case
	if line[0].lower() not in word:
		fileout.write(line[0].lower() + '\t' + str(len(line) - 1) + '\n')
		word.append(line[0])

file1.close()
fileout.close()