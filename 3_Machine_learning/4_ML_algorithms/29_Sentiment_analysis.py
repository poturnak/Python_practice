#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

# Sentiment analysis is often called opinion mining
# It is sub-disicpline of a broader NLP (natural language processing) field
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

df = pd.read_csv(os.path.join(basepath, 'movie_data.csv'))
print(df.head(3))