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

# read data into pandas data frame
X = pd.read_json("/Users/Zipfian/Desktop/train.json")

# function to remove html tags
def strip_all_tags(html):
    if html is None:
        return None
    return "".join(BeautifulSoup(html).find_all(text=True))

# to remove newlines, tabs
remove_junk = re.compile(r'[\n\r\t]')

# a function to clean the text
def clean_text(series):
    document = series
    string_doc = document.encode('ascii', 'ignore')
    doc_html_free = strip_all_tags(string_doc)
    clean_doc = remove_junk.sub(' ', doc_html_free)
    return clean_doc

# a dataframe to test store the dependency features into
# features_df = pd.DataFrame( np.zeros( 0, dtype=[ ('event_id', 'int64'), ('sentence_id','int64'), ('relation', 'str'), ('word1','str'), ('word2', 'str') ]))


# parse_file = open("/Users/Zipfian/newparse.txt", 'r+')

# to build out the dependencies by sentence

def parse_file(document):
    document_list = []
    os.popen("echo '"+document+"' > ~/parsetemp.txt")
    os.popen("/usr/local/Cellar/stanford-parser/3.3.1/libexec/lexparser.sh ~/parsetemp.txt > ~/parsedtext.txt")
    parse_file = open("/Users/Zipfian/parsedtext.txt", 'r+')
    sentence_list = []
    for line in parse_file:
        if line[0] in string.lowercase:
            sentence_list.append(line)
    else:
        if sentence_list:
            document_list.append(sentence_list)
            sentence_list = []
    return document_list






