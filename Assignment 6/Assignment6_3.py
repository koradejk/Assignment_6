
class Arithmetic:
    def __init__(self,value):
        self.value=value
    def Chkprime(self):
        value=self.value
        for i in range(2, int(value ** (1 / 2)) + 1):
            if value % i == 0:
                return False
            # if number is prime then return True
        return True
    def ChkPerfect(self):
        value=self.value
        sum=0
        for i in range(1,value):
            if (value % i == 0):
                sum= sum + i
        if (sum== value):
           return True
        else:
            return False
    def Factors(self):
        value=self.value
        factors_list=[]
        i=1
        while i <= value:
            if value % i == 0:
                factors_list.append(i)
            i = i + 1
            return factors_list
    def SumFactors(self,i):
        factor_list=i
        sum=0
        for i in factor_list:
            sum+=1
            return sum
value=int(input("Enter the value:"))
obj=Arithmetic(value)
chk_prime=obj.Chkprime()
if chk_prime==True:
    print("it is prime no")
else:
    print("it is not prime no")
result=obj.ChkPerfect()
if result==True:
    print("it is perfect no")
else:
    print("it is not perfect no")
factors=obj.Factors()
print("Factor list",factors)
add_factors=obj.SumFactors(factors)
print("sum of factor:",add_factors)

