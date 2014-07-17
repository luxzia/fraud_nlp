import re
import pandas as pd 
import string
import psycopg2
import parsing_features as pf 
import os

# def store_dependency_features(document_lst):
#     remove_dash = re.compile(r'-')
#     for i in xrange(len(document_lst)):
#         sentence_id = i
#         sentence_lst = document_lst[i]
#         if sentence_lst:
#             for j in xrange(len(sentence_lst)):
#                 dependency = sentence_lst[j]
#                 relation_search = re.search('[a-z]*.\(', dependency)
#                 if relation_search:
#                     this_relation = relation_search.group()[:-1]
#                 word_1_search = re.search('\(.*[\w].*\,', dependency)
#                 if word_1_search:
#                     this_word_1 = word_1_search.group()[1:-3]
#                     this_word_1 = remove_dash.sub('', this_word_1)
#                 word_2_search = re.search('\s.*[\w]+.*\-', dependency)
#                 if word_2_search:
#                     this_word_2 = word_2_search.group()[1:-1]

#                     conn_string = "dbname='nlp_test'"
#                     conn = psycopg2.connect(conn_string)
#                     cursor = conn.cursor()
#     for i in dataframe.index:
#         description_clean = clean_text(dataframe.description.ix[i])
#         parse_list = parse_file(description_clean)
#         corpus = build_corpus(dataframe['description'].ix[i])
#         account_type = dataframe['binary_acct_type'].ix[i]
#         user_id = dataframe['uid'].ix[i]
#         cursor.execute("INSERT INTO dependencies (acct_type, uid, dependencies, tokens) values (%s, %s, %s, %s)", (account_type, user_id, parse_list, corpus))
#     conn.commit()
                
# write out the code for the SQL inserts

# TURN INTO GET WORDS FUNCTION
def relation_and_words(parse_dependency):
    remove_dash = re.compile(r'-')
    relation_search = re.search('[a-z]*.\(', parse_dependency)
    if relation_search:
        this_relation = relation_search.group()[:-1]
    else:
        this_relation = ""
    word_1_search = re.search('\(.*[\w].*\,', parse_dependency)
    if word_1_search:
        this_word_1 = word_1_search.group()[1:-3]
        this_word_1 = remove_dash.sub('', this_word_1)
    else:
        this_word_1 = ""
    word_2_search = re.search('\s.*[\w]+.*\-', parse_dependency)
    if word_2_search:
        this_word_2 = word_2_search.group()[1:-1]
    else:
        this_word_2 = ""
    return this_relation, this_word_1, this_word_2

def store_dependency_features(dataframe):
    conn_string = "dbname='nlp_test'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    for item in dataframe.index:
        print item
        account_type = dataframe['binary_acct_type'].ix[item]
        user_id = dataframe['uid'].ix[item]
        cursor.execute("INSERT INTO event_info (event_id, acct_type, uid) VALUES (%s, %s, %s)" % (item, account_type, user_id))
        conn.commit()
        description = dataframe['description'].ix[item]
        print type(description)
        doc = pf.clean_text(description)
        dep_list = pf.parse_file(doc)
        for i in xrange(len(dep_list)):
            sentenceid = i
            sentence_lst = dep_list[i]
            if sentence_lst:
                for j in xrange(len(sentence_lst)):
                    dependency = sentence_lst[j]
                    current_relation, current_word_1, current_word_2 = relation_and_words(dependency)
                    print "INSERT INTO dependecy_features (event_id, sentence_id, relation, word_1, word_2) VALUES (%s, %s, '%s', '%s', '%s')" % (item, sentenceid, current_relation, current_word_1, current_word_2)
                    cursor.execute("INSERT INTO dependecy_features (event_id, sentence_id, relation, word_1, word_2) VALUES (%s, %s, '%s', '%s', '%s')" % (item, sentenceid, current_relation, current_word_1, current_word_2))
    conn.commit()

        # call the event_id from the event_info table to store with the dependencies
        #run through the desciption, break into dependencies and then features, 
        # store into dependency table
        # commit to table after each row