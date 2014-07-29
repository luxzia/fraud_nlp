import pandas as pd
import numpy as np
import gensim
from sklearn.preprocessing import StandardScaler

def write_word_vectors(dataframe, word_model):
        number_to_enter = raw_input("enter the number of rows you want to process: ")
        number_process = int(number_to_enter)
        features = np.zeros((number_process, 449))
        for i in xrange(number_process):
            this_word_1 = dataframe['word_1'].ix[i]
            this_word_2 = dataframe['word_1'].ix[i]
            if this_word_1 in word_model.vocab:
                features[i][0:50] = word_model[this_word_1]
                print "foo"
            if this_word_2 in word_model.vocab:
               features[i][50:100] = word_model[this_word_2]
               print "bar"
            reln = dataframe['relation-id'].ix[i]
            features[i][100+reln] = 1
            pos_w1 = dataframe['pos_word_1_id'].ix[i]
            features[i][364+pos_w1] = 1
            pos_w2 = dataframe['pos_word_2_id'].ix[i]
            features[i][407+pos_w2] = 1
        return features

def scale_features(feature_vector):
    f_scaled_ = StandardScaler().fit(feature_vector)
    features_scaled = f_scaled_.transform(feature_vector)
    return features_scaled