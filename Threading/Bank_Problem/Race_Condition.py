⚠️ Race Condition kya hoti hai?
Jab multiple threads ek hi data ko same time pe access / modify karte hain
aur final result galat aa jata hai → use Race Condition kehte hain.
👉 “Kaun pehle chalega” isi race ki wajah se problem hoti hai.


import threading  #This is lib for thread 
import time

balance = 1000
def withdraw(amount):
    global balance
    temp = balance
    time.sleep(1)
    balance = temp - amount
    
    print("After withdraw balance :- ",balance)


t1 = threading.Thread(target=withdraw, args=(500,))
t2 = threading.Thread(target=withdraw, args=(500,))
    
#Start thread
t1.start()
t2.start()

#Main thread ko bolta h ki phle ess thread ko complete ho jane doo 
t1.join()
t2.join()

print("Final balance :- ",balance)


OUTPUT:--

After withdraw balance :-  500
After withdraw balance :-  500
Final balance :-  500 # This is wrong answer. 

[Program finished]
