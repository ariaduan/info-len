import math as m

file1 = open('../corpora_and_texts_obtained/devset_result', 'rb')
file2 = open('../corpora_and_texts_obtained/replication_word_list', 'rb')
file3 = open('../corpora_and_texts_obtained/freq_in_train_set', 'rb')
file4 = open('../corpora_and_texts_obtained/replication_POS_word_list','rb')
file5 = open('../corpora_and_texts_obtained/pho_syl_len_word_list', 'rb')
fileout1 = open('../corpora_and_texts_obtained/RNN_for_gaussian_test', 'w', encoding = 'utf-8')
fileout2 = open('../corpora_and_texts_obtained/RNN_POS_for_gaussian_test', 'w', encoding = 'utf-8')
fileout3 = open('../corpora_and_texts_obtained/RNN_info_freq', 'w', encoding = 'utf-8')
fileout4 = open('../corpora_and_texts_obtained/RNN_POS_info_freq', 'w', encoding = 'utf-8')
fileout5 = open('../corpora_and_texts_obtained/RNN_info_freq_pho_syl', 'w', encoding = 'utf-8')

OPUS = []
for line in file2:
	line = line.decode('utf-8').split()
	OPUS.append(line[0])

freq_train = {}
for line in file3:
	line = line.decode('utf-8').split()
	freq_train[line[0]] = line[2:]

POS = {}
for line in file4:
	line = line.decode('utf-8').split()
	POS[line[0]] = line[1]

pho_syl = {}
for line in file5:
	line = line.decode('utf-8').split()
	if line[1].isdigit():
		pho[line[0]] = line[1:]

word_info = {}
word_info_g = {}
word_cnt = {}
for line in file1:
	line = line.decode('utf-8').split()
	if line[0] in word_info:
		word_info += float(line[1])
		word_info_g[line[0]].append(float(line[1]))
		word_cnt[line[0]] += 1
	else:
		word_info = float(line[1])
		word_info_g[line[0]] = [float(line[1])]
		word_cnt[line[0]] = 1

fileout3.write("word\tinfo_int\tfreq_int\tinfo_float\tfreq_float\tlen\tcnt\n")
fileout4.write("word\tinfo_int\tfreq_int\tinfo_float\tfreq_float\tlen\tpho\tsyl\tcnt\n")
fileout5.write("word\tinfo_int\tfreq_int\tinfo_float\tfreq_float\tlen\tcnt\tPOS\n")
for i in word_info:
	if i in OPUS:
		fileout1.write(i + '\t')
		for j in word_info_g[i]:
			fileout1.write(str(j) + '\t')
		fileout1.write('\n')
		fileout3.write(i + '\t' + str(int(word_info[i] / word_cnt[i])) + '\t' + freq_train[i][0] + '\t' + str(word_info[i] / word_cnt[i]) + '\t' + freq_train[i][1] + '\t' + len(i) + '\t' + str(word_cnt[i]) + '\n')
	if i in POS:
		fileout2.write(i + '\t' + POS[i] + '\t')
		for j in word_info_g[i]:
			fileout2.write(str(j) + '\t')
		fileout2.write('\n')
		fileout5.write(i + '\t' + str(int(word_info[i] / word_cnt[i])) + '\t' + freq_train[i][0] + '\t' + str(word_info[i] / word_cnt[i]) + '\t' + freq_train[i][1] + '\t' + len(i) + '\t' + str(word_cnt[i]) + '\t' + POS[i] + '\n')
	if i in pho_syl:
		fileout4.write(i + '\t' + str(int(word_info[i] / word_cnt[i])) + '\t' + freq_train[i][0] + '\t' + str(word_info[i] / word_cnt[i]) + '\t' + freq_train[i][1] + '\t' + len(i) + '\t' + pho_syl[i][0] + '\t' + pho_syl[i][1] + '\t' + str(word_cnt[i]) + '\n')
	
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
fileout1.close()
fileout2.close()
fileout3.close()
fileout4.close()
fileout5.close()