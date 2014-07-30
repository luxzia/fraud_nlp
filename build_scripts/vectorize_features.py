
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def vectorize_words(dataframe, word_model, feature_array): 

    """
    INPUT: a dataframe with the features to be vectorized and a Word2Vec model 
    OUTPUT: a two-dimensional numpy array with the word vectors 
    """

    for i in dataframe.index:
        this_word_1 = dataframe['word_1'].ix[i]
        this_word_2 = dataframe['word_1'].ix[i]

        if this_word_1 in word_model.vocab:
            feature_array[i][0:50] = word_model[this_word_1]

        if this_word_2 in word_model.vocab:
            feature_array[i][50:100] = word_model[this_word_2]
    return feature_array

def build_id_column(dataframe, dataframe_column, dictionary, name):
	
	"""
	INPUT: a dataframe with the features, a dictionary for writing a column for changing
	categorical data from strings to numerical data, the column to enumerate, and the name of
	the new column 
	OUTPUT: dataframe with original columns and id columns added
	"""

	for i, cat in enumerate(dataframe_column):
		dictionary[cat] = i

	dataframe['name'] == dataframe.column.map(dictionary)
	return dataframe, len(dictionary)

def vectorize_features(dataframe, word_model):

	"""
	INPUT: a dataframe with the features to vectorize, and a Word2Vec model that contains
	the words as vectors  
	OUTPUT: two-dimensional numpy array that is a feature matrix
	"""

	num = len(dataframe)

	relation_dict = {}
	dataframe_1, rel_num = build_id_column(dataframe, dataframe.relation, relation_dict, 'relation')
		
	pos_word_1_dict = {}
	dataframe_2, pos_word_1_num = build_id_column(dataframe_1, dataframe_1.pos_word_1, pos_word_1_dict, 'pos_word_1_id')

	pos_word_2_dict = {}
	dataframe_3, pos_word_2_num = build_id_column(dataframe_2, dataframe_2.pos_word_2, pos_word_2_dict, 'pos_word_2_id')

	extra_vector_size = rel_num + pos_word_1_num + pos_word_2_num

	features_pre = np.zeros((num, 100 + extra_vector_size))

	features_with_words = vectorize_words(dataframe_3, word_model, features_pre)

	for i in dataframe.index:
        reln = dataframe['relation_id'].ix[i]
        features_with_words[i][100+rel_num] = 1

        pos_w1 = dataframe['pos_word_1_id'].ix[i]
        features_with_words[i][100+rel_num+pos_word_1_num] = 1

        pos_w2 = dataframe['pos_word_2_id'].ix[i]
        features_with_words[i][100+rel_num+pos_word_1_num+pos_word_2_num] = 1

    return features_with_words

def scale_features(feature_matrix):
    	
   	"""
    INPUT: a two-dimensional numpy array that is the feature matrix
    OUTPUT: a two-dimensional numpy array with the features scaled
    """

    features_fit = StandardScaler().fit(feature_matrix)
    features_scaled = features_fit.transform(feature_matrix)
    return features_scaled

    