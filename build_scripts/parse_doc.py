import write_dependencies as wd 

def parse_document(sentence_dictionary, event_id, acct_type):

	"""
	INPUT: dictionary that is output from the Stanford Core Parser using 
	jsonrpclib
	OUTPUT: a list of lists where each sublist represents a dependency and
	contains sentence id, both words in the dependency and their part of speech tags

	This returns the values to be stored in the database
	"""

	dependency_store_list =[]
	for j in xrange(len(sentence_dictionary)):
			dependency_list = []
			sentence_id = j 
			dependencies = sentence_dictionary[j]['dependencies']

			word_info = sentence_dictionary[j]['words']
			word_list = []

			for k in xrange(len(word_info)):
				word_list.append(word_info[k][0])

			dependency_list = wd.parse_dependencies(dependencies, event_id, acct_type, sentence_id, word_list)
			dependency_store_list.append(dependency_list)

	return dependency_store_list