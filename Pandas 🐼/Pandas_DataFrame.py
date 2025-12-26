🐼 Pandas DataFrame (Python)

🔹DataFrame ek 2-Dimensional (rows + columns) data structure hota hai.

👉 Excel sheet / table jaisa hota hai.

DataFrame = Rows + Columns + Index

import pandas as pd

#Directory se
data = {
    "name": ["Sonu Yadav","Rahul Yadav","Rikesh Singh"],
    "marks": [80,90,99],
    "city":["Tamkuhi Road","Jaunpur","Jaipur"]
}

a = pd.DataFrame(data)

print(a)

#List se

list = [
    ["Sonu Yadav",99],
    ["Rahul Yadav", 90],
    ["Rikesh Singh",89]
]

l = pd.DataFrame(list,columns=["Name","Marks"])

print(l)
print(l[:1]) #slicing

'''
🔹 DataFrame dekhne ke functions
Copy code
Python
df.head()      # first 5 rows
df.tail()      # last 5 rows
df.shape       # (rows, columns)
df.columns     # column names
df.info()      # complete info
df.describe()  '''# statistics

path = "/storage/emulated/0/Python_Series/data.csv"
d = pd.read_csv(path)

print(d.head(2))
print(d.tail(2))
print(d.shape)
print(d.info())
print(d.describe())
print(d.columns)
print(d["name"]) #column access
print(d.iloc[2])    #index se access

#🔹 Data filtering (important 🔥)

print(d[d["marks"]>80])

#🔹 New Column Create

d["result"] = ["Pass","Pass","Pass"]
print(d)

'''🔹 Column delete

axis=0 # Row delete
axis=1  # Column delete
inplace=True  # permanent change
inplace=False''' # new DataFrame banega

#d.drop("result",axis=1,inplace=True)
print(d)

#🔹 Row delete

d.drop(1, axis=0, inplace=True)
print(d)

#🔹 Missing values (NaN)

d.isnull()      #check NaN
d.fillna(0)    #Fill NaN value 0
d.dropna()  #NaN delete

#Save all update in file

d.to_csv("/storage/emulated/0/Python_Series/data.csv", index=False) #index=false se index nhi save hoga
print("Update saved in CSV file .")

'''🔹 Extra useful options (knowledge)

df.to_csv("data.csv", sep=";")      # custom separator
df.to_csv("data.csv", header=True) # column names include
df.to_csv("data.csv", encoding="utf-8")
'''

# Series To DataFrame

series= pd.Series([1,2,3,4])

DF= pd.DataFrame(series,columns=["Number"])
print(DF)