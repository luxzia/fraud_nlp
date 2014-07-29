import pandas as pd
import numpy as np

""" A function for calculating account type based on sentence-level prediction.
    Takes a dataframe with columns event_id, sentence_id, and acct_type_pred"""
def build_score_df(dataframe, array):
	""" INPUT: dataframe with sentence_ids, numpy array with predicted scores
		OUTPUT: dataframe with sentence_ids and scores
		a function that builds a dataframe to pass to the fraud calculation
		function
	"""
	scoring_df = dataframe.sentence_id
	scoring_df['y_pred'] = y_pred.T
	return scoring_df
	
def calculate_fraud( dataframe ):
	event_pred_dict = {}
	for i in dataframe.index:
		if i not in event_ids:
			pass
		else:
			new_frame = dataframe[ dataframe.event_id == i ]
			new_frame = score_frame.reset_index( drop=True )
			mean_frame = new_frame.groupby(['sentence_id']).aggregate(np.mean)
			event_pred_dict[i] = []
			for j in in mean_frame.index:
				if mean_frame.y_pred.ix[j] < 0.75:
					event_pred_dict[i].append( "possibly fradulent ")
	return event_pred_dict

	