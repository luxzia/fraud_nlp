import pandas as pd 

def store_the_dependencies(dependency_list):

	"""
	INPUT: a list of lists that store the items in each sub list
	OUTPUT: a pandas dataframe with the dependencies stored 

	a function to build the dependencies to be featurized for the scoring
	"""
	
	new_frame = pd.DataFrame()
	for i,row in enumerate(dependency_list):
		new_frame[i] = dependency_list[i]
	column_list = ['sentence_id', 'relation', 'word_1', 'word_2', 'pos_word_1', 'pos_word_2']
	new_frame = new_frame.T 
	new_frame.columns = column_list
	return new_frame		