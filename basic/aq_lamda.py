#Along with lamda funciton we use two fuction 1. map 2. filter
#1.
def square(num):
    return num**2

print(square(5)) #25

my_list=[1,2,3,4,5]

def new_map():
    for items in map(square,my_list):
        print(items)

new_map()
# 1
# 4
# 9
# 16
# 25


#2.
def func2(name):
    if len(name)%2==0:
        return 'Even'
    else:
        return name[0]

names=['raj','karan','chauhan1']

def new_map2():
    new_list=list(map(func2,names))
    print(new_list)

new_map2() # ['r', 'k', 'Even']


################   FILTER
#3.
def func3(name):
    return len(name)%2==0

names3=['raj','karan','chauhan1']

def new_filter3():
    new_list=list(filter(func3,names3))
    print(new_list)

new_filter3() # ['chauhan1']

########################## lamda
#1.
def square(num):
    return num**2

print(square(5))#25

#2. we can also define it as in lamda
#def square(num):    return num**2
#lambda num: return num**2

#a.
num_list=[1,2,3,4,5]
def lamda1():
    return list(map(lambda num:num**2,num_list))

print(lamda1())# [1, 4, 9, 16, 25]

#b.
def lamda2():
    return list(map(lambda num:num%2==0,num_list))

print(lamda2())# [1, 4, 9, 16, 25] #[False, True, False, True, False]

#c.
name3=['raj','karan','chauhan']

def lamda3():
    return list(map(lambda val:val[0],name3))

print(lamda3())#['r', 'k', 'c']