We first try to replicate the work in [Word lengths are optimized for efficient communication](http://www.pnas.org/content/108/9/3526.short). According to the paper, we calculate the average amount of information conveyed by a particular word w by the following formula:$- \frac{1}{N} \sum_{i=1}^N log(W=w|C=c_i)$ where *$c_i$* is the context for the *i*th occurrence of *w* and *N* is the total frequency of *w* in the corpus. We use three metric to measure the word length: 1) numbers of characters, 2) numbers of phonemes, 3) numbers of syllables within each word. As for frequency, we simply get $$log_2(cnt_w / cnt_total)$$ where *cnt_w* is the count of the target word and *cnt_total* is the size of the corpus in words.

The corporus we use is English google-ngrams corpus which is take as an example among all the languages tested in the paper.

The original specification according to the paper is: 1) the 25,000 most frequent strings in the Google dataset for each language that 2) also occurred in the OpenSubtitles section of the OPUS Corpus. We add another two specifications which are we only consider words: 1)in lower case, 2)alphabetical.

When it comes to plotting, we use two methods of binning: 1) each bin represents 2% of the lexicon; 2) each bin represents lower-boundary integer of the value cluster. Error bars represent SEs.

We also plots spots figure and histogram figure to take a deeper insight in to the relationship between word length and informativeness. The spots figure is mainly used to see the band width of word length for each info/freq bin. The histogram figures are used to check the variance of *p(w|c)* for each word *w* to see if its distribution is Gaussian. Another type of histogram figure is used to examine the relationship among infomation value, frequency value and word length.

We also try to replicate this results with RNN models.

We first used the pre-trained RNN model--"hidden650_batch128_dropout0.2_lr20.0.pt" to compute the information value of each word in a natural corpus--1B Word Benchmark Dataset (https://github.com/ciprian-chelba/1-billion-word-language-modeling-benchmark to get data). The information value is computed according to the formula given in Word lengths are optimized for efficient communication. For the develop set, We extracted 30,000 sentences from the held-out set and computed the infomation value for each word within the dev set.
We also set specification criteria for the words we will finally use to test the relationship between informativeness and word length. That is we only consider words: 1)in lower case, 2)alphabetical, 3)appear more then mini-count times in the test set.


#################

Procdure:
replication:
Get OPUS_word_list with OPUS_word_list.py

Get google_25000 word list with google_25000.py

Get replication_word_list with replication_word_list.py

Get phoneme_len list with phoneme_len.py

Get syllable_len list with syllable_list_len.py

Get pho_syl_word_lists with pho_syl_len_word&for_POS.py

Get replication_POS_word_list and pho_syl_len_POS_word_list with replication&pho_syl_len_POS_word_list.py

Get 2gm_info_freq, 2gm_for_gaussian_test, 2gm_POS_for_gaussian_test, 2gm_POS_info_freq with 2gm_info_freq_and_for_gaussian_test.py (the same with 3gm and 4gm)

Get 2gm_gaussian.csv and 2gm_POS_gaussian.csv with gaussian_test.py (the same with 3gm and 4gm)

Get 2gm_merge with merge.py (the same with 3gm and 4gm)

Get 2gm_merge_bin_pair.csv with csy.py (the same with 3gm and 4gm)


RNN:
Get dev-set for RNN model with devset.py

Get devset-result with evaluate_target_word_test.py

Get freq_in_train_set with freq_in_train_set.py

Get RNN_for_gaussian_test, RNN_POS_for_gaussian_test, RNN_info_freq, RNN_POS_info_freq, and RNN_info_freq_pho_syl with info_freq_and_pho_syl_and_gaussian.py

Get csv files with csv.py

