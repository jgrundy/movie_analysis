import pandas as pd
import numpy as np
import os
import spacy as sp

def load_data(file):
    dirname = os.path.dirname(os.path.abspath("__file__"))
    filename = os.path.join(dirname, 'data/'+file)
    df = pd.read_csv(filename)
    return df

