Pandas kya hai?

Pandas Python ki data analysis & data handling library hai.
Iska use table-type data (Excel, CSV, database) ko easily handle karne ke liye hota hai.
👉 NumPy array ke upar bana hai, lekin zyada powerful hai data ke liye.


Pandas mainly kis ke liye?

📊 Data analysis
📁 CSV / Excel file read–write
🔍 Data filtering & searching
🔄 Data cleaning (missing values)
📈 Reports & statistics

Pandas ke 2 main data structures

1️⃣ Series
1-D data (list jaisa)

import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)

📌 Use: single column data

2️⃣ DataFrame

2-D table (rows + columns)

data = {
    "Name": ["Sonu", "Amit", "Ravi"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
print(df)

📌 Use: Excel / table type data