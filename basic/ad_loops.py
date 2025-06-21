############################
#section-34 "If Elif and Else"
num =33
if (num<4):
    print(' num is less then 4')
elif (num==5):
    print(" num is 5")
else:
    print("number is greater then 5")
# number is greater then 5


############################
#section-35 "For"

my_list=[1,2,3,4,5]
for val in my_list:
    print(val)

# 1
# 2
# 3
# 4
# 5

for val in my_list:
    if(val%2==0):
        print(val)
#2
#4

my_one=[1,2,3,4,5]
sum=0
for val in my_one:
    sum=sum+val

print("sum is :"+str(sum)) #sum is :15


str='raj karan'
for val in str:
    print(val)

# r
# a
# j
#
# k
# a
# r
# a
# n


# for a list containing set values
li=[(1,2),(3,4),(5,6)]
for val in li:
    print(val)
# (1, 2)
# (3, 4)
# (5, 6)

for a,b in li:
    print(a)
    print(b)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6


######## for dict
d={'k1':1,'k2':2,'k3':3}

#only keys
for val in d:
    print(val)
    # k1
    # k2
    # k3

#only values
for val in d.values():
    print(val)
    # 1
    # 2
    # 3

#key valuse
for val in d.items():
    print(val)
    # ('k1', 1)
    # ('k2', 2)
    # ('k3', 3)

for k,v in d.items():
    print('key is: '+ k+' and value is: ')
    print(v)
    # key  is :  k1 and value is:
    # 1
    # key  is : k2 and value is:
    # 2
    # key is : k3 and value is:
    # 3


############################
#section-36 "While"
# while someBooleanCOndition:
#   doSomething
# else:
#   doOtherThing

x=0
while x<5:
    print(f'The current value of x is : {x}')
    x=x+1
else:
    print(f'The current value of x is greater then 5 and is : {x}')

# The current value of x is : 0
# The current value of x is : 1
# The current value of x is : 2
# The current value of x is : 3
# The current value of x is : 4
# The current value of x is greater then 5 and is : 5



