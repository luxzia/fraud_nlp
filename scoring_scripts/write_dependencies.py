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

def parse_dependencies(dependency_list_of_lists, relation_list, sentence_id):

	"""
	INPUT: (1) a list of lists. Each sublist contains a triple with a dependency relation and the 
	two related words (2) a list that is appended to 
	OUTPUT: a list of lists.  Each sublist will contain the relation, the two related words
	and their respective parts of speech
	"""

	dependency_list = []
	for i in xrange(len(dependency_list_of_lists)):
				this_relation = make_ascii(dependency_list_of_lists[i][0])
				this_word_1 = make_ascii(dependency_list_of_lists[i][1])
				this_word_2 = make_ascii(dependency_list_of_lists[i][2])
				
				dependency_list.append(this_relation)
				dependency_list.append(this_word_1)
				dependency_list.append(this_word_2)

				if this_word_1 not in word_list:
					this_pos_word_1 = ""
				else:
					for m in xrange(len(word_list)):
						if this_word_1 == word_list[m]:
							this_pos_word_1 = make_ascii(word_info[m][1]['PartOfSpeech'])
				
				dependency_list.append(this_pos_word_1)

				if this_word_2 not in word_list:
					this_pos_word_2 = ""
				else:
					for n in xrange(len(word_list)):
						if this_word_2 == word_list[n]:
							this_pos_word_2 = make_ascii(word_info[n][1]['PartOfSpeech'])

				dependency_list.append(this_pos_word_2)
	return dependency_list 