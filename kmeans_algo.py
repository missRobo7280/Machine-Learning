import pandas as pd 
df=pd.read_excel(r"E:\AI & ML\Clustering\kmeans1.xlsx")
#print(df.head())


df1=df.drop(["ID Tag","Model"],axis=1)

df1=df1.drop(["Department"],axis=1)

print(df1.head())

from sklearn.cluster import KMeans
km=KMeans(n_clusters=4,init='k-means++',n_init=10)
km.fit(df1)

x=km.fit_predict(df1)
#print(x)

df["cluster"]=x

df1=df.sort_values('cluster')
print(df1)

df1.to_csv("KMeansPredicted2.csv")
