class BankAccount:
    bank_name="State Bank"

    def __init__(self,n,b):
        self.name=n
        self.bal=b

    def deposit(self,amount):
        self.bal+=amount
        print(f"Amount of {amount} Added Successfully")
    
    def withdraw(self,amount):
        if self.bal > amount:
            print("Sufficient amount")
            print("Your total Balance is ",self.bal)
            self.bal-=amount
            print("After withdraw the total Balance is",self.bal)
    def display(self):
        print("Account name: ",self.name)
        print("Balance: ",self.bal)
    
A=BankAccount("Alice",1000)
B=BankAccount("Bob",500)

print(A.bank_name)

A.display()
A.deposit(500)
A.display()
print()

B.display()
B.withdraw(200)
print()
B.display()