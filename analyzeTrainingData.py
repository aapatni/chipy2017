from sklearn.neural_network import MLPClassifier
import csv

x=[[]]
y=[]
with open('training.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=' ')
    for row in reader:
        x.append([row[0],row[1],row[2],row[3],row[4]])
        y.append(row[5])
print x
print y
clf = MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(5,1),random_state=1) #solver could also equal 'adam', or 'sgd'
#try this maybe?
#clf = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
print (clf.fit(x,y))
