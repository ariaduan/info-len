import os as o
import re
import math as m
from argparse import ArgumentParser
from pathlib import Path

p = ArgumentParser()
p.add_argument("train_set", type = Path) # '/Users/ariaduan1.0/Desktop/summer_experiment/Roger/projects/1-billion-word-language-modeling-benchmark-r13output/training-monolingual.tokenized.shuffled'
args = p.parse_args()
train_set = args.train_set

value = re.compile(r'^[A-Za-z][a-z]+$')

lt_ori = o.listdir(train_set)
lt = []
for i in lt_ori:
	if str(i)[:4] == 'news':
		lt.append(i)

word = {}
total = 0
for i in lt:
	file = open(i,'rb')
	for line in file:
		line = line.decode('utf-8').split()
		for i in line:
			if not value.match(i):
				continue
			i = i.lower()
			if i not in word:
				word[i] = 1
				total += 1
			else:
				word[i] += 1
				total += 1
	file.close()

fileout = open('../corpora_and_texts_obtained/freq_in_train_set', 'w', encoding = 'utf-8')
fileout.write('word\tcnt_int\tfreq_int\tfreq_float\n')
for i in word:
	fileout.write(i + "\t" + str(word[i]) + "\t" + str(int(-m.log(word[i] / total, 2))) + "\t" + str(-m.log(word[i] / total, 2)) + '\n')

fileout.close()