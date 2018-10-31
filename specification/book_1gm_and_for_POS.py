file1 = open('../corpora_and_texts_obtained/1gm_google_book_sort_OPUS_word_list', 'rb')
file2 = open('../corpora_and_texts_obtained/OPUS_POS_word_list', 'rb')
fileout1 = open('../corpora_and_texts_obtained/book_1gm_word_list', 'w', encoding = 'utf-8')
fileout2 = open('../corpora_and_texts_obtained/book_1gm_for_POS', 'w', encoding = 'utf-8')


OPUS = []
for line in file2:
	line = line.decode('utf-8').split()
	OPUS.append(line[0])
c = 0
for line in file1:
	line = line.decode('utf-8').split()
	if line[0] in OPUS:
		c += 1
		if c == 25001:
			break
	else:
		continue
	fileout1.write(line[0] + '\n')
	if line[0] == "wanna" or line[0] == "gonna" or line[0] == "gotta" or line[0] == "dunno" or line[0] == "na":
		continue
	fileout2.write(line[0] + '\n')

file1.close()
file2.close()
fileout1.close()
fileout2.close()
