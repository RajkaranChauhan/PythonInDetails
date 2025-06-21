############################
#section-49 "args and kwargs"

# arguments and key word arguments

#1. args
def myfunc(a,b):
    return a+b

print(myfunc(5,6)) #11

# what if we want more arguments
# we can use args or anything value or num
# here * is mandatory
def myfunc1(* args):
    return sum(args)

print(myfunc1(5,6,7)) #18
print(myfunc1(1)) #1



#2. kwargs
def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print(f"my fruit is {kwargs['fruit']}")
    else:
        print('No fruits')

myfunc2(fruit='apple',veggi='potato') # my fruit is apple
