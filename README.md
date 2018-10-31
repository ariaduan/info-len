# A Further Study on "Word lengths are optimized for efficient communication"
Code for [Word lengths are optimized for efficient communication](http://www.pnas.org/content/108/9/3526.short) reproduction(ngram) and replication(RNN). The code is written in Python.

## Introduction  

Assuming the outcome in that paper is trustworthy, we first tried to use RNN to replicate that work so as to test the generalization ability of the proposition and methods, but failed.  
  
So we turn back to try to reproduce the work and then scrutinize each prerequisite to see what cause the failure of the replication, meantime evaluating the reasonableness of each prerequisite set in that paper so as to confirm the validity of that work. 
  
## Prerequisites
 * [Python 3.6+ compiler](https://www.python.org)
 * [staford-postagger-full](https://nlp.stanford.edu/software/stanford-postagger-full-2018-10-16.zip). Save it under this repository.
 * [OPUS OpenSubtitle corpus for English](http://opus.nlpl.eu/download.php?f=OpenSubtitles/bg-en.xml.gz)(This file is already saved as **OpenSubtitles.bg-en.en** in **corpora_and_texts_obtained** folder which can be downloaded from [Google drive](https://drive.google.com/drive/folders/15bXrFCWAlQrJ3RTFImA9bdKI57G-uyR5?usp=sharing). Or you can find it on MIT Openmind in /om/data/public/info-len.)
 * [1T-benchmark corpora](http://www.statmt.org/lm-benchmark/1-billion-word-language-modeling-benchmark-r13output.tar.gz) (MIT Openmind has this resource in **/om/data/public/info-len/1-billion-word-language-modeling-benchmark-r13output**)
 * [google-web-ngram corpora for English](https://catalog.ldc.upenn.edu/LDC2006T13)(MIT Openmind has this resource in **/om/data/public/corpora/google-web-ngrams**)(Extract the file documenting unigrams according to their frequency. This file is already saved as **vocab_cs** in **corpora_and_texts_obtained** folder.)
 * [CMU phoneme list](http://www.speech.cs.cmu.edu/cgi-bin/cmudict). (This file is already saved as **phoneme_list** in **corpora_and_texts_obtained** folder.)  
 * [CELEX corpora](https://catalog.ldc.upenn.edu/LDC96L14)(MIT Openmind has this resource in **/om/data/public/corpora/celex**)(Extract **epl.cd** file from it. (This file is already saved in **corpora_and_texts_obtained** folder.)
 * [google-book-v2 corpora for English](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html)(MIT Openmind has this resource in **/om/data/public/corpora/google-book-v2 corpora**)
 
## Procedure  
In this section we presents the usage of codes for this work. **Please run the following codes under this master repository**.
  
### Specification word lists:  
This section is used for preparing the word lists for the replication. 
```
cd specification
```
You can skip this section if you have downloaded the **corpora_and_texts_obtained** folder from Google Drive. Please save the folder you have downloaded under this repository(to replace the old one).

#### OPUS 
	  
1) Get **OPUS_word_list** and **OPUS_word_list_for_POS** with **OPUS_word_list.py**:  
```
python3 OPUS_word_list.py
```
The obtained **OPUS_word_list** and **OPUS_word_list_for_POS** texts will be in **corpora_and_texts_obtained** folder. The former file contains words that exist in OPUS OpenSubtitle corpora. The latter file will be used as input text to obtain POS tags for each word. Compound words like "wanna" are removed.		  
  
#### Google  
1) Get **google_25000** word list with **google_25000.py**:  
```
python3 google_25000.py
```
The obtained **google_25000** text will be in **corpora_and_texts_obtained** folder. This file contains 25000 most frequent words in google dataset.  

2) Get **google_50000(/75000/100000)** word list with **google_50000(/75000/100000).py**: 
```
python3 google_50000.py
python3 google_75000.py
python3 google_100000.py
```
The obtained **google_50000(/75000/100000)** text will be in **corpora_and_texts_obtained** folder. This file contains the 25001~50000(/50001~75000/75001~100000) most frequent words in google dataset.  
  
#### OPUS+Google  

1) Get **replication_word_list** and **replication_word_list_for_POS** with **replication_word_list.py**: 
```
python3 replication_word_list.py
```
The obtained **replication_word_list** and **replication_word_list_for_POS** texts will be in **corpora_and_texts_obtained** folder. **replication_word_list** contains the intersection of **OPUS** and **google_25000**. **replication_word_list_for_POS** will be used as input text to obtain POS tags for each word. Compound words like "wanna" are removed.  
  
2) Get **replication_word_list_50000(/75000/100000)** and **replication_word_list_for_POS_50000(/75000/100000)** with **replication_word_list_50000(/75000/100000).py**:  
```
python3 replication_word_list_50000.py
python3 replication_word_list_75000.py
python3 replication_word_list_100000.py
```
The obtained **replication_word_list** and **replication_word_list_for_POS** texts will be in **corpora_and_texts_obtained** folder. **replication_word_list** contains the intersection of **OPUS** and **google_25000**. **replication_word_list_for_POS** will be used as input text to obtain POS tags for each word. Compound words like "wanna" are removed.  
  
  
#### Phoneme+Syllable  
1) Get **phoneme_len** list with **phoneme_len.py**: 
```
python3 phoneme_len.py
```
The obtained **phoneme_len** will be in **corpora_and_texts_obtained** folder. The format is: (word + phoneme_length)  
```
			egg	2  
```
2)  Get **syllable_len** list with **syllable_list_len.py**:  
```
python3 syllable_list_len.py
```
The obtained **syllale_list** and **syllable_len** texts will be in **corpora_and_texts_obtained** folder. The format is: (word + syllable_length)  
```
			egg	1  
```
3) Get **pho_syl_word_lists** and **pho_syl_word_list_for_POS** with **pho_syl_len_word_list_and_for_POS.py**: 
```
python3 pho_syl_len_word_list_and_for_POS.py
```
The obtained **pho_syl_len_word_list** and **pho_syl_word_list_for_POS** will be in **corpora_and_texts_obtained** folder. The format for the former file is: (word + phoneme_length + syllable_length).  
```	
			egg	2	1  
```
The latter file will be used as input text to obtain POS tags for each word. Compound words like "wanna" are removed.  

  
#### Google-book    
1) Get **1gm_google_book_sort_OPUS_word_list** with **1gm_google_book_sort_OPUS_word_list.py**(On MIT Openmind the [path] is **/om/data/public/corpora**):  
```
python3 1gm_google_book_sort.py [path]/google-books-v2/eng-us-all/google-books-eng-us-all-20120701-1gram.zs ../corpora_and_texts_obtained/OPUS_word_list  
```  
The obtained **1gm_google_book_sort_OPUS_word_list** containing words that appear in both google-book-ngram corpora and OPUS corpora sorted by words frequency will in **corpora_and_texts_obtained** folder.   
		
3) Get **book_1gm_for_POS** with **book_1gm_and for_POS.py**:
```
python3 book_1gm_for_POS.py
```
The obtained **book_1gm_word_list** and **book_1gm_for_POS** will be in **corpora_and_texts_obtained** folder.

	  
#### POS  
**Run the following command under the master repository**
1) Get **OPUS_POS**, **replciation_POS**, **replication_POS_50000(/75000/100000)**, **pho_syl_POS**, and **book_1gm_POS** with **stanford-postagger.sh**: 
```
cd stanford-postagger-full  

./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger ../corpora_and_texts_obtained/OPUS_word_list_for_POS > ../corpora_and_texts_obtained/OPUS_POS  

./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger ../corpora_and_texts_obtained/replication_word_list_for_POS > ../corpora_and_texts_obtained/replication_POS  
  
./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger ../corpora_and_texts_obtained/replication_word_list_for_POS_50000 > ../corpora_and_texts_obtained/replication_POS_50000

./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger ../corpora_and_texts_obtained/replication_word_list_for_POS_75000 > ../corpora_and_texts_obtained/replication_POS_75000

./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger ../corpora_and_texts_obtained/replication_word_list_for_POS_100000 > ../corpora_and_texts_obtained/replication_POS_100000
  
./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger ../corpora_and_texts_obtained/pho_syl_word_list_for_POS > ../corpora_and_texts_obtained/pho_syl_POS 

./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger ../corpora_and_texts_obtained/book_1gm_for_POS > ../corpora_and_texts_obtained/book_1gm_POS
```
The format for these obtained **replication_POS** and **pho_syl_POS** is:  
```		  
the_DT of_IN and_CC to_TO in_IN for_IN is_VBZ on_IN that_DT 	  
```
2) Get **replication_POS_word_list(\_50000/75000/100000)**, **pho_syl_len_POS_word_list**, and **book_1gm_POS_word_list** with **replication_and_pho_syl_len_POS_word_list.py**:
```
cd ../specification
python3 replication_and_pho_syl_len_POS_word_list.py
```
The obtained **replication_POS_word_list(\_50000/75000/100000)**, **OPUS_POS_word_list** and **book_1gm_POS_word_list** will be in **corpora_and_texts_obtained** folder. The format for **replication_POS_word_list(\_50000/75000/100000)** is: (word + POS)  

```  
			the	DT  
```  

The format for **pho_syl_len_POS_word_list** is: (word + phoneme_length + syllable_length + POS)  

```			  
			the	2	1	DT  
```      
  
### RNN replication:  
**Run the following command under the master repository**
This section is used for RNN replication. 
```
cd RNN
```
#### Basic (character-based word length)  

1) Get **devset** for RNN model with **devset.py**: 
```
python3 devset.py
```
The obtained **devset** text for test will be in **corpora_and_texts_obtained** folder. The size of this file is 60k sentences. The format for devset text is(capitalized word are turned into lower case):   
```			  
			<bos> w1 w2...wn <eos>   
```   
2) Get **devset-result** with **evaluate_target_word_test.py**:  
```
python3 language_models/evaluate_target_word_test.py --checkpoint language_models/hidden650_batch128_dropout0.2_lr20.0.pt --surprisalmode True --data language_models/English --prefixfile ../corpora_and_texts_obtained/devset --outf ../corpora_and_texts_obtained/devset_result  
```  
The obtained **devset_result** text recording surprisal value (infomation value/unpreditability) for each word in each sentence in the devset will be in **corporara_and_texts_obtained** folder. The format is:  
  
	>Peers 19.51535415649414  
	fear 19.504806518554688  
	the 3.9704360961914062  
	judgement 12.45867919921875  
	of 1.8514728546142578  
	their 5.592242240905762  
	peers 5.140864372253418  
	and 3.3437328338623047  
	try 11.75849437713623  
	to 0.21744504570960999  
	talk 10.510600090026855  
	sense 17.938188552856445  
	. 2.074157953262329  
	<eos> -0.0  


3) Get **freq_in_train_set** with **freq_in_train_set.py**(On MIT Openmind the [path] is **/om/data/public/info-len**):  
```  
python3 freq_in_train_set [path]/training-monolingual.tokenized.shuffled  
```  
The obtained **freq_in_train_set** text will be in **corpora_and_texts_obtained** folder.  
  
4) Get **RNN_en_merge_\[size\]**, **RNN_en_merge_\[size\]\_bin_pair.csv**, **RNN_en_merge_\[size\]\_bin_type.csv**, and **RNN_en_merge_\[size\]\_bin_all.csv** with **RNN_merge.py**:  
```		  
python3 RNN_merge.py --language en --size [size]  
```  
Here the size can be any number between 1~60000. The obtained **RNN_en_merge_[size]**, **RNN_en_merge_\[size\]\_bin_pair.csv**, **RNN_en_merge_\[size\]\_bin_type.csv**, and **RNN_en_merge_\[size\]\_bin_all.csv** texts will be in **corpora_and_texts_obtained** folder.  The format for **RNN_en_merge** is: (word + info_int + freq_int + info_float + freq_float + len + cnt + POS + pho + syl + d + p + h + func)  
```  
			and	2	5	2.4042419995623083	5.95369407398674	3	8202697422	CC	3	1	0.552565747871	0.0	0	kstest  
```  
where **info_int** is information value in integer type, **freq_int** is frequency value in integer type, **info_float** is information value in float type, **freq_float** is frequency value in float type, **len** is the orthographic length, **POS** is the part-of-speech tag, **pho** is the phoneme length, **syl** is syllable length, **d** and **p** are D statistic and p-value of normal distribution test on information distribution for each word in all possible contexts. If p<0.05, then **h** is 0, meaning non-normal. Else, **h** is 1, meaning normal. **func** is the specific function used for normal test which varies according to the size of data, i.e., **cnt**. If some value is "-1", then that value is lacked.  
  
5) Plot with plot.Rmd  
Run **RNN replication** section of **plot.Rmd** in R Studio.  
  
#### Phoneme-syllable test:  
1) Plot with plot.Rmd  
Run **phoneme-syllable test** section of **plot.Rmd** in R Studio. The obtained images will be in image folder.  
This is used to see if using phoneme or syllable instead of character to measure word length will make a difference.   
  
#### Gaussian distribution test:  
1) Plot with plot.Rmd  
Run **normal distribution test** section of **plot.Rmd** in R Studio.  
This is used to see if the distribution of information content in different context for each word has influence on word length.  
  
#### POS test:  
1) Plot with plot.Rmd  
Run **POS test** section of **plot.Rmd** in R Studio.  
This is used to see if the POS type for each word has influence on word length.  
  
### Reproduction:
**Run the following command under the master repository**
This section is used for ngram reproduction.
```
cd replication
```
#### Basic test  
1) Get \[n\]gm_en_merge\[\_leaveone\], \[n\]gm_en_merge\[\_leaveone\]\_bin_pair.csv, \[n\]gm_en_merge\[\_leaveone\]\_bin_type.csv,and \[n\]gm_en_merge\[\_leaveone\]\_bin_all.csv with \[n\]gm_merge.py(On MIT Openmind the [path] is **/om/data/public/info-len**):  
```  
python3 2gm_merge.py [path]/google_web_ngrams/data/2gms ../corpora_and_texts_obtained/replication_word_list ../corpora_and_texts_obtained/replication_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True

python3 3gm_merge.py [path]/google_web_ngrams/data/3gms ../corpora_and_texts_obtained/replication_word_list ../corpora_and_texts_obtained/replication_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True

python3 4gm_merge.py [path]/google_web_ngrams/data/4gms ../corpora_and_texts_obtained/replication_word_list ../corpora_and_texts_obtained/replication_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True
```

Remove **--LOO True** if you don't want to use leave-one-out cross validation.'  

2) Plot with plot.Rmd  
Run **reproduction** section of **plot.Rmd** in R Studio.  
  
#### Phoneme-syllable test:  
1) Plot with plot.Rmd  
Run **phoneme-syllable test** section of **plot.Rmd** in R Studio. The obtained images will be in image folder.  
This is used to see if using phoneme or syllable instead of character to measure word length will make a difference.   
  
#### Gaussian distribution test:  
1) Plot with plot.Rmd  
Run **normal distribution test** section of **plot.Rmd** in R Studio.  
This is used to see if the distribution of information content in different context for each word has influence on word length.  
  
#### POS test:  
1) Plot with plot.Rmd  
Run **POS test** section of **plot.Rmd** in R Studio.  
This is used to see if the POS type for each word has influence on word length.  
  
  
### Prerequistes evaluation: 
**Run the following command under the master repository**
This section is used for prerequisites evaluation.
```
cd prerequisites_evaluation
``` 
#### Dataset specification: (frequency clip 50000)  
1) Get [n]gm_en_merge_50000\[\_leaveone\], \[n\]gm_en_merge_50000[\_leaveone]\_bin_pair.csv, [n]gm_en_merge_50000[\_leaveone]\_bin_type.csv,and [n]gm_en_merge_50000[\_leaveone]\_bin_all.csv with [n]gm_merge_50000.py(On MIT Openmind the [path] is **/om/data/public/info-len**):
```  
python3 2gm_merge_50000.py [path]/google_web_ngrams/data/2gms ../corpora_and_texts_obtained/replication_word_list_50000 ../corpora_and_texts_obtained/replication_POS_word_list_50000 ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True

python3 3gm_merge_50000.py [path]/google_web_ngrams/data/3gms ../corpora_and_texts_obtained/replication_word_list_50000 ../corpora_and_texts_obtained/replication_POS_word_list_50000 ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True

python3 4gm_merge_50000.py [path]/google_web_ngrams/data/4gms ../corpora_and_texts_obtained/replication_word_list_50000 ../corpora_and_texts_obtained/replication_POS_word_list_50000 ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True
```
Remove **--LOO True** if you don't want to use leave-one-out cross validation.'  
  
2) Plot with plot.Rmd  
Run **frequency clip evaluation** section of **plot.Rmd** in R Studio. Also replace the cutoff number with different number to see the difference.	  
  
#### Plotting method: (binning)  
1) Plot with plot.Rmd 
Run **errorbar_bin** and **error_int** in each section to see the difference.	  
  
### Gereralization ability test:  
#### Model adaptation (RNN)  
pass  
  
#### Corpora adaptation: (google-book-ngram) 
**Run the following command under the master repository**
This section is used for adaptation evaluation.
```
cd specification
``` 
1) Get [n]gm_en_merge[\_leaveone], [n]gm_en_merge[\_leaveone]\_bin_pair.csv, [n]gm_en_merge[\_leaveone]\_bin_type.csv,and [n]gm_en_merge[\_leaveone]\_bin_all.csv with [n]gm_merge.py(On MIT Openmind the [path] is **/om/data/public/info-len**): 
```
python3 2gm_google_book_merge.py [path]/google-books-v2/eng-us-all/google-books-eng-us-all-20120701-2gram.zs ../corpora_and_texts_obtained/replication_word_list ../corpora_and_texts_obtained/replication_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True

python3 3gm_google_book_merge.py [path]/google-books-v2/eng-us-all/google-books-eng-us-all-20120701-3gram.zs ../corpora_and_texts_obtained/replication_word_list ../corpora_and_texts_obtained/replication_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True

python3 4gm_google_book_merge.py [path]/google-books-v2/eng-us-all/google-books-eng-us-all-20120701-4gram.zs ../corpora_and_texts_obtained/replication_word_list ../corpora_and_texts_obtained/replication_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True
```

The frequency clip specification for this is the most frequent 25000 google-web-ngram words.
		
2) Get [n]gm_book_merge[\_leaveone], [n]gm_book_merge[\_leaveone]\_bin_pair.csv, [n]gm_book_merge[\_leaveone]\_bin_type.csv,and [n]gm_book_merge[\_leaveone]\_bin_all.csv with [n]gm_merge.py(On MIT Openmind the [path] is **/om/data/public/info-len**): 
```
python3 2gm_google_book_merge.py [path]/google-books-v2/eng-us-all/google-books-eng-us-all-20120701-2gram.zs ../corpora_and_texts_obtained/book_1gm_word_list ../corpora_and_texts_obtained/book_1gm_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language book --LOO True

python3 3gm_google_book_merge.py [path]/google-books-v2/eng-us-all/google-books-eng-us-all-20120701-3gram.zs ../corpora_and_texts_obtained/book_1gm_word_list ../corpora_and_texts_obtained/book_1gm_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language book --LOO True

python3 4gm_google_book_merge.py [path]/google-books-v2/eng-us-all/google-books-eng-us-all-20120701-4gram.zs ../corpora_and_texts_obtained/book_1gm_word_list ../corpora_and_texts_obtained/book_1gm_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language book --LOO True
```

The frequency clip specification for this is the most frequent 25000 google-book-ngram words. 
	  
3) Plot with plot.Rmd  
Run **corpora adaptation** section of **plot.Rmd** in R Studio.  
  
#### Multilingual adaptation: (chinese)  
to be done...  
  

