#for outliers in data we use the feature_scaling method in which we convert the data in a particular column into a range of values
#there are two methods:1.Normalization        2. Standardization
#in Normalization we have MinMaxScaler in which we transform the values in a range of 0 to 1.
#formula=(x-min)/(max-min)
#in  standardization we have standard StandardScaler
#formula=(x-mean)/standard deviation
#mean is nothing but the average and standard deviation is the variation from the mean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a=[i for i in 'abcdefghijklmnop']
data=pd.read_excel(r"E:\AI & ML\credit_loan.xlsx",names=a)
print(data.columns)


print(data.shape)
#print(data)
print(data.head())

print(data.isna().sum())


data['b'].value_counts()
data['b'].replace(to_replace='?',value= 14.00,inplace=True)
data['n'].replace(to_replace='?',value= 12.00,inplace=True)


s='adefgijlm'
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in s:
    data[i]=le.fit_transform(data[i])

x=np.array(data.iloc[ : , :-1])##[0,1,2,3,5]])
y=data.iloc[ : ,-1].values
print(x.shape,y.shape)

##feature scaling
from sklearn.preprocessing import StandardScaler
scaled=StandardScaler()
scaledx=scaled.fit_transform(x)


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(scaledx,y,test_size=0.23,random_state=1)

print(xtrain.shape,ytrain.shape)
print(xtest.shape,ytest.shape)


from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)
model.fit(xtrain,ytrain)
ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)

#without feature_scaling
#accuracy=65.40880503144653
#with normalization
#accuracy=88.67924528301887
#with standardization
#87.42138364779875