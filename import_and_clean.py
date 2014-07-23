import string
from bs4 import BeautifulSoup # is there a way to indicate if it has html?
import unicodedata # check if the string is a string or unicode
import re

# build out a flask app

query = raw_input("enter a string to calcluate chances that it is fraud ")

# function to strip out tags from html
def strip_all_tags(html):
    if html is None:
    return None
    return "".join(BeautifulSoup(html).find_all(text=True))

# remove newlines, tags, and carriage returns
remove_junk = re.compile(r'[\n\r\t]')

# function process data:
# 1 - to change unicode to ascii
# 2 - strip html
# 3 - remove newlines, returns, and tabs
def clean_text(document):
    string_doc = document.encode('ascii', 'ignore')
    doc_html_free = striphtml(string_doc)
    clean_doc = remove_junk.sub(' ', doc_html_free)
    return clean_doc
