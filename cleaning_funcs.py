import pandas as pd
import numpy as np
import os
import spacy as sp
import lemminflect

def load_data(file):
    """
    Imports data from a csv file at a relative path.
    """
    dirname = os.path.dirname(os.path.abspath("__file__"))
    filename = os.path.join(dirname, 'data/'+file)
    df = pd.read_csv(filename)
    return df

#function for outputting data to csv
def output_data(df, file):
    """
    Outputs data to a csv file at a relative path.
    """
    dirname = os.path.dirname(os.path.abspath("__file__"))
    filename = os.path.join(dirname, 'data/output/'+file)
    df.to_csv(filename, index=False)
    print('Data output to '+filename)

def text_preprocessing(text):
    """
    Preprocesses text by removing punctuation, lowercasing, and tokenizing.
    
    NOTE: not happy with how the lemmatizer works on adverbs
    """

    nlp = sp.load('en_core_web_sm')

    try:
        if type(text) == list:
            text = join_list(text)

        clean_text = remove_punctuation(text.lower())

        doc = nlp(clean_text)
        # tokens = [token.lemma_ for token in doc if not token.is_stop]
        tokens = [token._.lemma() for token in doc if not token.is_stop]
        return tokens
    except:
        return ''

#function for removing punctuation
def remove_punctuation(text):
    """
    Removes punctuation from text.
    """
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for char in punctuation:
        text = text.replace(char, '')
    return text

#function for joining list of strings
def join_list(list):
    """
    Joins list of strings into a single string.
    """
    return ' '.join(list)