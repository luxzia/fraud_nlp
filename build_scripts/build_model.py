import pandas as pd
import clean_descriptions as cd
import store_and_parse_build as sp  
from sqlalchemy import engine
from pandas.io import read_sql
import pandas as pd
import vectorize_features as vf  
import gensim
from sklearn import grid_search
import pickle

description_model = gensim.models.Word2Vec.load('word_model')

"""
This assumes that the data will be given with an id, account type and a description only
so that the dataframe will have an "event_id" column, an "acct_type" column and a "description"
column
"""

if __name__ = "__main__":
	prelim_df = pd.read_json('data.json')
	clean_df = cd.clean_the_data(prelim_df)
	sp.store_and_parse(clean_df)

	engine = create_engine('postgresql://postgres@localhost/fraud_detection')
	dependency_df = pd.read_sql_table('dependency_features', engine)

	features = vf.vectorize_features(dependency_df)
	y_train = dependency_df['acct_type']
	y_train = y_train.values
	clf = grid_search.GridSearchCV(cv=None,                                
       estimator=LogisticRegression(C=1.0, intercept_scaling=1, dual=False, fit_intercept=True,
          penalty='l1', tol=0.0001),
       param_grid={'C': [0.001, 0.01, 0.1, 1, 10, 50, 100, 1000]})
	model = clf.fit(features, y_train)

	with open('lr_model.pkl','w') as f:
  		pickle.dump(model,f) 






