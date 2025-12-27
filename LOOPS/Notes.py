🔁 Loop kya hota hai?

Loop ka use ek hi kaam ko bar-bar repeat karne ke liye hota hai jab tak condition true ho.
Python me mainly 2 types ke loop hote hain:

• for loop
• while loop

1️⃣ for Loop

🔹 Use kab karte hain?

Jab hume fixed number of times loop chalana ho
List, tuple, string, range par iterate karna ho

🔹 Syntax

for variable in sequence:
    statement
  
✅ Example 1: List ke sath

names = ["Sonu", "Rahul", "Rikesh"]

for name in names:
    print(name)
  
🔹 range() function

range(start, stop, step)
✅ Example

for i in range(2, 11, 2):
    print(i)
📌 Output: 2 4 6 8 10

2️⃣ while Loop
🔹 Use kab karte hain?

Jab tak condition true ho loop chalana ho
Iteration ka exact count pata na ho
🔹 Syntax

while condition:
    statement
  
✅ Example : Simple while

i = 1
while i <= 5:
    print(i)
    i += 1
  
🔹 break (loop tod deta hai)

for i in range(1, 10):
    if i == 5:
        break     # Jab i=5 hoga toh loop bnd ho jayega 
    print(i)
  
🔹 continue (current iteration skip)

for i in range(1, 6):
    if i == 3:
        continue      #i=3 iteration nhi chlega
    print(i)
  
🔹 pass (kuch nahi karta)

for i in range(5):
    pass
  
4️⃣ Nested Loop (Loop ke andar loop)

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
      
5️⃣ Exam ke liye Short Notes 📝
for loop → sequence par iterate karta hai
while loop → condition based loop
break → loop terminate
continue → iteration skip
pass → empty statement
Nested loop → loop ke andar loop

6️⃣ One-line Loop (Extra knowledge 🔥)

for i in range(5): print(i)
