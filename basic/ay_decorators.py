"""
if you have a funciton and for some reason you need more lines of code in that fucntion. Then we copy the funciton as funciton2 and add the new lines of code
what if you don't need thr function2 anymore the next day, you need to delete manually
the better way would be having ON and OFF switch
"""

#1.
def func():
    return 'Hello'

print(func()) # Hello

# if we try to print func without '()'  then it represents the object of the function and gives your the address of the funciton as given below
print(func) # <function func at 0x00000216CD3C8AE0>

#2. now assigning the object 'func' to new reff variable
greet=func

print(greet) # <function func at 0x0000022306438AE0> pointing to the same def of func
print(greet()) # Hello

#now greet is pointing to the same def or made a copy of the def
#now we will delete hello and see


print(func()) #Hello
del func
# print(func()) # NameError: name 'func' is not defined -->  getting this error to by pass this error we are commenting it out

# so when we try to print hello then it is throwing error that means hello obj is delted

print(greet()) #Hello  -> this proves that greet did not made an new def it is pointing to the same obj as fucn

"""
NOTE: a function obj can be passed to a different object, 
"""


#2. now defining a def inside a def, and the scope of the inner def will be inside the outer def
print("------------------------------------")
def hello(name='raj'):
    print("Inside hello def")

    def greet():
        return "\n from greet function"

hello()  #Inside hello def
# here it only printed "Inside hello def"
#greet def is in the inner loop of the hello def
#till  now greet def is not called and it has a return type

print("------------------------------------")
def hello(name='raj'):
    print("Inside hello def")

    def greet():
        return "\n from greet function"
    print(greet())

hello()
# Inside hello def
#  from greet function

# now the def greet is also called, as we have called it inside  the def hello

"""
Now lets return the greet() from inner loop to outside of the hello object 
- till now greet and hello def  can be executed inside the hello def
- what if we want to execute it out of hello def
- for this we have to return the greet def from hello def
"""
print("***********")
def hello1(name='raj'):
    print("i am inside hello1")
    def greet():
        print("inside greet")
    def welcome():
        print("inside welcome")

    print("i am going to return  a function")

    if name=='raj':
        return greet     # please keep in mind it is returning a object not a def or string value
    else:
        return welcome

hello1("raj")
# i am inside hello1
# i am going to return  a function
print("*-*-*-*-*-*-*-*")

new_func=hello1("raj") # here the return type of hello1('raj') is assign to new_func
# i am inside hello1
# i am going to return  a function
print(new_func)  #<function hello1.<locals>.greet at 0x000001E70327D120>
new_func()  # using () is calling the funciton associated with the object new_func
# inside greet




"""
Now lets see how can we pass def as an argument to a different def 
"""
print("===================================================")
def hello2():
    return "hello raj"

def other_def(some_def):
    print("i am other definaiton")
    print(some_def())

print(hello2()) #hello raj

other_def(hello2)  # here passing the obj of hello() with out '()'
# i am other definaiton
# hello raj

"""
FINALLY we are going to talk about decorators
Idea is to warp paper like gift to original function and then return
"""
print("=======================================================================================")
print("=======================================================================================")

def new_dec(original_dec):
    def warp_func():
        print("Before")
        original_dec()
        print("After")
    return warp_func()

def func_needs_dec():
    print("I wanted to be decorate")


final_funciton=new_dec(func_needs_dec)
# Before
# I wanted to be decorate
# After

print("11111111")
 #OR we can rewrite this as

@new_dec  #passing this to the definition that need the decorator
def func_needs_dec():
    print("I wanted to be decorate")

# Before
# I wanted to be decorate
# After


