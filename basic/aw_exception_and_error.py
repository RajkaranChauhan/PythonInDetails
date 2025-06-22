# try: this block may leads to an error
# except: if there is an error then this block will execute
# finally: This block will always execute

try:
    print(10+'10') # this will throw error
except :
    print('check the input again')
finally:
    print("I always run")
#output:
# check the input again
#I always run

try:
    print(10+5) # this will throw error
except :
    print('check the input again')
finally:
    print("I always run")
# output:
# 15
# I always run




#for all other expection use expect
# except TypeError:
#     print("Type Error")
# except:
#     print("all other exception")
# finally:
#     print("finally block")

def ask_for_int():
    try:
        resutl=int(input('provide a number: '))
    except:
        print("That is not a number")
    finally:
        print("I am finally block")
ask_for_int()
# provide a number: mm
# That is not a number
# I am finally block

# provide a number: 5
# I am finally block


def ask_for_int1():
    while True:
        try: # here this block acts as if block
            resutl=int(input('provide a number: '))
        except:
            print("That is not a number")
            continue
        else:
            print("Thank you")
            break
        finally:
            print("I am finally block")
ask_for_int1()

# provide a number: f
# That is not a number
# I am finally block
# provide a number: k
# That is not a number
# I am finally block
# provide a number: 55
# Thank you
# I am finally block
