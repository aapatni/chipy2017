from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import SGDRegressor
from sklearn import preprocessing
import csv

import pandas as pd

df = pd.read_csv('training.csv')
x = df.iloc[:,:5].values
y = df["Direction"].values

print (type(x),type(y))
print( y.shape )
print (x.shape )

clf = SGDRegressor(max_iter=500,tol=1e-3)
print (clf.fit(x,y))
print (clf.predict([[200,130,290,540,10]]))

