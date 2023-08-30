import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a=[i for i in 'abcdefghijklmno']
data=pd.read_csv(r'E:\AI & ML\Activity-2\income.csv',names=a)
print(data.columns)

#data['a'].value_counts()
data['a'].unique()
#data.isna().sum()

data['b'].value_counts()
data['b'].replace(to_replace=' ?',value=' Private',inplace=True)

data['g'].value_counts()
data['g'].replace(to_replace=' ?',value=' Adm-clerical',inplace=True)

data['n'].value_counts()
data['n'].replace(to_replace=' ?',value=' United-States',inplace=True)

data['x']=np.arange(0,len(data))
s='bdfghijn'
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for i in s:
    data[i+'enc']=le.fit_transform(data[i])

s=data.drop_duplicates('b').set_index('x')
print(s[['b','benc']])
s1=data.drop_duplicates('d').set_index('x')
print(s1[['d','denc']])
s2=data.drop_duplicates('f').set_index('x')
print(s2[['f','fenc']])
s3=data.drop_duplicates('g').set_index('x')
print(s3[['g','genc']])
s4=data.drop_duplicates('h').set_index('x')
print(s4[['h','henc']])
s5=data.drop_duplicates('i').set_index('x')
print(s5[['i','ienc']])
s6=data.drop_duplicates('j').set_index('x')
print(s6[['n','denc']])
s7=data.drop_duplicates('n').set_index('x')
print(s7[['n','nenc']])
print(data.columns)


data.drop([['b', 'd', 'f', 'g', 'h', 'i', 'j', 'n']],axis=1,inplace=True)
x=np.array(data.iloc[:])
y=data.ioc[:,:-1].values
print(x.shape,y.shape)
          

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.001,random_state=12)
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)
model.fit(xtrain,ytrain)


ypred=model.predict(xtest)
from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)