import pandas as pd
import jsonrpclib
import psycopg2
from simplejson import loads
import parse_doc as ps 
import create_dataframe as cd  

server = jsonrpclib.Server("http://localhost:8080")


def store_and_parse(document):

	""" 
	INPUT: dataframe with event id and description
	OUTPUT: sql inserts into database
	
	This function takes in the dataframe, parses the text data, and stores the 
	dependencies, associated words and their parts of speech into a Postgres 
	database.
	'"""

	result = []
	# while loop necessary because of the parse server timing out occasionally and 
	# needing to be hit again
	while type(result) == list:
		result = loads(server.parse(document))
	sentences = result['sentences']
	print "Length of sentences :: ", len(sentences)
	dependencies_list = ps.parse_document(sentences)
	new_frame = cd.store_the_dependencies(dependencies_list)
	return new_frame




