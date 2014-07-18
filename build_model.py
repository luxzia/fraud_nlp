from sklearn import metrics
from sklearn.decomposition import NMF
from gensim.models.ldamodel import LdaModel
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import psycopg2

# get a small selection of data from the database

conn_string = "dbname='nlp_test'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

