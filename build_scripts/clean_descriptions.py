import clean_text as ct

def clean_the_data(dataframe):

"""
INPUT: a dataframe with unparsed text in the description field
OUTPUT: a dataframe with cleaned text in the description field
"""

	for i in dataframe.index:
		doc = ct.clean_text(dataframe.description.ix[i])
		dataframe.description.ix[i] = doc
	return dataframe