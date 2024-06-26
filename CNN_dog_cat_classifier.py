# I mainly used Jupyter Notebook to execute this code.
# I have provided comments before every block of code if you want to use jupyter notebook too.

# dataset url : https://drive.google.com/drive/u/0/folders/1dZvL1gi5QLwOGrfdn9XEsi4EnXx535bD
# you all must download these 4 csv files as dataset and then save them to the working directory to train the model.

# block 1 

import numpy as np
import random
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten

# block 2

X_train = np.loadtxt('input.csv', delimiter = ',') # dataset input.csv
Y_train = np.loadtxt('labels.csv', delimiter = ',') # dataset labels.cvs

X_test = np.loadtxt('input_test.csv', delimiter = ',') # datasets input_test.csv
Y_test = np.loadtxt('labels_test.csv', delimiter = ',') # datasets labels_test.csv

# block 3

X_train = X_train.reshape(len(X_train), 100, 100, 3)
Y_train = Y_train.reshape(len(Y_train), 1)

X_test = X_test.reshape(len(X_test), 100, 100, 3)
Y_test = Y_test.reshape(len(Y_test), 1)

X_train = X_train/255.0
X_test = X_test/255.0

# block 4

print("Shape of X_train: ", X_train.shape)
print("Shape of Y_train: ", Y_train.shape)
print("Shape of X_test: ", X_test.shape)
print("Shape of Y_test: ", Y_test.shape)

# block 5

idx = random.randint(0, len(X_train))
plt.imshow(X_train[idx, :])
plt.show()

# block 6

model = Sequential([
    Conv2D(32, (3,3), activation = 'relu', input_shape = (100, 100, 3)),
    MaxPooling2D((2,2)),
    
    Conv2D(32, (3,3), activation = 'relu'),
    MaxPooling2D((2,2)),
    
    Flatten(),
    Dense(64, activation = 'relu'),
    Dense(1, activation = 'sigmoid')
])

# block 7 

model = Sequential()

model.add(Conv2D(32, (3,3), activation = 'relu', input_shape = (100, 100, 3)))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(32, (3,3), activation = 'relu'))
model.add(MaxPooling2D((2,2)))

model.add(Flatten())
model.add(Dense(64, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

# block 8

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# block 9

model.fit(X_train, Y_train, epochs = 5, batch_size = 64)

# block 10

model.evaluate(X_test, Y_test)

# block 11

idx2 = random.randint(0, len(Y_test))
plt.imshow(X_test[idx2, :])
plt.show()

y_pred = model.predict(X_test[idx2, :].reshape(1, 100, 100, 3))
y_pred = y_pred > 0.5

if(y_pred == 0):
    pred = 'dog'
else:
    pred = 'cat'
    
print("Our model says it is a :", pred)