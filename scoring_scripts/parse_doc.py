import unicodedata

def make_ascii(s):
	"""
	INPUT: unicode string
	OUTPUT: string

	The output from the Stanford Core Parser is unicode and this is 
	written as a quick way to convert the strings to be stored in the 
	database
	"""

	try:
		val = s.encode('ascii', 'ignore')
	except Exception, e:
		print "ERROR :: ", str(e)
		val = s
	return val

def parse_document(sentence_dictionary, event_id):
	"""
	INPUT: dictionary that is output from the Stanford Core Parser using 
	jsonrpclib
	OUTPUT: a list of lists where each sublist represents a dependency and
			contains sentence id, both words in the dependency 
			and their part of speech tags

	This returns the values to be stored in the database
	"""
	dependency_store_list =[]
	for j in xrange(len(sentence_dictionary)):
			dependency_list = []
			dependency_list.append(j)
			dependencies = sentence_dictionary[j]['dependencies']
			word_info = sentence_dictionary[j]['words']
			word_list = []
			for k in xrange(len(word_info)):
				word_list.append(word_info[k][0])
			for l in xrange(len(dependencies)):
				this_relation = make_ascii(dependencies[l][0])
				this_word_1 = make_ascii(dependencies[l][1])
				this_word_2 = make_ascii(dependencies[l][2])
				dependency_list.append(this_relation)
				dependency_list.append(this_word_1)
				dependency_list.append(this_word_2)
				if this_word_1 not in word_list:
					this_pos_word_1 = ""
				else:
					for m in xrange(len(word_list)):
						if this_word_1 == word_list[m]:
							this_pos_word_1 = make_ascii(word_info[m][1]['PartOfSpeech'])
				
				if this_word_2 not in word_list:
					this_pos_word_2 = ""
				else:
					for n in xrange(len(word_list)):
						if this_word_2 == word_list[n]:
							this_pos_word_2 = make_ascii(word_info[n][1]['PartOfSpeech'])
				dependency_list.append(this_pos_word_1)
				dependency_list.append(this_pos_word_2)
				dependency_store_list.append(dependency_list)
	return dependency_store_list