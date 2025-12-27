🧵 String kya hoti hai?

String characters ka collection hota hai jo quotes (" " / ' ') ke andar likha jata hai.

name = "Sonu"
city = 'Delhi'

✔ Python mein string immutable hoti hai (matlab ek baar banne ke baad change nahi hoti)

🔹 String banane ke tareeke

a = "Hello"
b = 'Hello'
c = """Hello World"""

🔹 String Indexing

Index 0 se start hota hai

s = "Python"
print(s[0])   # P
print(s[3])   # h
print(s[-1])  # n

🔹 String Slicing

s = "Python"
print(s[0:4])   # Pyth
print(s[2:])    # thon
print(s[:3])    # Pyt
print(s[::2])   # Pto

🔹 String Immutable hoti hai

❌ Ye galat hai:

s = "Hello"
s[0] = 'h'   # Error

✔ Sahi tareeka:

s = "Hello"
s = "h" + s[1:]
print(s)

🔹 String Concatenation

a = "Hello"
b = "World"
print(a + " " + b)

🔹 String Repetition

print("Hi " * 3) #3 time Hi

🔹 len() function

name = "Sonu"
print(len(name))  # 4

🔥 Important String Methods (EXAM IMPORTANT)
🔹 Case Conversion

s = "Python"
print(s.upper())   # PYTHON
print(s.lower())   # python
print(s.title())   # Python
print(s.capitalize())

🔹 Checking Methods

s = "hello123"

print(s.islower())
print(s.isupper())
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())

🔹 Searching Methods

s = "I love Python"

print(s.find("Python"))
print(s.index("love"))
print("Java" in s)

🔹 Replace & Split

s = "Hello World"
print(s.replace("World", "Python"))

s2 = "a,b,c"
print(s2.split(","))

🔹 Join

words = ["I", "Love", "Python"]
print(" ".join(words))

🔹 Strip (spaces hatane ke liye)

s = "  Hello  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

🔹 String Formatting

1️⃣ f-string (BEST & LATEST)

name = "Sonu"
age = 20
print(f"My name is {name} and age is {age}")

2️⃣ format()

print("My name is {} and age is {}".format(name, age))

3️⃣ % formatting

print("My name is %s" % name)

🔹 Escape Characters

print("Hello\nWorld")
print("Hello\tWorld")
print("He said \"Python\"")

🔹 String Loop

s = "Sonu"
for ch in s:
    print(ch)
  
🔹 String Comparison

a = "abc"
b = "ABC"
print(a == b)
print(a.lower() == b.lower())
