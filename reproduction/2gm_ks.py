from check_normality import check_normality
file1 = open("/om/data/public/info-len/corpora_and_texts_obtained/2gm_en_merge_leaveone_1",'rb')
fileout = open("/om/data/public/info-len/corpora_and_texts_obtained/2gm_en_merge_leaveone_0_bin",'w',encoding = 'utf-8')
print('haha')
file1.readline()
cnt = 0
for line in file1:
	cnt += 1
	if cnt % 100 == 0:
		print(cnt)
	line = line.decode('utf-8').split('\t')
	x = []
	for i in line[:10]:
		fileout.write(i + '\t')
	tmp = line[10].split('), (')
	tmp[0] = tmp[0][2:]
	tmp[-1] = tmp[-1][:-3]
	for i in tmp:
		w, c = i.split(', ')
		w = float(w)
		c = int(c)
		for j in range(int(c)):
			x.append(w)
	if len(x) < 3:
		fileout.write("-1\t-1\t-1\t-1\n")
		continue
	d, p, h, func = check_normality(x)
	fileout.write(str(d) + '\t' + str(p) + '\t' + str(h) + '\t' + func + '\n')

file1.close()
fileout.close()
