st = "python is cool language"

new = st[::-1].upper() //reverse && upper case 
print(f" reverse = {new}")

y="    Hey Sonu Bro "
a =y.strip() //space remove 
print(a)

re= y.replace("Sonu","Rikesh") //replace 
print(re)

sp = y.split() //words mein todna
print(sp)

j = " ".join(sp) //space add Kiya 

print(j)

print(y.isalnum()) //check 


'''Program 
user se input lekar count && reverse print '''

sentance = input("Enter your sentence :- ")

words = sentance.split()

print(f"count = {len(words)}")

reverse = sentance[::-1]

print(f" reverse = {reverse}")