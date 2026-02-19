🔹 Exception kya hai?
Runtime error jo program chalne ke time aata hai.

Example: invalid input, divide by zero.

🔹 Exception Handling kya hai?
Errors ko handle karna taaki program crash na ho.

🔹 Basic Syntax

try:
    risky code
except ErrorType:
    handle error

🔹 Example

try:
    num = int(input())
except ValueError:
    print("Invalid input")

🔹 Multiple Exceptions

try:
    result = 10 / num
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

🔹 else Block
Error nahi → else run.

try:
    num = int(input())
except ValueError:
    print("Error")
else:
    print("Valid")

🔹 finally Block
Hamesha run hota hai.

finally:
    print("Done")

🔹 Common Exceptions
•ValueError
•ZeroDivisionError
•IndexError
•KeyError
•FileNotFoundError

🔹 raise keyword
Manual error throw karne ke liye.

raise ValueError("Wrong value")

🔹 Best Use
✔ User input validation
✔ File handling
✔ Safe programs

🧠 One-line exam definition
Exception Handling: Runtime errors ko handle karne ka mechanism using try-except.