"""
- generator function allows us to write a function that can send back values and then later resume to pickup where it left off
- allowing up to generate a sequence  of values over time
- when generator function is compiled they become an object that supports an iteration protocol
-when they are called in code they don't actually return a value and then exit
- it will automatically suspend and resume their execution and state around the last point
-advantage is instead of having to compute an entire series of values up front it generated one value and waits till next value is called for
-occupies less memory
"""

def simple_gen():
    for val in range(3):
        yield val

for num in simple_gen():
    print(num)

# 0
# 1
# 2

print("111111111111111111111111111111111111111")

g=simple_gen()
print(g) #<generator object simple_gen at 0x000001228E534880>

print(next(g))
#0
print(next(g))
#1
print(next(g))
#2
print(next(g))
#  error:  StopIteration

"""
so for the first part the number was generated till the range in one go as it was called again and again in for loop 
in the second part we see it is generating a new number when only it is called 
"""