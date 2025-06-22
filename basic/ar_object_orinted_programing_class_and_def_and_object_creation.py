
#1.
class SampleOne():
    pass

#the below lines are not part of class smapleone as it is as same indent as class so this is condiserd as seperate command
sampleOne = SampleOne()
print(type(sampleOne)) #<class '__main__.SampleOne'>

#2.
class Dog():
    def __init__(self,bread):
        self.bread=bread

dog=Dog('lab')
print(dog.bread) #lab

#3.
class Circle():
    pi=3.14
    def __init__(self,radius=1): #default value of radius is 1
        self.radius=radius

    def circumferance(self):
        return self.radius*self.pi*2

circle=Circle(5)
circ=circle.circumferance()
print(circ) #31.400000000000002