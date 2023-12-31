import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(r"E:\AI & ML\iris.csv")#data collection
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
a=np.arange(1,151)
data['new']=a

data['sw'].fillna(data['sw'].mean(),inplace=True)
data['pl'].fillna(data['pl'].mean(),inplace=True)

x=np.array(data.iloc[: , [0,1,2,3,5]])
y=data.iloc[:,-2].values#before comma it is rows and after the comma it isf or columns

print(x.shape,y.shape)
print(x.ndim)
y.ndim


# #splitting the data into training and testing data
# from sklearn.model_selection import train_test_split
# #size will tell the ratio between the train and test data and random_state will tell the algo that same set of data needs to go for training and testing
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)

# print(xtrain.shape,ytrain.shape)
# print(xtest.shape,ytest.shape)

# #model building
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score as acc
# model=KNeighborsClassifier(n_neighbors=3)#or we can also use "distance=3"
# #if we have NaN(not a Number)values in the dataset we will get value error
# #we cannot make the changes in the target feature as bcoz algo will learn from wrong data
# model.fit(xtrain,ytrain)
# ypred=model.predict(xtest)
# print(acc(ytest,ypred))
# #acc=accuracy(ytest,ypred)


# #making the predictions
# print(model.predict([[5.3,2.8,1.9,0.1],[3.5,2.3,1.2,5.6],[34.6,67.5,32.1,90.3]]))