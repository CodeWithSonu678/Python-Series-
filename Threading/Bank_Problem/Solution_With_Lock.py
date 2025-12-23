🔐 Lock (Thread Synchronization)
Lock ek synchronization mechanism hai jo shared data ko protect karta hai.
Lock ka use karke ek time pe sirf ek thread critical section ko access kar sakta hai, jisse race condition avoid hoti hai.
👉 Python me threading.Lock() ka use hota hai.
Syntax :-
lock = threading.Lock()
with lock:
    # critical section

##Start Program
import threading  #library for thread 
import time            #library for tiem

balance = 1000

lock = threading.Lock() #lock kar diya 

def withdraw(amount):
    global balance
    with lock:                      #ek time par keval ek thread chlega 
        temp = balance
        time.sleep(1)
        balance = temp - amount
    
        print("After withdraw balance :- ",balance)


t1 = threading.Thread(target=withdraw, args=(500,))
t2 = threading.Thread(target=withdraw, args=(500,))
    
#Start thread
t1.start()
t2.start()

#Stop main thread 
t1.join()
t2.join()

print("Final balance :- ",balance)

