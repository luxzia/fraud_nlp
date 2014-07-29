import pandas as pd
import numpy as np
import gensim

def vectorize_words(dataframe, word_model, numpy_array): 

    """
    INPUT: a dataframe with the features to be vectorized and a Word2Vec model 
    OUTPUT: a numpy array with the word vectors 
    """

    for i in dataframe.index:
            this_word_1 = dataframe['word_1'].ix[i]
            this_word_2 = dataframe['word_1'].ix[i]

            if this_word_1 in word_model.vocab:
                numpy_array[i][0:50] = word_model[this_word_1]

            if this_word_2 in word_model.vocab:
               numpy_array[i][50:100] = word_model[this_word_2]
    

def write_word_vectors(dataframe, word_model):

    """
    INPUT: a dataframe with the features to be vectorized and includes
    a dependency relation column, two columns representing words and two representing the part
    of speech tags for the words
    OUTPUT: a numpy array representing the features as a vectorized
    """

    num = len(dataframe)
    features = np.zeros((num, 449))
    features_with_words = vectorize_words(dataframe, word_model, features)

    for i in dataframe.index:
        reln = dataframe['relation_id'].ix[i]
        features_with_words[i][100+reln] = 1

        pos_w1 = dataframe['pos_word_1_id'].ix[i]
        features_with_words[i][364+pos_w1] = 1

        pos_w2 = dataframe['pos_word_2_id'].ix[i]
        features_with_words[i][407+pos_w2] = 1
    
    return features_with_words

