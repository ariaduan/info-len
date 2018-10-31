import re
value = re.compile(r'^[A-Za-z][a-z]+$')

file1 = open('../corpora_and_texts_obtained/OpenSubtitles.bg-en.en', 'rb')
fileout = open('../corpora_and_texts_obtained/OPUS_word_list', 'w', encoding = 'utf-8')
fileout1 = open('../corpora_and_texts_obtained/OPUS_word_list_for_POS', 'w', encoding = 'utf-8')

word = {}
for line in file1:
	line = line.decode('utf-8').split()
	for i in line:
		#only lower case and alphabetic
		if value.match(i):
			i = i.lower()
			if len(i) not in word:
				word[len(i)] = [i]
			elif i not in word[len(i)]:
				word[len(i)].append(i)
lt = list(word)
m = max(lt)

for i in range(1, m+1):
	if i not in word:
		continue
	for j in word[i]:
		fileout.write(j + '\n')
		if j == "wanna" or j == "gonna" or j == "gotta" or j == "dunno" or j == "na":
			continue
		else:
			fileout1.write(j + '\n')

file1.close()
fileout.close()
fileout1.close()
