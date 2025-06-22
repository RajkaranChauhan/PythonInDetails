class Animal():
    def __init__(self,name):
        self.name=name

    def speak(self):
        raise NotImplementedError("Sub class must implement this method")

# animal=Animal('tom')
# animal.speak() #NotImplementedError: Sub class must implement this method

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
    def speak(self):
        return self.name+ " says woff"

class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
    def speak(self):
        return self.name+ " says meao"

dog=Dog("Tommy")
cat=Cat("Pussy")
print(dog.speak())#Tommysays woff

print(cat.speak())#Pussy says meao

