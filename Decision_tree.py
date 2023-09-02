#Decision tree
#it is best suited for the dataset that contains categorical values
#it is a white box algo....we get to know the backend process
#it cannot be used for large dataset it may lead to overfitting
# 1. Information gain:it means how mauch impact has the feature on the  target feature      Data with high                    
#2.Gini index:it determines the impurity in the data,the data with low Gini Index is more suitable
#by default decision tree takes the gini index
#for using the informtion gain we need to mention criterion ="entropy"

import pandas as pd 
import numpy as np

data=pd.read_csv(r'E:\AI & ML\fires.csv')

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
(xtrain,xtest,ytrain,ytest)=train_test_split(x,y,test_size=0.125,random_state=12)
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion="gini")
model.fit(xtrain,ytrain)


ypred=model.predict(xtest)
from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)

#accuracy with entropy=87.5
#accracy with gini =81.25s