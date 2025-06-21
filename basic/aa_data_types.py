############################
# section-6
from builtins import print

a=2
print(a) # 2
print(type(a))  # int

############################
# section-7
my_income=10000
tax=.3 #30%
income_tax= my_income*tax
print(income_tax)  # 3000

############################
#section-15 "Strings"
print("Hello World") #Hello World
print("hello \nworld") #hello
                        #world

#[Start:Stop:step] stop- till this but not included
# characters: h e l l o
#index      : 0 1 2 3 4
#rev index  : 0-4-3-2-1


############################
#section-16 "indexing and slicing with string"
my_string="hello world"
print(my_string[0]) #h
print(my_string[8]) #r
print(my_string[-1]) #d
print(my_string[-4]) #o
print(my_string[2:]) #ello world
print(my_string[:3]) #hel
print(my_string[2:5]) #ll0
print(my_string[: :]) #hello world
print(my_string[: :2]) #hlowrd
print(my_string[: :-1]) # dlrow olleh


############################
#section-17 "String properties and methods"
name='sam'
# i am planning to update sam to pam
# name[0]='p' #name[0]='p' #this will throw errro as this is not supported

last_letters=name[1:]
print(last_letters) # am
print('p'+last_letters) #pam

print(2+3)#5
print('2'+'3')#23

x='Hello'
print(x)#Hello
print(x.upper()) # HELLO
print(x.lower()) #hello
print(x.split('e')) #['H', 'llo']
y='Hi this is a string for test'
print(y.split('i')) # ['H', ' th', 's ', 's a str', 'ng for test']


############################
#section-19 "Print formatting using string"
#1. .formate()
#2. f-strings

#1. .formate()
print("this is a string {}".format('INSERTED')) #this is a string INSERTED
print("this {} {} {}".format('is','a','string')) #this is a string
print("this {2} {1} {0}".format('is','a','string')) # this string a is
print("this {2} {2} {2}".format('is','a','string')) # this string string string
print("this {a} {b} {c}".format(a='is',b='a',c='string')) #this is a string

#2. f-strings
name='raj'
age=25
print(f'Hello {name}, your age is {age}') #Hello raj, your age is 25

############################
#section-21 "List"

my_list=[1,2,3]
print(my_list) #[1, 2, 3]
my_list=['abc', 2, 33.33]
print(my_list) # ['abc', 2, 33.33]
print(my_list[0]) #abc
print(my_list[1:]) # [2, 33.33]

# concatination
my_list2=['raj','karan']
new_list=my_list+my_list2
print(new_list) # ['abc', 2, 33.33, 'raj', 'karan']

new_list[0]='NEW VALUE'
print(new_list) # ['NEW VALUE', 2, 33.33, 'raj', 'karan']

#to add value at the end of the list
new_list.append("LAST VALUE")
print(new_list) # ['NEW VALUE', 2, 33.33, 'raj', 'karan', 'LAST VALUE']

# remove last value
new_list.pop()
print(new_list) #['NEW VALUE', 2, 33.33, 'raj', 'karan']

#store the last removed value in some variable
print(new_list) ##['NEW VALUE', 2, 33.33, 'raj', 'karan']
pop_value=new_list.pop()
print(new_list)#['NEW VALUE', 2, 33.33, 'raj']
print(pop_value) # karan

new_list.pop(0)
print(new_list) #[2, 33.33, 'raj']

new_list.pop(-1)
print(new_list) #[2, 33.33]

#sorting list
list_to_sort=[ 'r','a','j','e','s','h']
print(list_to_sort) #['r', 'a', 'j', 'e', 's', 'h']
list_to_sort.sort()
print(list_to_sort) # ['a', 'e', 'h', 'j', 'r', 's']

list_to_sort=[ 'r','a','j','e','s','h']
print(list_to_sort) #['r', 'a', 'j', 'e', 's', 'h']
sort_list=list_to_sort.sort()
print(sort_list) # None as .sort() does not return any value

list_to_sort=[ 'r','a','j','e','s','h']
print(list_to_sort) #['r', 'a', 'j', 'e', 's', 'h']
new_list=list_to_sort
print(new_list) #['r', 'a', 'j', 'e', 's', 'h']

# reverse a list
new_list.reverse()
print(new_list) # ['h', 's', 'e', 'j', 'a', 'r']

print('h' in new_list) #true

l=list(range(10))
print(min(l)) #0
print(max(l))  # 9
############################
#section-23 "Dictionaries"

my_dic={'key1':'value1', 'key2':'value2'}
print(my_dic) # {'key1': 'value1', 'key2': 'value2'}
print(my_dic['key1']) # value1

d={'k1':123,'k2':[0,1,2],'k3':{'key':'val'}}
print(d['k1']) # 123
print(d['k2'][2])# 2
print(d['k3']['key'])# val

d={'k1':123,'k2':['a','b','c'],'k3':{'key':'val'}}
print(d) # {'k1':123,'k2':['a','b','c']'k3':{'key':'val'}}
one=d['k2']
print(one) # ['a', 'b', 'c']
two=one[1]
print(two) #b
print(two.upper()) # B

print(d.keys()) # dict_keys(['k1', 'k2', 'k3'])
print('k1' in d.keys()) #true
print(d.values()) # dict_values([123, ['a', 'b', 'c'], {'key': 'val'}])
print(d.items()) # dict_items([('k1', 123), ('k2', ['a', 'b', 'c']), ('k3', {'key': 'val'})])


############################
#section-25 "Tuples"

# it is similar to list but it is immuatable
# element inside tuple cannot be reassigned
# it used round bracket () eg. (1,2,3)

t= (1,2,3)
print(type(t)) #<class 'tuple'>
print(t)# (1, 2, 3)
len(t)# 3
print(t[0]) #1
print(t[-1]) #3


#it has two methods
# t.count()
# t.index('a')
t=('a','b','a')# v
print(t)
print(t.count('a')) #2
print(t.index('b')) #1


# t[0]='man' #TypeError: 'tuple' object does not support item assignment


############################
#section-25 "Set"

my_set=set()
print(my_set) #set()
print(type(my_set)) # <class 'set'>
my_set.add('abc')
print(my_set) #{'abc'}
my_set.add('mno')
print(my_set) #{'mno', 'abc'}
my_set.add('abc')
print(my_set) ##{'mno', 'abc'}    duplicate is not allowed

list_randon=['ab',12, 12,'ab']
print(list_randon) # ['ab', 12, 12, 'ab']
print(set(list_randon))# {12, 'ab'}
