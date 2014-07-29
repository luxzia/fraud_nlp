import pandas as pd
import numpy as np


def build_score_df(dataframe, array):

	"""
	INPUT:  dataframe with sentence_ids, numpy array with predicted scores
	OUTPUT: dataframe with sentence_ids and scores

	a function that builds a dataframe to pass to the fraud calculation
	function
	"""

	scoring_df = dataframe.sentence_id
	scoring_df['y_pred'] = y_pred.T
	return scoring_df
		
def calculate_fraud( dataframe ):
	
	""" 
	INPUT: 	a dataframe with the score per dependency predicted by the model and a sentence id 
	for the dependency
	OUTPUT: prediction

	a function for calculating account type based on sentence-level prediction
    """

	mean_frame = dataframe.groupby(['sentence_id']).aggregate(np.mean)
	for j in in mean_frame.index:
		if mean_frame.y_pred.ix[j] < 0.75:
			print "fraudulent"
		


	

	