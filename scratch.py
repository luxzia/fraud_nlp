# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

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
import numpy as np

# <codecell>

X = pd.read_json("/Users/Zipfian/Desktop/train.json")

# <codecell>

X.columns

# <codecell>

X.body_length.head(5)

# <codecell>

foo1 = X.description.ix[0]

# <codecell>

len(foo1)

# <codecell>

X.acct_type.value_counts()

# <codecell>

X['binary_acct_type'] = X['acct_type'].apply(lambda x: 1 if x == 'premium' else 0)
        

# <codecell>

X.acct_type.head()

# <codecell>


# <codecell>

X.binary_acct_type.value_counts()

# <codecell>

X.body_length.value_counts()

# <codecell>

print (X.body_length != 0).any(axis=0)

# <codecell>

X = X[X.body_length != 0]

# <codecell>

X.binary_acct_type.value_counts()

# <codecell>

X_premium = X[X.binary_acct_type == 1]

# <codecell>

X_fraud = X[X.binary_acct_type == 0]

# <codecell>

X_premium.shape

# <codecell>

to_choose = np.random.randint(11887, size=1622)
print to_choose
X_premium_sample = X_premium.ix[to_choose]

# <codecell>

X_final_pent = X_premium_sample.append(X_fraud)

# <codecell>

X_final = X_final_pent[['binary_acct_type', 'uid', 'description']]

# <codecell>

for i in X_final.index:
    print X_final['binary_acct_type'].ix[i]

# <codecell>


# <codecell>


