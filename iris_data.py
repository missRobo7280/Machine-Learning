import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\Swati\OneDrive\Desktop\AI & ML\iris.csv")#data collection
# data.shape
# data
# data.isna()
# data.isna().sum()
# data.describe()
# #correlation matrix 
# # #correlation:the strength of association between the features
# print(data.iloc[:,:-1].corr())
# #plotting the correlation matrix
# a=data.iloc[:,:-1].corr()
# plt.matshow(a)
# plt.colorbar()#to add the color bar on the side
# plt.show()

# #dividing the data into independent and dependent features
# #we need to give the algorithm the data in the form of a matrix or array only
# #x=data.iloc[ : , : -1]  it is dataframe
# #y=data.iloc[: , -1] it is also a dataframe
# #two methods for conversion to array---> np.array() or .values
x=np.array(data.iloc[: , :-1])
y=data.iloc[:,-1].values
print(x.shape,y.shape)
print(x.ndim)
y.ndim


#splitting the data into training and testing data
from sklearn.model_selection import train_test_split
#size will tell the ratio between the train and test data and random_state will tell the algo that same set of data needs to go for training and testing
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)

print(xtrain.shape,ytrain.shape)
print(xtest.shape,ytest.shape)

#model building
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)
model.fit(xtrain,ytrain)
ypred=model.predict(xtest)
#print(accuracy_score(ytest,ypred))
acc=accuracy(ytest,ypred)
