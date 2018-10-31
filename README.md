### Introduction  

This work aims to replicate the work in [Word lengths are optimized for efficient communication](http://www.pnas.org/content/108/9/3526.short), in which it is proved that word length has a higher corraletion with the average amount of information conveyed by a particular word **w** than with the frequency of **w**, which challenges the authority of Zipf's law. '  
  
According to that paper, the information value is calculated by the following formula:  
  
<a href="https://www.codecogs.com/eqnedit.php?latex=$$-&space;\frac{1}{N}&space;\sum_{i=1}^N&space;logP(W=w|C=c_i)$&space;$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$-&space;\frac{1}{N}&space;\sum_{i=1}^N&space;logP(W=w|C=c_i)$&space;$" title="$$- \frac{1}{N} \sum_{i=1}^N logP(W=w|C=c_i)$ $" /></a>  
  
where **<a href="https://www.codecogs.com/eqnedit.php?latex=$c_i$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$c_i$" title="$c_i$" /></a>** is the context for the **<a href="https://www.codecogs.com/eqnedit.php?latex=$i$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$i$" title="$i$" /></a>**th occurrence of **<a href="https://www.codecogs.com/eqnedit.php?latex=$w$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$w$" title="$w$" /></a>** and **<a href="https://www.codecogs.com/eqnedit.php?latex=$N$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$N$" title="$N$" /></a>** is the total frequency of **<a href="https://www.codecogs.com/eqnedit.php?latex=$w$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$w$" title="$w$" /></a>** in the corpus.  
  
The frequency value is the negative log unigram probability for **w**.  
  
The word length is the orthographic length of **w**.  
  
As for plotting method: x-axis represents parallel information value and frequency value; y-axis represents word length. Error bars represent SEs and each bin represents 2% of the lexicon.  
  
The paper also presents partial correlations: frequency and length partialing out information content; information content and length partialing out frequency.   
  
 
  
### Procedure  
In this section we presents the usage of codes for this work.  
  
#### Specification word lists:  
This section is used for preparing the word lists for the replication. We suggest you skip this section and start from the next section to directly see the replication results. All the word lists can be downloaded from Google Drive. You can download that folder to replace the **corpora_and_texts_obtained** folder.

##### OPUS  
1) Download OPUS OpenSubtitle corpus for English. (This file is already saved as **OpenSubtitles.bg-en.en** in **corpora_and_texts_obtained** folder.)   
	  
2) Get OPUS_word_list and OPUS_word_list_for_POS with OPUS_word_list.py:  
		Run **OPUS_word_list.py** under **specification** folder. The obtained **OPUS_word_list** and **OPUS_word_list_for_POS** texts will be in **corpora_and_texts_obtained** folder. The former file contains words that exist in OPUS OpenSubtitle corpora. The latter file will be used as input text to obtain POS tags for each word. Compound words like "wanna" are removed.		  
  
##### Google  
1) Download google-web-ngram corpora and extract the file documenting unigrams according to their frequency. (This file is already saved as **vocab_cs** in **corpora_and_texts_obtained** folder.)  
	  
2) Get google_25000 word list with google_25000.py:  
		Run **google_25000.py** under **specification** folder. The obtained **google_25000** text will be in **corpora_and_texts_obtained** folder. This file contains 25000 most frequent words in google dataset.  
  
	3) Get google_50000 word list with google_50000.py:  
		Run **google_50000.py** under **specification** folder. The obtained **google_50000** text will be in **corpora_and_texts_obtained** folder. This file contains the 25001~50000 most frequent words in google dataset.  
  
##### OPUS+Google  

1) Get replication_word_list and replication_word_list_for_POS with replication_word_list.py:  
		Run **replication_word_list.py** under **specification** folder. The obtained **replication_word_list** and **replication_word_list_for_POS** texts will be in **corpora_and_texts_obtained** folder. **replication_word_list** contains the intersection of **OPUS** and **google_25000**. **replication_word_list_for_POS** will be used as input text to obtain POS tags for each word. Compound words like "wanna" are removed.  
  
2) Get replication_word_list_50000(/75000/100000) and replication_word_list_for_POS_50000(/75000/100000) with replication_word_list_50000(/75000/100000).py:  
		Run **replication_word_list_50000(/75000/100000).py** under **specification** folder. The obtained **replication_word_list** and **replication_word_list_for_POS** texts will be in **corpora_and_texts_obtained** folder. **replication_word_list** contains the intersection of **OPUS** and **google_25000**. **replication_word_list_for_POS** will be used as input text to obtain POS tags for each word. Compound words like "wanna" are removed.  
  
  
##### Phoneme+Syllable  
1) Download phoneme list from http://www.speech.cs.cmu.edu/cgi-bin/cmudict. (This file is already saved as **phoneme_list** in **corpora_and_texts_obtained** folder.)  
	  
2) Get phoneme_len list with phoneme_len.py:  
		Run **phoneme_len.py** under **specification** folder. The obtained **phoneme_len** will be in **corpora_and_texts_obtained** folder. The format is: (word + phoneme_length)  
```
			egg	2  
```
3) Download CELEX corpora and extract **epl.cd** file from it. (This file is already saved in **corpora_and_texts_obtained** folder.)  
	  
4) Get syllable_len list with syllable_list_len.py:  
		Run **syllable_list_len.py** under **specification** folder. The obtained **syllale_list** and **syllable_len** texts will be in **corpora_and_texts_obtained** folder. The format is: (word + syllable_length)  
```
			egg	1  
```
5) Get pho_syl_word_lists and pho_syl_word_list_for_POS with pho_syl_len_word_list_and_for_POS.py:  
		Run **pho_syl_len_word_list_and_for_POS.py** under **specification** folder. The obtained **pho_syl_len_word_list** and **pho_syl_word_list_for_POS** will be in **corpora_and_texts_obtained** folder. The format for the former file is: (word + phoneme_length + syllable_length).  
```	
			egg	2	1  
```

The latter file will be used as input text to obtain POS tags for each word. Compound words like "wanna" are removed.  
	  
##### POS  
1) Get replciation_POS and pho_syl_POS with stanford-postagger.sh  
		Download staford-postagger-full and save it in \[path1\]. Assume the **corpora_and_texts_obtained** folder is in \[path2\]. (Here the \[path1\] and \[path2\] on Openmind are both: **/om/data/public/info-len**.)  
		Run following command to get **replication_POS** and **pho_syl_POS** text which contains tags for each word in these word lists:  
```
			cd [path1]/stanford-postagger-full  
			  
			./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger [path2]/corpora_and_texts_obtained/OPUS_word_list_for_POS > [path2]/corpora_and_texts_obtained/OPUS_POS  
  
			./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger [path2]/corpora_and_texts_obtained/replication_word_list_for_POS > [path2]/corpora_and_texts_obtained/replication_POS  
  
			./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger [path2]/corpora_and_texts_obtained/replication_word_list_for_POS_50000(/75000/100000) > [path2]/corpora_and_texts_obtained/replication_POS_50000(/75000/100000)  
  
			./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger [path2]/corpora_and_texts_obtained/pho_syl_word_list_for_POS > [path2]/corpora_and_texts_obtained/pho_syl_POS  
```
The format for these obtained files is:  
```			  
			the_DT of_IN and_CC to_TO in_IN for_IN is_VBZ on_IN that_DT  
```	  
2) Get replication_POS_word_list(\_50000/75000/100000), replication_POS_word_list(\_50000/75000/100000), and pho_syl_len_POS_word_list with replication_and_pho_syl_len_POS_word_list.py  
		Run **replication_and_pho_syl_len_POS_word_list.py** under **specification** folder. The obtained **replication_POS_word_list(\_50000/75000/100000)**, and **pho_syl_len_POS_word_list** will be in **corpora_and_texts_obtained** folder. The format for **replication_POS_word_list(\_50000/75000/100000)** is: (word + POS)  
```  
			the	DT  
```  
The format for **pho_syl_len_POS_word_list** is: (word + phoneme_length + syllable_length + POS)  
```			  
			the	2	1	DT  
```  
3) Get OPUS_POS_word_listi with OPUS_POS_word_list.py	  
		Run **OPUS_POS_word_list.py** under **specification** folder.  
  
##### Google-book  
1) Download **google-book-v2** corpora and save it in \[path\] (Here on Openmind the \[path\] is **/om/data/public/corpora/**).  
  
2) Get 1gm_google_book_sort_OPUS_word_list with 1gm_google_book_sort_OPUS_word_list.py  
		Run **1gm_google_book_sort_OPUS_word_list.py** under **specification** folder with following command:  
```
			python3 1gm_google_book_sort.py [path]/google-books-v2/eng-us-all/google-books-eng-us-all-20120701-1gram.zs ../corpora_and_texts_obtained/OPUS_word_list  
```  
		The obtained **1gm_google_book_sort_OPUS_word_list** containing words that appear in both google-book-ngram corpora and OPUS corpora sorted by words frequency will in **corpora_and_texts_obtained** folder.   
		
3) Get book_1gm_for_POS with book_1gm_and for_POS.py
		Run  **book_1gm_for_POS.py** under **specification** folder. The obtained **book_1gm_word_list** and **book_1gm_for_POS** will be in **corpora_and_texts_obtained** folder.

4) Get book_1gm_POS with stanford-postagger.sh
		Run following command to get **replication_POS** and **pho_syl_POS** text which contains tags for each word in these word lists:  
```  
			cd [path1]/stanford-postagger-full  
			  
			./stanford-postagger.sh models/wsj-0-18-left3words-distsim.tagger [path2]/corpora_and_texts_obtained/book_1gm_for_POS > [path2]/corpora_and_texts_obtained/book_1gm_POS
```			

  
	  
  
#### RNN replication:  
##### basic (character-based word length)  
1) Get devset for RNN model with devset.py:  
		Run **devset.py** under **RNN** folder. The obtained **devset** text for test will be in **corpora_and_texts_obtained** folder. The size of this file is 60k sentences. The format for devset text is(capitalized word are turned into lower case):   
```			  
			<bos> w1 w2...wn <eos>   
```   
2) Get devset-result with evaluate_target_word_test.py:  
		Run evaluate_target_word_test.py under **RNN** folder with command:  
```
			 python3 language_models/evaluate_target_word_test.py --checkpoint language_models/hidden650_batch128_dropout0.2_lr20.0.pt --surprisalmode True --data language_models/English --prefixfile ../corpora_and_texts_obtained/devset --outf ../corpora_and_texts_obtained/devset_result  
```  
		The obtained **devset_result** text recording surprisal value (infomation value/unpreditability) for each word in each sentence in the devset will be in **corporara_and_texts_obtained** folder. The format is:  
```  
			Peers 19.51535415649414  
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
```	  
3) Get freq_in_train_set with freq_in_train_set.py:  
		Download 1T-benchmark corpora in \[path\] (Here the \[path\] on Openmind is **/om/data/public/info-len/1-billion-word-language-modeling-benchmark-r13output**). It should contain training-monolingual.tokenized.shuffled and heldout-monolingual.tokenized.shuffled.  
		Run **freq_in_train_set.py** under **RNN** folder with command:  
```  
			python3 freq_in_train_set [path]/training-monolingual.tokenized.shuffled  
```  
		The obtained **freq_in_train_set** text will be in **corpora_and_texts_obtained** folder.  
  
4) Get RNN_en_merge_\[size\], RNN_en_merge_\[size\]\_bin_pair.csv, RNN_en_merge_\[size\]\_bin_type.csv, and RNN_en_merge_\[size\]\_bin_all.csv with RNN_merge.py  
		Run **RNN_merge.py** under **RNN** folder with following command:  
```		  
			python3 RNN_merge.py --language en --size [size]  
```  
		Here the size can be any number between 1~60000. The obtained **RNN_en_merge_[size]**, **RNN_en_merge_\[size\]\_bin_pair.csv**, **RNN_en_merge_\[size\]\_bin_type.csv**, and **RNN_en_merge_\[size\]\_bin_all.csv** texts will be in **corpora_and_texts_obtained** folder.  The format for **RNN_en_merge** is: (word + info_int + freq_int + info_float + freq_float + len + cnt + POS + pho + syl + d + p + h + func)  
```  
			and	2	5	2.4042419995623083	5.95369407398674	3	8202697422	CC	3	1	0.552565747871	0.0	0	kstest  
```  
		where **info_int** is information value in integer type, **freq_int** is frequency value in integer type, **info_float** is information value in float type, **freq_float** is frequency value in float type, **len** is the orthographic length, **POS** is the part-of-speech tag, **pho** is the phoneme length, **syl** is syllable length, **d** and **p** are D statistic and p-value of normal distribution test on information distribution for each word in all possible contexts. If p<0.05, then **h** is 0, meaning non-normal. Else, **h** is 1, meaning normal. **func** is the specific function used for normal test which varies according to the size of data, i.e., **cnt**. If some value is "-1", then that value is lacked.  
  
5) Plot with plot.Rmd  
		Download **corpora_and_texts_obtained** folder onto your own computer. Save in \[path\]. Run **RNN replication** section of **plot.Rmd** in R Studio.  
  
##### phoneme-syllable test:  
1) Plot with plot.Rmd  
		Run **phoneme-syllable test** section of **plot.Rmd** in R Studio. The obtained images will be in image folder.  
			This is used to see if using phoneme or syllable instead of character to measure word length will make a difference.   
  
##### gaussian distribution test:  
1) Plot with plot.Rmd  
		Run **normal distribution test** section of **plot.Rmd** in R Studio.  
			This is used to see if the distribution of information content in different context for each word has influence on word length.  
  
##### POS test:  
1) Plot with plot.Rmd  
		Run **POS test** section of **plot.Rmd** in R Studio.  
			This is used to see if the POS type for each word has influence on word length.  
  
#### reproduction:  
##### basic test  
1) Get \[n\]gm_en_merge\[\_leaveone\], \[n\]gm_en_merge\[\_leaveone\]\_bin_pair.csv, \[n\]gm_en_merge\[\_leaveone\]\_bin_type.csv,and \[n\]gm_en_merge\[\_leaveone\]\_bin_all.csv with \[n\]gm_merge.py:  
Download **google-web-ngrams** corpora and save it in \[path\] (Here on Openmind the \[path\] is **/om/data/public/corpora**).   
Run **[n]gm_merge.py** under **replication** folder with command: (n = 2/3/4)  
```  
			python3 [n]gm_merge.py [path]/google_web_ngrams/data/[n]gms ../corpora_and_texts_obtained/replication_word_list ../corpora_and_texts_obtained/replication_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True   
```			  
Remove **--LOO True** if you don't want to use leave-one-out cross validation.'  

2) Plot with plot.Rmd  
		Run **reproduction** section of **plot.Rmd** in R Studio.  
  
##### phoneme-syllable test:  
1) Plot with plot.Rmd  
		Run **phoneme-syllable test** section of **plot.Rmd** in R Studio. The obtained images will be in image folder.  
			This is used to see if using phoneme or syllable instead of character to measure word length will make a difference.   
  
##### gaussian distribution test:  
1) Plot with plot.Rmd  
		Run **normal distribution test** section of **plot.Rmd** in R Studio.  
			This is used to see if the distribution of information content in different context for each word has influence on word length.  
  
##### POS test:  
1) Plot with plot.Rmd  
		Run **POS test** section of **plot.Rmd** in R Studio.  
			This is used to see if the POS type for each word has influence on word length.  
  
  
#### prerequistes evaluation:  
##### dataset specification: (frequency clip 50000)  
1) Get [n]gm_en_merge_50000\[\_leaveone\], \[n\]gm_en_merge_50000[\_leaveone]\_bin_pair.csv, [n]gm_en_merge_50000[\_leaveone]\_bin_type.csv,and [n]gm_en_merge_50000[\_leaveone]\_bin_all.csv with [n]gm_merge_50000.py:  
		**google-web-ngrams** corpora is in \[path\] (Here on Openmind the [path] is **/om/data/public/corpora**).   
		Run **[n]gm_merge_50000.py** under **prerequisites_evaluation** folder with command: (n = 2/3/4)  
```  
			python3 [n]gm_merge_50000.py [path]/google_web_ngrams/data/[n]gms ../corpora_and_texts_obtained/replication_word_list_50000 ../corpora_and_texts_obtained/replication_POS_word_list_50000 ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True   
```		  
		Remove **--LOO True** if you don't want to use leave-one-out cross validation.'  
  
2) Plot with plot.Rmd  
		Run **frequency clip evaluation** section of **plot.Rmd** in R Studio. Also replace the cutoff number with different number to see the difference.	  
  
##### plottinging method: (binning)  
1) Plot with plot.Rmd  
		Run **errorbar_bin** and **error_int** in each section to see the difference.	  
  
#### gereralization ability test:  
##### model adaptation (RNN)  
	pass  
  
##### corpora adaptation: (google-book-ngram)  
1) Get [n]gm_en_merge[\_leaveone], [n]gm_en_merge[\_leaveone]\_bin_pair.csv, [n]gm_en_merge[\_leaveone]\_bin_type.csv,and [n]gm_en_merge[\_leaveone]\_bin_all.csv with [n]gm_merge.py:  
		Download **google-book-v2** corpora and save it in \[path\] (Here on Openmind the [path] is **/om/data/public/corpora/**).   
  		Run **[n]gm_google_book_merge.py** under **replication** folder with command: (n = 2/3/4)  
```
			python3 [n]gm_google_book_merge.py [path]/google-books-v2/eng-us-all/google-books-eng-us-all-20120701-[n]gram.zs ../corpora_and_texts_obtained/replication_word_list ../corpora_and_texts_obtained/replication_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language en --LOO True
```		
	The frequency clip specification for this is the most frequent 25000 google-web-ngram words.
		
2) Get [n]gm_book_merge[\_leaveone], [n]gm_book_merge[\_leaveone]\_bin_pair.csv, [n]gm_book_merge[\_leaveone]\_bin_type.csv,and [n]gm_book_merge[\_leaveone]\_bin_all.csv with [n]gm_merge.py:  
  	Run **[n]gm_google_book_merge.py** under **replication** folder with command: (n = 2/3/4)  
```
			python3 [n]gm_google_book_merge.py [path]/google-books-v2/eng-us-all/google-books-eng-us-all-20120701-2gram.zs ../corpora_and_texts_obtained/book_1gm_word_list ../corpora_and_texts_obtained/book_1gm_POS_word_list ../corpora_and_texts_obtained/pho_syl_len_word_list --language book --LOO True
```	  
	 The frequency clip specification for this is the most frequent 25000 google-book-ngram words. 
	  
3) Plot with plot.Rmd  
		Run **corpora adaptation** section of **plot.Rmd** in R Studio.  
  
##### multilingual adaptation: (chinese)  
to be done...  
  

