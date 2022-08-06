import pandas as pd
import numpy as np
import os
import spacy as sp

def load_data(file):
    """
    Imports data from a csv file at a relative path.
    """
    dirname = os.path.dirname(os.path.abspath("__file__"))
    filename = os.path.join(dirname, 'data/'+file)
    df = pd.read_csv(filename)
    return df

def text_preprocessing(text):
    """
    Preprocesses text by removing punctuation, lowercasing, and tokenizing.
    """
    nlp = sp.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return tokens