#The Language of Fraud

###Required technologies for this product:

####NLP
* [**Stanford Core Parser**](http://nlp.stanford.edu/software/corenlp.shtml)
* [**Word2Vec**](https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=word2vec%20gensim%20tutorial)
* [**CoreNLP**](https://pypi.python.org/pypi/corenlp-python)

####Python libraries
* Pandas
* Gensim
* Scikit-learn
* Numpy

####Database
* Postgres

The inspiration for this project comes from an in-class case study we did on fraud detection.  Bag of words approaches and text length in text that appeared in one field per event seemed to show some promise for fraud detection.  As a formally-trained linguist, I wanted to use some more advanced NLP technqiues.  The Stanford Core Parser provides an excellent wealth of linguistic information on a piece of text, including dependencies and part-of-speech tags.  The Word2Vec modeling takes a corpus as input and returns each word within that corpus as a vector.

This project is meant as a proof of concept model, not a working application.  




