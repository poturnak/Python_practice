#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# Sentiment analysis is often called opinion mining
# It is sub-discipline of a broader NLP (natural language processing) field
# A popular task in sentiment analysis is the doc classification based on the expressed opinion or emotions

# Let's now work with the IMDB database that will let us mine some reviews for moview
# We will import that data into the pandas object

import pyprind
import pandas as pd
import os
import numpy as np

# change the `basepath` to the directory of the
# unzipped movie dataset

basepath = '/Users/nikolay.poturnak/Desktop/MACHINE LEARNING/IMDB dataset/'
#
# labels = {'pos': 1, 'neg': 0}
# pbar = pyprind.ProgBar(50000)
# df = pd.DataFrame()
# for s in ('test', 'train'):
#     for l in ('pos', 'neg'):
#         path = os.path.join(basepath, s, l)
#         for file in os.listdir(path):
#             with open(os.path.join(path, file), 'r', encoding='utf-8') as infile:
#                 txt = infile.read()
#             df = df.append([[txt, labels[l]]], ignore_index=True)
#             pbar.update()
# df.columns = ['review', 'sentiment']
#
# np.random.seed(0)
# df = df.reindex(np.random.permutation(df.index))
# df.to_csv('basepath', index=False)

# df = pd.read_csv(os.path.join(basepath, 'movie_data.csv'))
# print(df.head(3))


# In this part we will learn the bag of words model that will let us represent text as feature vectors
# here is the idea begind bag of words model:
#  - we create the vocabulary of unique tokens, for example words, from the entire set of documents
#  - we construct a feature vector from each document that contains the counts of how often each word occurs
#    in the document

# In scikit learn there is a class CountVectorizer that takes array of text and build the bag of words model for us
# It extracts words from the text (or ngrams), then assigns an integer to each word
# Then after transformation each vector represents the document
# each position in the vector shows if the word is present in the document
# if yes, then the position with the corresponding word index will be marked as 1
# the value in the vector position will show how many times the word occurs in that document

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer()
docs = np.array([
        'The sun is shining',
        'The weather is sweet',
        'The sun is shining, the weather is sweet, and one and one is two'])

bag = count.fit_transform(docs)
print(count.vocabulary_)
print(bag.toarray())

# if we just print the vectorizer it will return the sparse representaiton
# each pair in parenthesis will return the positon where the word is present
# (0,1) means for vector 1, the word in the position 1 is present
# the value associated with the position will tell us how many times the word is seen
print(bag)

# unigram model is when you have one word representing a token
# n-gram model can can have multiple words representing a token

# oftentimes we analyze text and there are words occuring in both positive class and negative class documents
# we need to down-weight those types of words
# for that purpose we will look at tf-idf (term frequency inverse document frequency)

# tf-idf (t,d) = tf(t,d) * idf(t,d)
# idf(t,d) = log(n / (1 + df(d,t)))
#  - t is the term
#  - d is the document
#  - tf - term frequency, how many times word t occures in document d
#  - idf - inverse document frequency
#          n is the total number of documents
#          df(d,t) - number of documents that contain the word t

from sklearn.feature_extraction.text import TfidfTransformer

tfidf = TfidfTransformer(use_idf=True, norm='l2', smooth_idf=True)
np.set_printoptions(precision=2)
print(tfidf.fit_transform(count.fit_transform(docs)).toarray())

# you can get the following insights about tfidf
# if the tfidf values are more or less the same, means the word is noise (occur everywhere + in loger sentences there are more
# occurneces of that word)
# if the values are different for one word across documents, means there is shorter snetence and the number
# of occurences is more or less the same



