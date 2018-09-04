file1 = open('../corpora_and_texts_obtained/news.en-00000-of-00100', 'rb')
fileout = open('../corpora_and_texts_obtained/devset', 'w', encoding = 'utf-8')

cnt = 0
for line in file1:
	line = line.decode('utf-8').split()
	fileout.write('<bos> ')
	#change captized case into lower case
	fileout.write(line[0].lower() + ' ')
	for i in line[1:]:
		fileout.write(i + ' ')
	fileout.write('<eos>\n')
	cnt += 1
	if cnt == 60000:
		break

file1.close()
fileout.close()

