from zs import ZS
from argparse import ArgumentParser
from pathlib import Path
import re
value = re.compile(r'^[A-Za-z][a-z]+$')

p = ArgumentParser()
p.add_argument("input_folder", type = Path) # '/om/data/public/corpora/google_web_ngrams/data/2gms'
p.add_argument("OPUS_word_list", type = Path) # '../corpora_and_texts_obtained/OPUS_word_list'
args = p.parse_args()

input_folder = str(args.input_folder)
OPUS_word_list = str(args.OPUS_word_list)

file1 = open(OPUS_word_list,'rb')

fileout1 = open('../corpora_and_texts_obtained/1gm_google_book_sort_OPUS_word_list','w',encoding = 'utf-8')

OPUS_word_list = []

for line in file1:
	line = line.decode('utf-8').split()
	OPUS_word_list.append(line[0])

cnt = {}
file = ZS(input_folder)
c = 0
for line in file:
	c += 1
	if c % 1000000 == 0:
		print(c, line.decode('utf-8'))
	line = line.decode('utf-8').split()
	if int(line[1]) < 1960 or int(line[1]) > 2000:
		continue
	tgt = line[0].split("_")[0]
	if tgt not in OPUS_word_list:
		continue
	if tgt not in cnt:
		cnt[tgt] = 0
	cnt[tgt] += int(line[2])
file.close()

sort_words = sorted(cnt.items())
tmp = []
for i, j in sort_words:
	tmp.append([j, i])
sort_cnt = sorted(tmp, reverse = True)

for i, j in sort_cnt:
	fileout1.write(j + '\t' + str(i) + '\n')
	
file1.close()
fileout1.close()


