import os
import math as m
import gzip as gz
from check_normality import check_normality
from argparse import ArgumentParser
from pathlib import Path
import re
value = re.compile(r'^[A-Za-z][a-z]+$')

p = ArgumentParser()
p.add_argument("input_folder", type = Path) # '/om/data/public/corpora/google_web_ngrams/data/2gms'
p.add_argument("replication_word_list", type = Path) # '../corpora_and_texts_obtained/replication_word_list'
p.add_argument("replication_POS_word_list", type = Path) # '../corpora_and_texts_obtained/replication_POS_word_list'
p.add_argument("pho_syl_len_word_list", type = Path) # '../corpora_and_texts_obtained/pho_syl_len_word_list'
p.add_argument("--language", type = str)
p.add_argument("--LOO", type = bool, default = False)
args = p.parse_args()

input_folder = str(args.input_folder)
replication_word_list = str(args.replication_word_list)
replication_POS_word_list = str(args.replication_POS_word_list)
pho_syl_len_word_list = str(args.pho_syl_len_word_list)
lang = args.language
lt = os.listdir(input_folder)

file1 = open(replication_word_list,'rb')
file2 = open(replication_POS_word_list,'rb')
file3 = open(pho_syl_len_word_list,'rb')
if args.LOO == True:
	fileout1 = open('../corpora_and_texts_obtained/2gm_{}_merge_leaveone_1'.format(lang),'w',encoding = 'utf-8')
	print('../corpora_and_texts_obtained/2gm_{}_merge_leaveone'.format(lang))
else:
	fileout1 = open('../corpora_and_texts_obtained/2gm_{}_merge_1'.format(lang),'w',encoding = 'utf-8')
	print('../corpora_and_texts_obtained/2gm_{}_merge'.format(lang))
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
		ix[tmp_tg][N] += tmp_cnt
		ix[tmp_tg][ix_bg][tmp_bg] = tmp_cnt
		if tmp_bg not in bg:
			bg[tmp_bg] = int(tmp_cnt)
		else:
			bg[tmp_bg] += int(tmp_cnt)
		total += tmp_cnt
	file.close()

fileout1.write("word\tinfo_int\tfreq_int\tinfo_float\tfreq_float\tlen\tcnt\tPOS\tpho\tsyl\td\tp\th\tfunc\n")

if args.LOO == True:	
	for i in ix:
		if i in replication_word_list:
			b = ix[i][ix_bg]
			for tmp_b in b:
				if b[tmp_b] - 1 == 0 or bg[tmp_b] - 1 == 0:
					continue
				ix[i][info] += (-m.log((b[tmp_b] - 1) / (bg[tmp_b] - 1), 2) * b[tmp_b])
				ix[i][info_g].append(-m.log((b[tmp_b] - 1) / (bg[tmp_b] - 1), 2))
			ix[i][info] = ix[i][info] / ix[i][N]
			ix[i][freq] = -m.log(ix[i][cnt] / total, 2)
			fileout1.write(i + '\t' + str(int(ix[i][info])) + '\t' + str(int(ix[i][freq])) + '\t' + str(ix[i][info]) + '\t' + str(ix[i][freq]) + '\t' + str(len(i)) + '\t' + str(ix[i][cnt]) + '\t')
			if i in replication_POS_word_list:
				fileout1.write(replication_POS_word_list[i] + '\t')
			else:
				fileout1.write("-1" + "\t")
			if i in pho_syl_len_word_list:
				fileout1.write(pho_syl_len_word_list[i][0] + '\t' + pho_syl_len_word_list[i][1] + '\t')
			else:
				fileout1.write("-1" + "\t" + "-1" + "\t")
			x = ix[i][info_g]
			x = list(map(float, x))
			if len(x) < 3:
				fileout1.write("-1\t-1\t-1\t-1\n")
				continue
			d, p, h, func = check_normality(x)
			fileout1.write(str(d) + '\t' + str(p) + '\t' + str(h) + '\t' + func + '\n')

else:
	for i in ix:
		if i in replication_word_list:
			b = ix[i][ix_bg]
			for tmp_b in b:
				if b[tmp_b] - 1 == 0 or bg[tmp_b] - 1 == 0:
					continue
				ix[i][info] += (-m.log(b[tmp_b] / bg[tmp_b], 2) * b[tmp_b])
				ix[i][info_g].append(-m.log(b[tmp_b] / bg[tmp_b], 2))
			ix[i][info] = ix[i][info] / ix[i][N]
			ix[i][freq] = -m.log(ix[i][cnt] / total, 2)
			fileout1.write(i + '\t' + str(int(ix[i][info])) + '\t' + str(int(ix[i][freq])) + '\t' + str(ix[i][info]) + '\t' + str(ix[i][freq]) + '\t' + str(len(i)) + '\t' + str(ix[i][cnt]) + '\t')
			if i in replication_POS_word_list:
				fileout1.write(replication_POS_word_list[i] + '\t')
			else:
				fileout1.write("-1" + "\t")
			if i in pho_syl_len_word_list:
				fileout1.write(pho_syl_len_word_list[i][0] + '\t' + pho_syl_len_word_list[i][1] + '\t')
			else:
				fileout1.write("-1" + "\t" + "-1" + "\t")
			x = ix[i][info_g]
			x = list(map(float, x))
			if len(x) < 3:
				fileout1.write("-1\t-1\t-1\t-1\n")
				continue
			d, p, h, func = check_normality(x)
			fileout1.write(str(d) + '\t' + str(p) + '\t' + str(h) + '\t' + func + '\n')
		
	
file1.close()
file2.close()
file3.close()
fileout1.close()

if args.LOO == True:
	inp = '../corpora_and_texts_obtained/2gm_{}_merge_leaveone_1'.format(lang)
else:
	inp = '../corpora_and_texts_obtained/2gm_{}_merge_1'.format(lang)
file1 = open(inp, 'rb')
fileout1 = open(str(inp) + '_bin_pair.csv', 'w', encoding = 'utf-8')
fileout2 = open(str(inp) + '_bin_type.csv', 'w', encoding = 'utf-8')
fileout3 = open(str(inp) + '_bin_all.csv', 'w', encoding = 'utf-8')

words = {}
info = []
freq = []
file1.readline()
for line in file1:
	line = line.decode('utf-8').split()
	words[line[0]] = line[1:]
	info.append(float(line[3]))
	freq.append(float(line[4]))

words_info = list(words)
words_freq = list(words)
info_bin = {}
freq_bin = {}
for i in range(len(info) - 1):
	for j in range(i + 1, len(info)):
		if info[i] > info[j]:
			info[i], info[j] = info[j], info[i]
			words_info[i], words_info[j] = words_info[j], words_info[i]

for i in range(len(freq) - 1):
	for j in range(i + 1, len(freq)):
		if freq[i] > freq[j]:
			freq[i], freq[j] = freq[j], freq[i]
			words_freq[i], words_freq[j] = words_freq[j], words_freq[i]
cnt = 0
limit = 0.02 * len(words)
total = 0
for i in range(len(info)):
	total += info[i]
	cnt += 1
	if cnt > limit:
		binnum = total / cnt
		for j in  range(i - cnt + 1, i + 1):
			words[words_info[j]].append(str(binnum))
		cnt = 0
		total = 0
	if i == len(info) - 1:
		binnum = total / cnt
		for j in  range(i - cnt + 1, i + 1):
			words[words_info[j]].append(str(binnum))
		cnt = 0
		total = 0

for i in range(len(freq)):
	total += freq[i]
	cnt += 1
	if cnt > limit:
		binnum = total / cnt
		for j in  range(i - cnt + 1, i + 1):
			words[words_freq[j]].append(str(binnum))
		cnt = 0
		total = 0
	if i == len(freq) - 1:
		binnum = total / cnt
		for j in  range(i - cnt + 1, i + 1):
			words[words_freq[j]].append(str(binnum))
		cnt = 0
		total = 0

fileout1.write("word,info_int,freq_int,info_float,freq_float,len,cnt,POS,pho,syl,d,p,h,func,info_bin,freq_bin\n")
fileout2.write("word,type,value_int,value_float,value_bin,len,cnt,POS,pho,syl,d,p,h,func\n")
fileout3.write("word,type,value_int,value_float,value_bin,cnt,POS,d,p,h,func\n")
for i in words:
	fileout1.write(i + ',')
	for j in words[i][:-1]:
		fileout1.write(j + ',')
	fileout1.write(words[i][-1] + '\n')
	fileout2.write(i + ',' + 'info' + ',' + words[i][0] + ',' + words[i][2] + ',' + words[i][13] + ',' + words[i][4] + ',' + words[i][5] + ',' + words[i][6] + ',' + words[i][7] + ',' + words[i][8] + words[i][9] + ',' + words[i][10] + ',' + words[i][11] + ',' + words[i][12] + '\n')
	fileout2.write(i + ',' + 'freq' + ',' + words[i][1] + ',' + words[i][3] + ',' + words[i][14] + ',' + words[i][4] + ',' + words[i][5] + ',' + words[i][6] + ',' + words[i][7] + ',' + words[i][8] + words[i][9] + ',' + words[i][10] + ',' + words[i][11] + ',' + words[i][12] + '\n')
	fileout3.write(i + ',' + 'info' + ',' + words[i][0] + ',' + words[i][2] + ',' + words[i][13] + ',' + words[i][5] + ',' + words[i][6] + words[i][9] + ',' + words[i][10] + ',' + words[i][11] + ',' + words[i][12] + '\n')
	fileout3.write(i + ',' + 'freq' + ',' + words[i][1] + ',' + words[i][3] + ',' + words[i][14] + ',' + words[i][5] + ',' + words[i][6] + words[i][9] + ',' + words[i][10] + ',' + words[i][11] + ',' + words[i][12] + '\n')
	fileout3.write(i + ',' + 'len' + ',' + words[i][4] + ',' + words[i][4] + ',' + words[i][4] + ',' + words[i][5] + ',' + words[i][6] + words[i][9] + ',' + words[i][10] + ',' + words[i][11] + ',' + words[i][12] + '\n')
	fileout3.write(i + ',' + 'pho' + ',' + words[i][7] + ',' + words[i][7] + ',' + words[i][7] + ',' + words[i][5] + ',' + words[i][6] + words[i][9] + ',' + words[i][10] + ',' + words[i][11] + ',' + words[i][12] + '\n')
	fileout3.write(i + ',' + 'syl' + ',' + words[i][8] + ',' + words[i][8] + ',' + words[i][8] + ',' + words[i][5] + ',' + words[i][6] + words[i][9] + ',' + words[i][10] + ',' + words[i][11] + ',' + words[i][12] + '\n')

file1.close()
fileout1.close()
fileout2.close()
fileout3.close()
