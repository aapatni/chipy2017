from sklearn.neural_network import MLPClassifier
import csv

x=[[]]
y=[]
with open('training.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=' ')
    for row in reader:
        x.append([row[0],row[1],row[2],row[3],row[4]])
        y.append(row[5])
clf = MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(5,2),random_state=1) #solver could also equal 'adam', or 'sgd'
print (clf.fit(x,y))
