#numpy

import numpy as np
# #we can check if the given array is a numpy array as in a normal list the elements are separated by commas unlike in np arrays
# a=np.array([5,34,67])
# print(a)
# print(type(a))
# #to generate a np array with sequential numbers-->same like range function
# a2=np.arange(1,8,2)
# print(a2)

# b=np.array([[1,4,6,5],[3,8,2,9]])
# #b.size --->it tells the number of elements of the array
# #b.ndim--->it tells the dimensions of the array
# #b.shape--->it tells the number of rows and columns of the array

# #generating a np array and initialiazing with 0's
# a=np.zeros((4,3))#4 rows and three columns
# print(a)
# #initializg with ones
# arr=np.ones((3,5))
# print(arr)
# #creating an empty array with no values
# arr2=np.empty((3,3))
# print(arr2)

###to get the array acc to a certain condition
# a=np.arange(30,100)
# print(a[a>90])


###to use the reshape method of numpy
# a=np.arange(1,25).reshape(3,8)#2d array
# print(a)
# b=np.arange(1,25).reshape(3,4,2)#3d arr it will create three 4x2  2-d matrices 
# print(b)
# c=np.arange(1,25).reshape(4,3,2)#it will create four 3x2  2-d matrices
# print(c)
# d=np.arange(0,16).reshape(2,2,2,2)
# print(d)

###to get the transpose of the matrix
# a=np.arange(1,17).reshape(4,4)
# print(a)
# print(a.T)
# arr=np.arange(1,25).reshape(3,4,2)
# print(arr)
# print(arr.T)

####to convert multidim array into single dimension
# arr=np.arange(1,10).reshape(3,3)
# a=arr.flatten()
# print(a)
# arr=np.arange(1,10).reshape(3,3)
# a=arr.flatten(order='C')#it converts into rowwise 1-D matrix
# b=arr.flatten(order='F')#it converts into columnwise 1-D matrix
# print(a)

# ### to add new row or new column to the previously existing array we use to append funvtion of np
# d=np.array([[4,5,6],[7,8,9]])
# print(d)
# nr_app=np.append(d,[[1,2,3]],axis=0)#axis=0 means row added
# print(nr_app)
# nc_app=np.append(d,[[100],[345]],axis=1)#axis=1 means column added
# print(nc_app)

###to insert a particular position in the matrix we use the insert() method
# a=np.arange(1,10).reshape(3,3)
# new_a=np.insert(a,2,[[19,11,2001]],axis=1)#at row number 3
# new_a2=np.insert(a,2,[[19,11,2001]],axis=0)#at col number 3
# print(a)
# print(new_a)
# print(new_a2)

###to use the split() function from numpy
# a=np.arange(1,25)
# print(a)
# b=np.split(a,3)
# print(b)
# c=np.split(a,4)
# print(c)
# d=np.split(a,8)
# print(d)
# e=np.split(a,6)
# print(e)

# a=np.arange(1,11)
# print(a)
# b=np.split(a,[3,6,8])#it will split after specific positions like after 3 after 6 and after 8
# print(b)

####to split a 2-D array
arr=np.arange(1,17).reshape(4,4)
brr=np.split(arr,2,axis=0)#it splits after the 2nd
brr2=np.split(arr,1,axis=1)
print(arr)
print(brr)
print(brr2)
