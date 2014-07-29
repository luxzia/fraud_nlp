import pandas as pd
import jsonrpclib
import psycopg2
from simplejson import loads
server = jsonrpclib.Server("http://localhost:8080")
import sys
import parse_doc as ps 
import sql_write as sq  


def store_and_parse(dataframe):

	""" 
	INPUT: dataframe with event id, account type, and description
	OUTPUT: sql inserts into database
	
	This function takes in the dataframe, parses the text data, and stores the 
	dependencies, associated words and their parts of speech into a Postgres 
	database.
	'"""

	conn_string = "dbname='fraud_detection'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

	for i in dataframe.index:
		this_event_id = dataframe.event_id.ix[i]
		this_acct_type = dataframe.acct_type.ix[i]
		document = dataframe.description.ix[i]

		result = []
		# while loop necessary because of the parse server timing out occasionally and needing to be hti again
		while type(result) == list:
			result = loads(server.parse(document))

		sentences = result['sentences']
		print "Length of sentences :: ", len(sentences)

		dependency_list = ps.parse_document(sentences, this_event_id, this_acct_type)
		sq.write_to_sql(dependency_list)






