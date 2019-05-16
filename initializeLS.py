# -*- coding: utf-8 -*-
"""meowLS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bc7GAqq50ZsW_8zQQ8PNje1wJoIodFcS
"""
import time
import pyphen
from .Features.WikiFrequency import *
from .Features.Ngram import *
from .Features.Word2Vec import *
start = time.time()
dic = pyphen.Pyphen(lang='en')
import pickle
import os

DIRECTORY = os.path.dirname(__file__) + '/files/'
######## General Functions ############
def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

class Initializer:
    def __init__(self):
        print("Inside class")
        lexicons = {}
        with open(DIRECTORY + "lexicon.tsv") as f:
            for line in f:
                (key, val) = line.split()
                lexicons[key.lower()] = val
        self.subs_rank_nnclf = load_obj(DIRECTORY + 'subs_ranking_model_3')
        self.substitutions_db = load_obj(DIRECTORY + "substitutions")
        self.fivegram_model = NgramModel(DIRECTORY + "newsela.lm", 2, 2)
        self.threegram_model = NgramModel(DIRECTORY + "newsela.lm", 1, 1)
        self.syllable_dict = pyphen.Pyphen(lang='en')
        self.wiki_frequency = WikiFrequency()
        # self.word2vec = Word2Vec()
        elapsed_time = time.time() - start
        print("loaded models in ", elapsed_time)



"""**Model**"""

from sklearn.preprocessing import maxabs_scale
import re
