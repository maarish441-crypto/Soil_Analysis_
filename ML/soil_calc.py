

import pandas as pd
import numpy as np
import pickle

def predictI(data):
    with open('ALGO.pkl','rb') as f:
        model = pickle.load(f)
        var = model.predict(data)
        return var
    