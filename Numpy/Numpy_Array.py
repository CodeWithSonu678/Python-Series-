import numpy as np


#1️⃣Numpy Array

a = np.array([1,2,3,4]) #1D

b= np.array([[1,2],[3,4]]) #2D
'''
2️⃣Array properties

ndim → dimension
shape → rows, columns
size → total elements
dtype → data type
'''
print(a.ndim,a.shape,a.dtype,a.size)

#Output :-- 1 (4,) int64 4

#3️⃣ Special Arrays

# zeros() :- All Zero
c=np.zeros((3,4))
print(c.ndim)

#Output :-- 2

#ones() :- All one 
d= np.ones((3,4))
print(d,d.ndim,d.shape,d.size)

#Output :-- [[1. 1. 1. 1.][1. 1. 1. 1.][1. 1. 1. 1.]] 2 (3, 4) 12

'''
•arange(start, stop, num)

Start :-Yaha se start hoga
Stop :- stop include nhi hoga
num :- itne ke gap par hoga '''

e = np.arange(5,100,5) 
print(e)

#Output :-- [ 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95]

'''
•linspace(start, stop, num)

Start :-Yaha se start hoga
Stop :- stop bhu include hoga
num :- itne ke gap = (stop - start) / (num - 1) par hoga'''

f= np.linspace(1,10,3)
print(f)

#Output :-- [ 1.   5.5 10. ]