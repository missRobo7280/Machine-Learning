import pandas as pd 
import numpy as np


data=pd.read_csv(r"E:\AI & ML\iris.csv")

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.4,random_state=45)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
model=LogisticRegression()
model.fit(xtrain,ytrain)
y_pred = model.predict(xtest)
acc = accuracy_score(ytest, y_pred)
print(acc)


import matplotlib.pyplot as plt
plt.scatter(xtest, ytest, color='blue', label='Actual')
plt.plot(xtest, y_pred, color='aqua', label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()
