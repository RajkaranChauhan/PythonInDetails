#1. Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line
#   formula for d and slope m is given
# coordinate 1=(3,2)
# coordinate 2=(8,10)
# li -Line(coordinate1,coordinate2)

class Line():
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2

    def distance(self):
        m,n=self.coor1
        x,y=self.coor2
        return ((n-m)**2 + (y-x)**2)**.5

    def slope(self):
        m, n = self.coor1
        x, y = self.coor2
        return (n-m)/(y-x)

c1=(3,2)
c2=(8,10)
line=Line(c1,c2)
print(line.slope()) # -0.5
print(line.distance()) # 2.23606797749979



#2. for cylinder find volume and surface area

class Cylinder():
    def __init__(self, height=1,radius=1):
        self.height=height
        self.radius=radius

    def volume(self):
        return self.height*3.14*(self.radius)**2

    def surface_area(self):
        top=3.14*(self.radius**2)
        return (2*top)+(2*3.14*self.height*self.radius)

cyl=Cylinder(2,3)
print(cyl.volume()) #56.52
print(cyl.surface_area())#94.2


#3. bank account class with attribute owner, balance and two methods deposit and withdraw. withdraw cannot exceed balance

class Account():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,dep_amount):
        self.balance=self.balance+dep_amount
        print(f'Balance after deposit is {self.balance} and amount deposited is {dep_amount}')

    def withdraw(self,wd_amt):
        if self.balance>=wd_amt:
            self.balance=self.balance-wd_amt
            print(f"withdraw accepted of amount {wd_amt} and balance after withdraw is {self.balance}")
        else:
            print("Not enough balance")

    def __str__(self):
        return f"Owner: {self.owner}\n Balance: {self.balance}"

acc=Account('Raj',1000)
print(acc.owner) #Raj
print(acc.balance)#1000

acc.deposit(500) #Balance after deposit is 1500 and amount deposited is 500

acc.withdraw(1800) #Not enough balance

acc.withdraw(1100) #withdraw accepted of amount 1100 and balance after withdraw is 400

print(acc)
# Owner: Raj
#  Balance: 400