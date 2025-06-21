from random import shuffle
my_list=list(range(0,20,2))
print(my_list) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
shuffle(my_list)
print(my_list) #[10, 8, 16, 6, 12, 2, 18, 14, 0, 4]