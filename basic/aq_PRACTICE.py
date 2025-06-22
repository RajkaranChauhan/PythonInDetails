#1. volume of sphere
def vol_sphere(radius):
    return (4/3)*3.14*(radius*3)

print(vol_sphere(5))#62.8

#2. check weather a num in a given range (inclusive of high and low)
# 5 in range (0,5) False
#5 in range (0,10) True

def range_check(num, low, high):
    if num in range(low,high+1):
        print(f'The num {num} is in the range of low {low} and high {high}')
    else:
        print(f'The num {num} is NOT the range of low {low} and high {high}')

range_check(5,0, 5)#The num 5 is in the range of low 0 and high 5
range_check(5,0, 10)# The num 5 is in the range of low 0 and high 10


#3. In a string find the count of upper and lower case

def up_low_case(text):
    upper=0
    low=0
    for val in text:
        if val.isupper():
            upper +=1
        else:
            low +=1

    print(f"upper case is : {upper} and lower case is: {low}")

up_low_case("RajKaranChauhan") #upper case is : 3 and lower case is: 12

#4. unique value in list
def unique_value():
    list4=['raj','karan','chauhan','raj']
    unq=[]
    for val in list4:
        if val not in unq:
            unq.append(val)

    print(unq)

unique_value() #['raj', 'karan', 'chauhan']

#5. duplicate
def unique_value1():
    list5=['raj','karan','chauhan','raj']
    unq=[]
    dup=[]
    for val in list5:
        if val not in unq:
            unq.append(val)
        else:
            dup.append(val)

    print(dup)

unique_value1() #['raj']


#6. palindrom like liril

def palindrom(text):
    rev=text[::-1]
    if rev==text:
        print(f'the text {text} is palindrom')
    else:
        print(f'the text {text} is NOT palindrom')

palindrom('liril') #print(f'the text {text} is palindrom')
palindrom('raj')# the text raj is NOT palindrom
