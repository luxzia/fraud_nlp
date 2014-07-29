import pandas as pd
import jsonrpclib
import psycopg2
from simplejson import loads
import unicodedata
server = jsonrpclib.Server("http://localhost:8080")
import sys

def makeAscii(s):
	try:
		val = s.encode('ascii', 'ignore')
	except Exception, e:
		print "ERROR :: ", str(e)
		val = s
	return val



def store_and_parse(dataframe):
	""" 
	INPUT: dataframe with event id and description
	OUTPUT: sql inserts into database
	
	This function takes in the dataframe, parses the text data, and stores the 
	dependencies, associated words and their parts of speech into a Postgres 
	database.
	'"""
	new_frame = pd.DataFrame(columns = ['event_id', 'sentence_id', 'relation', 'word_1', 'word_2', 'pos_word_1', 'pos_word_2'])
	for i in dataframe.index:
		this_event_id = dataframe.event_id.ix[i]
		document = dataframe.description.ix[i]
		result = []
		# while loop necessary because of the parse server timing out occasionally and needing to be hti again
		while type(result) == list:
			result = loads(server.parse(document))
		sentences = result['sentences']
		print "Length of sentences :: ", len(sentences)
		for j in xrange(len(sentences)):
			dependencies = sentences[j]['dependencies']
			word_info = sentences[j]['words']
			word_list = []
			for k in xrange(len(word_info)):
				word_list.append(word_info[k][0])
			for l in xrange(len(dependencies)):
				this_relation = makeAscii(dependencies[l][0])
				this_word_1 = makeAscii(dependencies[l][1])
				this_word_2 = makeAscii(dependencies[l][2])

				if this_word_1 not in word_list:
					this_pos_word_1 = ""
				else:
					for m in xrange(len(word_list)):
						if this_word_1 == word_list[m]:
							this_pos_word_1 = makeAscii(word_info[m][1]['PartOfSpeech'])
				
				if this_word_2 not in word_list:
					this_pos_word_2 = ""
				else:
					for n in xrange(len(word_list)):
						if this_word_2 == word_list[n]:
							this_pos_word_2 = makeAscii(word_info[n][1]['PartOfSpeech'])
							
				print this_pos_word_1, this_pos_word_2
				try:
					print type(this_relation), type(this_pos_word_1)
					print "sentence id:", j
					new_frame
					### HOW DO I DO A BATCH ADD TO A DATAFRAME???
					data = (this_acct_type, this_event_id, j, this_relation, this_word_1, this_word_2, this_pos_word_1, this_pos_word_2)
					sql_string = "INSERT INTO features (acct_type, event_id, sentence_id, relation, word_1, word_2, pos_word_1, pos_word_2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"                 
				except Exception, e:
					print str(e)
					print "cannot score example"
					sys.exit()
					conn.rollback()
	return new_frame




