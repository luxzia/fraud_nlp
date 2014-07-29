import string
from bs4 import BeautifulSoup 
import unicodedata 
import re


def strip_all_tags(html):
	"""
	INPUT: a document with html in it 
	OUTPUT: a document string with html cleaned out 
	"""

    if html is None:
    	return None
    return "".join(BeautifulSoup(html).find_all(text=True))

# remove newlines, tags, and carriage returns
remove_junk = re.compile(r'[\n\r\t]')

def clean_text(document):
	"""
	INPUT: a document string with unicode, html, and other issues
	OUTPUT: a cleaned document string for parsing
	"""

    string_doc = document.encode('ascii', 'ignore')
    doc_html_free = striphtml(string_doc)
    clean_doc = remove_junk.sub(' ', doc_html_free)
    return clean_doc