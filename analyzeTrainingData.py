from sklearn.neural_network import MLPClassifier
import csv

x=[[]]
y=[]
with open('training.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=' ')
    for row in reader:
        print(row)
        x.append([row[0],row[1],row[2],row[3],row[4]])
        y.append(row[5])
clf = MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(15,),random_state=1)
print (clf.fit(x,y))
