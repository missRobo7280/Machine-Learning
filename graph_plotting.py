# import matplotlib.pyplot as plt
# v=[3,4,5,2]
# c=[2,4,1,5,]
# d=[1,4,3,5]
# #line plot
# plt.plot(v,c,c='orange',linewidth=4,linestyle="dashed",marker='*',mfc='b',mec='b',label='voltage')
# plt.plot(v,d,c='yellow',linewidth=4,linestyle="dashed",marker='o',mfc='r',mec='r',label='current')
# plt.show()


#scatterplot
#plt.scatter(v,c,marker='+')


#barplot
import matplotlib.pyplot as plt
v=[3,4,7,5]
c=[1,2,3,4]
s=['2020','2021','2022','2023']
plt.bar(c,v,tick_label=s)
plt.show()


###subplots
##import matplotlib.pyplot as plt
##v=[3,4,5,2]
##c=[2,4,1,5]
##d=[4,1,2,5]
##plt.subplot(2,1,1)
##plt.plot(v,c,c='g')
##plt.subplot(2,1,2)
##plt.plot(v,c,c='r')
##plt.show()


#piechart
# import matplotlib.pyplot as plt
# a=[5,2,3,6]
# col=['blue','yellow','pink','orange']
# s=['python','c','java','cpp']
# plt.pie(a,colors=col,labels=s,startangle=90,explode=(0.1,0,0,0),autopct='%1.2f')
# plt.legend()
# #plt.savefig(r'E:\html files\images\graph.jpg')
# plt.show()
