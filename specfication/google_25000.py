file1 = open('../corpora/vocab_cs','rb')
fileout = open('../corpora/google_25000','w',encoding = 'utf-8')

import re
value = re.compile(r'^[A-Za-z][a-z]+$')

cnt = 0
words = []
for line in file1:
	line = line.decode('utf-8').split()
	#only lower case and alphabetic
	if value.match(line[0]) and line[0].lower() not in words:
		fileout.write(line[0] + '\n')
		words.append(line[0].lower())
		cnt += 1
		if cnt == 25000:
			break

file1.close()
fileout.close()