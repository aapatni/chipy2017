from sklearn.linear_model import SGDRegressor
from sklearn import preprocessing
import csv

import pandas as pd

def analyze():
    df = pd.read_csv('training.csv')
    x = df.iloc[:,:5].values
    y = df["Direction"].values

    print (type(x),type(y))
    print( y.shape )
    print (x.shape )

    clf = SGDRegressor(max_iter=5000,tol=1e-3)
    print (clf.fit(x,y))
    print (clf.predict([[0,0,0,0,0]]))

