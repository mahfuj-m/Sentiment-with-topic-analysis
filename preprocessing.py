import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet

def shuffle_dataset(dataframe):
    return dataframe.sample(frac=1).reset_index(drop=True)

def text_processing(words):
    
    words=words.lower()
    # Removing special charaters
    words=re.sub(r'[^a-zA-Z0-9\s]',"",words)
    #Removing stopwords
    stops=set(stopwords.words('english'))
    filter_words=[word for word in words.split(" ") if word not in stops]
    words=" ".join(filter_words)
    
    # Removing the rest numbers
    words=re.sub(r'[^a-zA-Z\s]',"",words)
    return nltk.word_tokenize(words)