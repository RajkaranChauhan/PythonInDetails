class Dog():
    def __init__(self,name):
        self.name=name

    def speak(self):
        return f"'{self.name}' says woff!"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"'{self.name}' says meao!"
    

dog=Dog("niko")
cat=Cat("flex")

print(dog.speak()) #'niko' says woff!
print(cat.speak()) # 'flex' says meao!




