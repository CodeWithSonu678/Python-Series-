import threading  #This is lib for thread 
import time

def func(sec):
    print(f"Thread is running for {sec} seconds")
    time.sleep(sec)
    print(f"Thread finished after {sec} seconds")

#Explain :- yahan target btata h kiss function ko chlna h aur args agrument leta h function ka list ke roop mein 
t1 = threading.Thread(target=func, args=(4,))
t2 = threading.Thread(target=func, args=(2,))
t3 = threading.Thread(target=func, args=(1,))
    
#Start thread
t1.start()
t2.start()
t3.start()

#Main thread ko bolta h ki phle ess thread ko complete ho jane doo 
t1.join()
t2.join()
t3.join()

print("All threads are completed!")
