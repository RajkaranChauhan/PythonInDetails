from random import shuffle

#1
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

# the below lines of code is to test the above def shuffle_list()
# new_list=[' ',' ','O']
# res=shuffle_list(new_list)
# print(res) #[' ', 'O', ' ']   # ['O', ' ', ' ']

def player_guess():
    guess=''
    while guess not in ['0','1','2']: #here the numbers are taken as str coz the input takes string
        guess=input("pick any one number from '0','1','2' : ")

    return int(guess) # as input filed return values in string so we need to type cast to int

# # to test the def player_guess
# print(player_guess())

def check_guess(shuffle_list, guess):
    if shuffle_list[guess]=='O':
        print('TRUE')
    else:
        print("FALSE")
        print(shuffle_list)

def final_function():
    my_list=[' ',' ','O']
    return_shuffle=shuffle_list(my_list)
    guess=player_guess()
    check_guess(return_shuffle,guess)

final_function()