# Dunder are special methods to give info about the object created but for that we need to set few definations as given below
#1.
class Book():
    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page


b = Book("python", "raj", 200)
print(b)  # <__main__.Book object at 0x00000291BCE45E50>


# in the above example when we try to pring the refference variable of the class it is not giving any infomation

#2.
class Book1():
    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page
#creating a special method /dunder, this method is already there just we are defining it
    def __str__(self):
        return f"{self.title} by {self.author}"

b1 = Book1("python", "raj", 200)
print(b1)  # python by raj

#3.
# len(b1)
# output:  len(b1)
# TypeError: object of type 'Book1' has no len()

class Book2():
    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page
#creating a special method /dunder, this method is already there just we are defining it
    def __len__(self):
        return self.page

    #to delete a object
    def __del__(self):
        print("A book object has been delted")

b2 = Book2("python2", "raj2", 250)
print(len(b2)) #250

del (b2) #A book object has been delted

#