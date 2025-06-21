############################
#section-41 "Methods and function"
#1
def keyword():
    '''
    'comment out'
    '''
    print('hello')


keyword() # hello

#2
def add_function(a,b):
    return  a+b

print(add_function(5,6)) #11


#3
def one_argumetn(name):
    print(f'hello {name}')

one_argumetn('raj') #hello raj


# 4
def one_argumetn(name='Default'):
    print(f'hello {name}')

one_argumetn()  # hello Default



############################
#section-45 "Logic with function"

def even_check(num):
    return num%2==0

print(even_check(5)) # false
print(even_check(4)) # true

def even_check_list(num_list):
    boo=True
    for val in num_list:
        if val%2==0:
            pass
        else:
            boo=False
            break

    if(boo):
        return "the list is even in nature"
    else:
        return "The list is not even in nature"

print(even_check_list([2,4,6])) #the list is even in nature
print(even_check_list([2,5,6])) # The list is not even in nature
