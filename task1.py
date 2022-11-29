"""
    Affinity Answers
    Task 1: Calculating the profanity of racism in tweets 
    - By Harsh Khandelwal
"""


import re 
import pandas as pd
import numpy as np
from textblob import TextBlob 
import csv
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords
n_words= set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()


"""
    The Vocab contains all the racial words
    And we can give the weight for individual word
    For the time being all words have same weights
"""

vocab= ["black", "asian", "slaves"]
weights= [1,1,1]


def clean(text):
  """
    Removing links and @tags
    lower case text and replacing '-' and space
    removing stopwords and numbers
    tokenizing words
    stemming words
  """
  text= ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split()) 
  text= text.lower().replace('-', ' ')

  table= str.maketrans('', '', string.punctuation+string.digits)
  text= text.translate(table)

  tokens = word_tokenize(text)

  stemmed = [porter.stem(word) for word in tokens]
  words = [w for w in stemmed if not w in n_words]
  text = ' '.join(words)
  return text 

def text_2_vec(text):
    """
        Create a CountVector for racial words present in vocab
    """

    wordfreq= [text.count(p)*w for p, w in zip(vocab, weights)]
    return wordfreq

def distance(text):
    """
        Calculate the diistance betweeen the  CountVector of text and origin
        large distance implies more racial behaviour
    """

    vector= text_2_vec(text)
    dist = np.linalg.norm(vector)
    return dist

def profanity(data):
    """
        Calculate the profanity for every tweet in data
    """

    data["tweets"] = data["tweets"].apply(clean)
    scores= data["tweets"].apply(distance)
    return scores

data= pd.read_csv("tweets.csv")
data["profanity"] = profanity(data)
data.head()
    
