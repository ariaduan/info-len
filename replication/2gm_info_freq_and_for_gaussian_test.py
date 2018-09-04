import os
import math as m
import gzip as gz
from argparse import ArgumentParser
from pathlib import Path
import re
value = re.compile(r'^[A-Za-z][a-z]+$')

p = ArgumentParser()
p.add_argument("input_folder", type = Path) # '/om/data/public/corpora/google_web_ngrams/data/2gms'
p.add_argument("replication_word_list", type = Path) # '../corpora_and_texts_obtained/replication_word_list'
p.add_argument("replication_POS_word_list", type = Path) # '../corpora_and_texts_obtained/replication_POS_word_list'
p.add_argument("pho_syl_len_word_list", type = Path) # '../corpora_and_texts_obtained/pho_syl_len_word_list'
args = p.parse_args()

input_folder = str(args.input_folder)
replication_word_list = str(args.replication_word_list)
replication_POS_word_list = str(args.replication_POS_word_list)
pho_syl_len_word_list = str(args.pho_syl_len_word_list)
lt = os.listdir(input_folder)

file1 = open(replication_word_list,'rb')
file2 = open(replication_POS_word_list,'rb')
file3 = open(pho_syl_len_word_list,'rb')
fileout1 = open('../corpora_and_texts_obtained/2gm_info_freq','w',encoding = 'utf-8')
fileout2 = open('../corpora_and_texts_obtained/2gm_for_gaussian_test','w',encoding = 'utf-8')
fileout3 = open('../corpora_and_texts_obtained/2gm_POS_for_gaussian_test','w',encoding = 'utf-8')
fileout4 = open('../corpora_and_texts_obtained/2gm_pho_syl_len','w',encoding = 'utf-8')
fileout5 = open('../corpora_and_texts_obtained/2gm_POS_info_freq','w',encoding = 'utf-8')

replication_word_list = []
replication_POS_word_list = {}
pho_syl_len_word_list = {}
for line in file1:
	line = line.decode('utf-8').split()
	replication_word_list.append(line[0])
for line in file2:
	line = line.decode('utf-8').split()
	replication_POS_word_list[line[0]] = line[1]
for line in file3:
	line = line.decode('utf-8').split()
	pho_syl_len_word_list[line[0]] = line[1:]

ix = {} # ix[w] = {cnt:0, ix_bg:[], info:0, info_g:[], N:0}
total = 0
bg = {} # b g['bg'] = 0
cnt = 'cnt'
ix_bg = 'ix_bg'
freq = 'freq'
info = 'info'
info_g = 'info_g'
N = 'N'
for i in lt:
	if i == '2gm.idx':
		continue
	print(i)
	file = gz.open(input_folder + '/' + i,'rb')
	for line in file:
		line = line.decode('utf-8').split()
		if len(line) < 3:
			continue
		for w in line[:-1]:
			if value.match(w):
				w = w.lower()
		tmp_bg = line[0]
		tmp_tg = line[1]
		tmp_cnt = int(line[2])
		if tmp_tg not in ix:
			ix[tmp_tg] = {cnt:0, ix_bg:{}, freq:0, info:0, info_g:[], N:0}
		ix[tmp_tg][cnt] += int(tmp_cnt)
		ix[tmp_tg][N] += 1
		ix[tmp_tg][ix_bg][tmp_bg] = tmp_cnt
		if tmp_bg not in bg:
			bg[tmp_bg] = int(tmp_cnt)
		else:
			bg[tmp_bg] += int(tmp_cnt)
		total += tmp_cnt
	file.close()

fileout1.write("word\tinfo_int\tfreq_int\tinfo_float\tfreq_float\tlen\tcnt\n")
fileout4.write("word\tinfo_int\tfreq_int\tinfo_float\tfreq_float\tlen\tpho\tsyl\tcnt\n")
fileout5.write("word\tinfo_int\tfreq_int\tinfo_float\tfreq_float\tlen\tcnt\tPOS\n")

for i in ix:
	if i in replication_word_list:
		b = ix[i][ix_bg]
		for tmp_b in b:
			ix[i][info] += -m.log(b[tmp_b] / bg[tmp_b], 2)
			ix[i][info_g].append(-m.log(b[tmp_b] / bg[tmp_b], 2))
		ix[i][info] = ix[i][info] / ix[i][N]
		ix[i][freq] = -m.log(ix[i][cnt] / total, 2)
		fileout1.write(i + '\t' + str(int(ix[i][info])) + '\t' + str(int(ix[i][freq])) + '\t' + str(ix[i][info]) + '\t' + str(ix[i][freq]) + '\t' + str(len(i)) + '\t' + str(ix[i][cnt]) + '\n')
		fileout2.write(i + '\t') 
		for j in ix[i][info_g]:
			fileout2.write(str(j) + '\t')
		fileout2.write('\n')
	if i in replication_POS_word_list:
		fileout3.write(i + '\t' + replication_POS_word_list[i] + '\t') 
		for j in ix[i][info_g]:
			fileout3.write(str(j) + '\t')
		fileout3.write('\n')
		fileout5.write(i + '\t' + str(int(ix[i][info])) + '\t' + str(int(ix[i][freq])) + '\t' + str(ix[i][info]) + '\t' + str(ix[i][freq]) + '\t' + str(len(i)) + '\t' + str(ix[i][cnt]) + '\t' + replication_POS_word_list[i] + '\n')
	if i in pho_syl_len_word_list:
		fileout4.write(i + '\t' + str(int(ix[i][info])) + '\t' + str(int(ix[i][freq])) + '\t' + str(ix[i][info]) + '\t' + str(ix[i][freq]) + '\t' + str(len(i)) + '\t' + pho_syl_len_word_list[i][0] + '\t' + pho_syl_len_word_list[i][1] + str(ix[i][cnt]) + '\n')
file1.close()
file2.close()
file3.close()
fileout1.close()
fileout2.close()
fileout3.close()
fileout4.close()
fileout5.close()