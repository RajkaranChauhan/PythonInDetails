############################
#section-23 "practice"
#1. for given 2 numbers if all the num are even then return the lesser number and if the one or both are odd then return greater number

def func1(a,b):
    if a%2==0 and b%2==0:
        if a>b:
            return b
        else:
            return a
    elif a%2!=0 or b%2!=0:
        if a>b:
            return a
        else:
            return b

print(func1(5,7)) #7
print(func1(5,2)) #5
print(func1(2,4)) #2
print(func1(4,6)) #4

#2. function takes two words string return true if both words starts with same letter
def func2(text1,text2):
    return text1[0]==text2[0]

print(func2('raj','raju')) # True
print(func2('raj','karan')) # False

#3. Two integer ruturn True  if sum is 20 or if one of then is 20 or return false
def func3(a,b):
    # return if a+b==20 or a==20 or b==20  # this is one liner solution
    if a+b==20:
        return True
    elif a==20 or b==20:
        return True
    else:
        return False


print(func3(10,10)) #true
print(func3(10,20)) #true
print(func3(10,11)) #false


#4. uppercase first and fourth letter of a string
def func4(text):
    first=text[0]
    second=text[1:3]
    third=text[3]
    fourth=text[4:]
    return first.upper()+second+third.upper()+fourth

print(func4('karan')) # KarAn

#5. return a sentence with a word reverse

def reverse(text):
    return text[::-1]
def sentence_reverse(text):
    rev=''
    list=text.split()
    for val in list:
        rev= rev+" "+reverse(val)

    return rev.strip()

print(sentence_reverse("raj karan chauhan")) #jar narak nahuahc

#6 in a list [1,2,3,3] if it contains 3 next to 3 then return true or lese return false

def fucn6(list):
    for val in range(len(list)-1):
        if list[val]==list[val+1]:
            return True

    return False

print(fucn6([1,2,3])) #False
print(fucn6([1,2,3,3]))# True

#7. given a string return a string where for every character in the original there are three character
#'raj'-> 'rrraaajjj'
def fucn7(text):
    ret=''
    for val in text:
        # ret=ret+val+val+val
        ret = ret + val*3

    return ret

print(fucn7('raj')) #rrraaajjj