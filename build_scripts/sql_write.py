import psycopg2

def write_to_sql(dependency_lst_of_lists):
	"""
	INPUT: a list of lists where each sublist contains an event id, a sentence id, a dependency
	relation, the two related words and their respective parts of speech
	OUTPUT: writes to a postgres database
	"""

	conn_string = "dbname='fraud_detection'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

	for lst in dependency_lst_of_lists:
		this_event_id = lst[0]
		this_acct_type = lst[1]
		this_sentence_id = lst[2]
		this_word_1 = lst[3]
		this_word_2 = lst[4]
		this_pos_word_1 = lst[5]
		this_pos_word_2 = lst[6]

		data = (this_acct_type, this_event_id, this_sentence_id, this_relation, this_word_1, this_word_2, this_pos_word_1, this_pos_word_2)
		sql_string = "INSERT INTO features (acct_type, event_id, sentence_id, relation, word_1, word_2, pos_word_1, pos_word_2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
		cursor.execute(data, sql_string)
		conn.commit()