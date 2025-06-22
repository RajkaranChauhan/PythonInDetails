class Animal():
    def __init__(self):
        print("Contracture of Animal")

    def who_am_i(self):
        print("I am animal")

    def eat(self):
        print("I am eating in Animal")


animal = Animal()  # Contracture of Animal


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)  # this is used to call the constructor of parent
        print("Constructor of Dog")


dog = Dog()
# Contracture of Animal
# Constructor of Dog

dog.eat()  # I am eating in Animal
dog.who_am_i()  # I am animal


# overriding method
class Dog1(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Constructor of Dog1")

    # over riding the below method
    def who_am_i(self):
        print("I am Dog1")

    def bark(self):
        print("wooff!")


dog1 = Dog1()
# Contracture of Animal
# Constructor of Dog1

dog1.eat()  # I am eating in Animal
# below is overriding method
dog1.who_am_i()  # I am Dog1
dog1.bark()  # wooff!
