
'''🐼Pandas Series :--

Series ek 1-Dimensional (1D) data structure hoti hai
👉 List / array jaisi, lekin index ke saath
Series = Data + Index'''

import pandas as pd

indexs= ["a","b","c","d","e","f"]
a = pd.Series([4,5,6,7,None,8],index=indexs)
'''
🔹 Series ke important properties
Copy code
Python
s.values     # data
s.index      # index
s.dtype      # data type
s.size  '''     # total elements

print(a.values)
print(a.index)
print(a.dtype)
print(a.size)

print(a[:3]) #Slicing
print(a+10) #all values mein 10 add
print(a.isnull()) #Check nul value
print(a.fillna(0)) # feel nul value

#Directory se Series
#📌 Key → Index, Value → Data

data = {"math":90,"english":89,"hindi":99}

b= pd.Series(data)
print(b)
print(b["hindi"]) #99

print(b[:2]) #99