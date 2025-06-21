############################
#section-38 "List comprehensionn"
#1
my_str='hello'
my_lst=list()
for val in my_str:
    my_lst.append(val)

print(my_lst) #['h', 'e', 'l', 'l', 'o']

#2
list2 = [val for val in my_str]
print(list2)


#3
list3=[val  for val in range(20)]
print(list3) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

#4
list4=[val*val  for val in range(10)]
print(list4) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#5
list5=[val for val in range(20) if val%2==0]
print(list5) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#6 celcius to farenheite
celcius=[0,10,20,34.5]
farenheitte=[((9/5)*temp+32) for temp in celcius]
print(farenheitte) #[32.0, 50.0, 68.0, 94.1]

#7 if else
result=[val if val%2==0 else 'ODD' for val in range(9)]
print(result) #[0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8]

#8 nested loop
list8=list()
for x in [2,4,6]:
    for y in [100, 200, 300]:
        list8.append(x*y)

print(list8) # [200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

 # OR

list9=[x*y for x in [1,2,3] for y in [100,200,300]]
print(list9) #[100, 200, 300, 200, 400, 600, 300, 600, 900]


#10
list10=[val for val in range(50) if val%3==0]
print(list10) #[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

#11
word="the apple is red in colour"
list11=[ val[0] for val in word.split()]
print(list11) #['t', 'a', 'i', 'r', 'i', 'c']

#12 range 1 to 100, multiple of 3 print fizz for 5 buzz and for 3 and 5 fizzBuzz
for val in range(1,20):
    if (val%3==0) and (val%5==0):
        print(str(val)+' FizzBuzz')
    elif(val%3==0):
        print(str(val)+' Fizz')
    elif (val % 5 == 0):
        print(str(val)+' Buzz')
# 3 Fizz
# 5 Buzz
# 6 Fizz
# 9 Fizz
# 10 Buzz
# 12 Fizz
# 15 FizzBuzz
# 18 Fizz
