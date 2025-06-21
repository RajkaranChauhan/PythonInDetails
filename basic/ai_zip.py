#zip The zip() function combines two or more iterables (like lists, tuples, or strings)
# into a single iterable of tuples, pairing elements by position.

my_list1=[1,2,3]
my_list2=['a','b','c']
for val in zip(my_list1, my_list2):
    print(val)
    # (1, 'a')
    # (2, 'b')
    # (3, 'c')

#if the both the list is not same lenght then it will be sorten to the values available
my_list3=[1,2,3,4]
my_list4=['a','b','c']
for val in zip(my_list3, my_list4):
    print(val)
    # (1, 'a')
    # (2, 'b')
    # (3, 'c')

my_list1=[1,2,3]
my_list2=['a','b','c']
print(list(zip(my_list1,my_list2))) #[(1, 'a'), (2, 'b'), (3, 'c')]

print(dict(zip(my_list1,my_list2))) # {1: 'a', 2: 'b', 3: 'c'}

print('a' in my_list2) #true


