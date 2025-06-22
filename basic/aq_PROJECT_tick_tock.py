# here we are planning to design a ticktock game

#1. setting up the game frame
def display_row(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

row1=[' ', ' ',' ']
row2=[' ', ' ',' ']
row3=[' ', ' ',' ']

display_row(row1,row2,row3)
# [' ', ' ', ' ']
# [' ', ' ', ' ']
# [' ', ' ', ' ']

row2[1]='x'
row3[2]='o'

display_row(row1,row2,row3)
# [' ', ' ', ' ']
# [' ', 'x', ' ']
# [' ', ' ', 'o']

#2. taking user input

def user_input():
    choice=input("Please select number from 1 to 9 :")
    return choice # as input take values in string format but we need int but when we user choise.isdigit() this will work
#choise='100' this is not int but this is digit
#choise.isdigit() -> True
#int(choise) -> 100 instead of '100'

#3. validating user input if it is number and if it in range 1-9
def user_choice():
    choice='wrong'
    choice_range=range(1,10)
    with_in_range=False
    while choice.isdigit()==False and with_in_range==False:
        choice=user_input()
        #check if the choise made is digit
        if choice.isdigit()==False:
            print("Sorry please select a digit with range 1-9")

        #range checker
        if choice.isdigit()==False:
            if choice in choice_range:
                with_in_range=True
            else:
                with_in_range=False

    return choice

# print(user_choice())


#4. 
