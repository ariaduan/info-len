# bin per 2% voca
# 1. replicate, binning
# 2. normal binning
# 3. gaussian
# 4. most frequent
from argparse import ArgumentParser
from pathlib import Path

p = ArgumentParser()
p.add_argument("--inp_file", action = "append", type = Path)
args = p.parse_args()
inps = args.inp_file

for inp in inps:
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
	fileout2.write("word,type,value_int,value_float,value_bin,len,cnt,POS,pho,syl,POS,pho,syl,d,p,h,func\n")
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
	fileout1.close()
	fileout2.close()
	fileout3.close()