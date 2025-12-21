class Bank:
    
    def __init__(self,u,b):
        self.username= u
        self.balance= b
        
    def show(self):
        print(f"Account Holder :- {self.username} | balance :- {self.balance}")
     
     
user1 = Bank("Sonu Yadav",5000)
user1.show()

user2 = Bank("Rikesh Singh",4000)
user2.show()


OUTPUT:----

Account Holder :- Sonu Yadav | balance :- 5000
Account Holder :- Rikesh Singh | balance :- 4000
