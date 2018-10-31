import os
import math as m
from zs import ZS
from check_normality import check_normality
from argparse import ArgumentParser
from pathlib import Path
import re



file = ZS('/om/data/public/corpora/google-books-v2/eng-us-all/google-books-eng-us-all-20120701-2gram.zs')
c = 0
for line in file:
	c += 1
	if c == 1000:
		print(line.decode('utf-8'))
file.close()


