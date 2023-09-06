# Challenge 1: Square Numbers and Return Their Sum

class Point:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def sqSum(self):
        return self.x **2 + self.y **2 + self.z **2

x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))
z = int(input("Enter the value of z : "))

point = Point(x,y,z)
print(point.sqSum())



# Challenge 2: Implement a Calculator Class


class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num2 - self.num1
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num2 / self.num1


num1 = int(input("Enter value of num1 : "))
num2 = int(input("Enter value of num2 : "))


obj = Calculator(num1, num2)

print(obj.add())       
print(obj.subtract())  
print(obj.multiply())  
print(obj.divide())



# Challenge 3: Implement the Complete Student Class


class Student:

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber

    def getRollNumber(self):
        return self._rollNumber
    
    
student = Student()
student.setName("Srikanth ")
student.setRollNumber("1234")

print(student.getName())         
print(student.getRollNumber())    



# Challenge 4: Implement a Banking Account

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

account = Account("Ashish", 5000)
print(account.title)    
print(account.balance) 


savings_account = SavingsAccount("Ashish", 5000, 5)
print(savings_account.title)        
print(savings_account.balance)      
print(savings_account.interestRate) 



# Challenge 5: Handling a Bank Account

class Account:

    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount
        

    def deposit(self, amount):
        self.balance += amount
        

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return self.balance * (self.interestRate / 100)

demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.deposit(500)
print(demo1.getBalance())

demo1 = SavingsAccount("Ashish", 2000, 5)   
demo1.withdrawal(500)
print(demo1.getBalance()) 

demo1 = SavingsAccount("Ashish", 2000, 5)
print(demo1.interestAmount())   






