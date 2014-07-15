import os
import pandas as pd
import re
from bs4 import BeautifulSoup
import urllib2
import unicodedata
import string

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

# write text to file and parse and write the parse info to file

os.popen("echo '"+new_sentence+"' > ~/stanfordtemp.txt")
os.popen("/usr/local/Cellar/stanford-parser/3.3.1/libexec/lexparser.sh ~/stanfordtemp.txt > ~/newparse.txt")

# open the file to be parsed
parse_file = open("/Users/Zipfian/newparse.txt", 'r+')
parser_out = str(parse_file)

# pull out the collapsed dependencies

parse_file = open("/Users/Zipfian/newparse.txt", 'r+')
alphabet = ['abcdefghijklmnopqrstuvwxyz']