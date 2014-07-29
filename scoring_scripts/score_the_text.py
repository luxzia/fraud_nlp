import DOC WITH CLEAN_TEXT
import DOC WITH STORE AND PARSE
import WORD_VECTORS
import calculate_score as cs
import pickle
import gensim

description_model = gensim.models.Word2Vec.load('word_model')

if __name__ = "__main__"
	document = raw_input("enter the document to be analyzed:  ")
	clean_doc = ??.clean_text(document)
	??.store_and_parse( document, description_model ) --> (1) dataframe with event_id, sentence_id, relation, word_1, word_2, pos_word_1, pos_word_2, acct_type
	??.vectorize --> feature matrix with binarized relation, pos_word_1, pos_word_2, word vectors
	model = pickle.load( open( 'MODEL', 'rb' ) )
	model.predict(features) --> y_pred
	create scoring dataframe with y_pred
	cs.calculate_frauds(y_pred)
