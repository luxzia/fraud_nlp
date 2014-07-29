import clean_text as ct  
import parse_and_store as ps 
import word_vectors as wv 
import calculate_score as cs
import pickle
import gensim

description_model = gensim.models.Word2Vec.load('word_model')

"""
INPUT: the raw text to be analyzed
OUTPUT: a string saying whether the text is fraudulent or not
"""

if __name__ = "__main__":

	document = raw_input("enter the document to be analyzed:  ")
	clean_doc = ct.clean_text(document)
	doc_df = ps.store_and_parse(clean_doc)
	features = wv.write_word_vectors(doc_df, description_model) 
	model = pickle.load( open( 'MODEL', 'rb' ) )
	y_pred = model.predict(features)
	scoring_df = cs.scoring_df(doc_df, y_pred)
	cs.calculate_frauds(scoring_df)
