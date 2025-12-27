🔷 Conditional Statements in Python

👉 Conditional statements ka use program mein decision lene ke liye hota hai.
Matlab: condition true ho → ek kaam, false ho → dusra kaam

🔹 Important Points (Exam Ready)
✔ Python mein indentation compulsory hai
✔ { } use nahi hota
✔ Conditions hamesha boolean (True / False) hoti hain
✔ elif unlimited use ho sakta hai

1️⃣ if Statement
🔹 Syntax

if condition:
  statement

🔹Example
age = 20
if age>18:
  print("You are young man")

•Explain
° Agar condition True hogi tabhi code block chlega
° Agar False hui toh kuch bhi execute nhi hoga

2️⃣ if–else Statement
🔹 Syntax

if condition:
    statement1
else:
    statement2
  
🔹 Example
num = 5

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
  
🔹 Explanation
Condition true → if block
Condition false → else block

3️⃣ if–elif–else Statement
🔹 Syntax
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3
  
🔹 Example
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
  
🔹 Explanation
Multiple conditions check kar sakte hain
Pehli true condition ka block execute hota hai

4️⃣ Nested if Statement
👉 if ke andar if
🔹 Example
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Age below 18")
  
5️⃣ Comparison Operators (Conditions mein use hote hain)
Operator        Meaning
==              Equal
!=              Not equal
>               Greater than
<               Less than
>=              Greater or equal
<=              Less or equal
  
6️⃣ Logical Operators
Operator        Use
and             Dono condition true
or              Koi ek condition true
not             Condition ka ulta
  
🔹 Example
age = 22
citizen = True

if age >= 18 and citizen:
    print("Eligible for voting")
       
7️⃣ Short Hand if (One-line if)
🔹 Example
a = 10
b = 5
if a > b: print("a is greater")
  
8️⃣ Ternary Conditional Operator
🔹 Syntax
value_if_true if condition else value_if_false
  
🔹 Example
a = 10
b = 20

print("a is greater") if a > b else print("b is greater")
