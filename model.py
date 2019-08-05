# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:48:52 2019

@author: Raghavendra J P
"""
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

# load the dataset
dataset = loadtxt('finaltrain.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:21]
y = dataset[:,21]

print(X)
print(y)

# define the keras model
model = Sequential()
model.add(Dense(30, input_dim=21, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(X, y, epochs=200 , batch_size=1000)

# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
predictions = model.predict_classes(X)
# summarize the first 5 cases
for i in range(10):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
    
# evaluate the model
scores = model.evaluate(X, y, verbose=0)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
 
# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
 
# later...

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

dataset = loadtxt('test.csv', delimiter=',')
# split into input (X) and output (y) variables
j = dataset[:,0:21]
# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
predictions = loaded_model.predict_classes(j)
# summarize the first 5 cases
for i in range(10):
	print('%s => %d ' % (j[i].tolist(), predictions[i]))