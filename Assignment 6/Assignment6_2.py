class BankAccount:
    ROI=10.5
    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount
    def Deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.Amount += amount
        print("\n Amount Deposited:", amount)
    def Withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.Amount>= amount:
            self.Amount-= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient")
    def CalculateIntrest(self):
        p=Amount
        r=10.5
        t=1
        print("The rate of interest:",p*r*t/100)
    def Display(self):
        print(self.Name,self.Amount)
Name=(input("Enter the Name:"))
Amount=int(input("Enter the amount:"))
obj1=BankAccount(Name,Amount)
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateIntrest()
obj1.Display()

