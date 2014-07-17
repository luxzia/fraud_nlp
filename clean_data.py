import os
import pandas as pd
import re
from bs4 import BeautifulSoup
import urllib2
import unicodedata
import string
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import nltk
import psycopg2
import numpy as np  

# read the data into a pandas data frame
X = pd.read_json("/Users/Zipfian/Desktop/train.json")
# take the description column
sentence = X.description.ix[2]
# covert unicode to string
str_sentence = sentence.encode('ascii', 'ignore')

# strip out html tags
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

# OR
def strip_all_tags(html):
    if html is None:
    return None
    return "".join(BeautifulSoup(html).find_all(text=True))

target_sentence = striphtml(str_sentence)

#OR

target_sentence = strip_all_tags(str_sentence)

# remove the rest of the useless bits
remove_junk = re.compile(r'[\n\r\t]')
new_sentence = remove_junk.sub(' ', target_sentence)

def clean_text(series):
    document = series
    string_doc = document.encode('ascii', 'ignore')
    doc_html_free = striphtml(string_doc)
    clean_doc = remove_junk.sub(' ', doc_html_free)
    return clean_doc

# write text to file and parse and write the parse info to file

os.popen("echo '"+new_sentence+"' > ~/stanfordtemp.txt")
os.popen("/usr/local/Cellar/stanford-parser/3.3.1/libexec/lexparser.sh ~/stanfordtemp.txt > ~/newparse.txt")

# open the file to be parsed
parse_file = open("/Users/Zipfian/newparse.txt", 'r+')
parser_out = str(parse_file)



# pull out the collapsed dependencies

parse_file = open("/Users/Zipfian/fraud_nlp/newparse.txt", 'r+')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for parsing the parse file
for line in parse_file:
    if line[0] in alphabet:
        print line[0]

# initialize the stop words
stop_words = stopwords.words('english')
extra_characters = ['!', '@', '#', '$','%', '^', '&', '*', '(', ')', '_', '-', '+' , '=', '[', '{', '}', ']', '|', '\', ''', '"', ':', ';', '<', ',', '.', '>', '?/' , '/']
for i in extra_characters:
    stop_words.append(i)


# build table in sql
CREATE TABLE dependencies ( transaction_id serial PRIMARY KEY, acct_type varchar(40), uid varchar(40), dependencies text, tokens text)

# for each cleaned up file "new_sentence" take out the tokens
words_sentence = [word for word in new_sentence.lower().split() if word not in stop_words]

dependency_list = []
def parse_file(document):
    dependency_list = []
    os.popen("echo '"+document+"' > ~/parsetemp.txt")
    os.popen("/usr/local/Cellar/stanford-parser/3.3.1/libexec/lexparser.sh ~/parsetemp.txt > ~/parsedtext.txt")
    parse_file = open("/Users/Zipfian/parsedtext.txt", 'r+')
    for line in parse_file:
        if line[0] in alphabet:
            dependency_list.append(line)
    return dependency_list

# clean up characters in the words
new_words_sentence = []
for word in words_sentence:
    for i in xrange(0, len(word)):
        if word[i] in extra_characters:
            new_words_sentence.append(word.strip(string.punctuation))

def build_corpus(document):
    cleaned_words = []
    words_sentence = [word for word in document.lower().split() if word not in stop_words]
    for word in words_sentence:
        cleaned_words.append(word.strip(string.punctuation))
    return cleaned_words



# to break into a binary problem
X['binary_acct_type'] = X['acct_type'].apply(lambda x: 1 if x == 'premium' else 0)

# drop rows with no description
X = X[X.body_length != 0]

# split out the premium account info for randomly selecting 1622 
X_premium = X[X.binary_acct_type == 1]
to_choose = np.random.randint(11887, size=1622)
X_premium_sample = X_premium.ix[to_choose]

# split out fraud account set
X_fraud = X[X.binary_acct_type == 0]

# combine the two samples
X_final_pent = X_premium_sample.append(X_fraud)

# chop down to just the desired columns
X_final = X_final_pent[['binary_acct_type', 'uid', 'description']]

#reset index
X_final_reset = X_final.reset_index()
def replace_nas(dataframe):
    for i in dataframe.index:
        if type(dataframe.description.ix[i]) == float:
            dataframe.description.ix[i] = ""

def dependencies_df(dataframe_in, dataframe_out):
    for i in dataframe_in.index:
        dataframe_out['event_id'] = i
        dataframe_out['account_type'] = dataframe_in['binary_acct_type'].ix[i]
        dataframe_out['user_id'] = dataframe_in['uid'].ix[i]
        description_clean = clean_text(dataframe_in.description.ix[i])
        parse_list = parse_file(description_clean)
        dataframe_out['dependency'].ix[i] = parse_list
        corpus = build_corpus(dataframe_in['description'].ix[i])
        dataframe_out['corpus'].ix[i] = corpus 
         

def parse_into_database(dataframe):
    conn_string = "dbname='nlp_project'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    for i in dataframe.index:
        description_clean = clean_text(dataframe.description.ix[i])
        parse_list = parse_file(description_clean)
        corpus = build_corpus(dataframe['description'].ix[i])
        account_type = dataframe['binary_acct_type'].ix[i]
        user_id = dataframe['uid'].ix[i]
        cursor.execute("INSERT INTO dependencies (acct_type, uid, dependencies, tokens) values (%s, %s, %s, %s)", (account_type, user_id, parse_list, corpus))
    conn.commit()




