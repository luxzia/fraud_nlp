import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine

# create database connection
engine = create_engine('postgresql://Zipfian@localhost/nlp_test')

# open dependency table into dataframe
 dependency_df = pd.read_sql_table('dependecy_features', engine)

# open event info table into dataframe
event_df = pd.read_sql_table('event_info', engine)

# merge the two dataframes
 combi_df = pd.merge(event_df, dependency_df, on='event_id')

# drop dummy table
combi_df = combi_df.drop('num_relations', 1) # should remove from sql

# create relations list
relations = list(combi_df['relation'].unique())

# create dictionary for mapping relations to ids
relation_dict = {}
for i, reln in enumerate(relations):
    relation_dict[reln] = i

# create relation_id column 
combi_df['relation_id'] = combi_df['relation'].map(relation_dict)

# create empty columns for word2vec values
for i in xrange(100):
    combi_df[i] = combi_df.apply(lambda _: '', axis = 1)

# the values for word_1
for i in combi_df2['word_1'].index:
	try:
		new_array = description_model[combi_df2['word_1'].ix[i]]
		for j in xrange(len(new_array)):
			print new_array
			combi_df2[j].ix[i] = new_array[j]
	except KeyError:
		for j in xrange(50):
			combi_df2[j].ix[i] = 0
