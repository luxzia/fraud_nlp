import pandas as pd
import numpy as np
import gensim

def write_word_vectors(dataframe, word_model):
        number_to_enter = raw_input("enter the number of rows you want to process: ")
        number_process = int(number_to_enter)
	features = np.zeros((number_process, 101))
	for i in xrange(number_process):
		this_word_1 = dataframe['word_1'].ix[i]
		this_word_2 = dataframe['word_1'].ix[i]
        	if this_word_1 in word_model.vocab:
			features[i][0:50] = word_model[this_word_1]
                        print "foo"
        	if this_word_2 in word_model.vocab:
			features[i][50:100] = word_model[this_word_2]
			print "bar"
		features[i][100] = dataframe.relation_id.ix[i]
	print features
	#return features

# write the size of the vectors as an argument to be passed
# add relation id

                
