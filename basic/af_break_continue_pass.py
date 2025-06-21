#continue : if the condition is true then go skip the current loop and go to the next loop
name='sammy'
for val in name:
    if(val=='a'):
        continue
    print(val)
    # s
    # m
    # m
    # y

# break: if the conditon is true then break the current loop and come out
name='modi'
for val in name:
    if(val=='d'):
        break
    print(val)
    # m
    # o

# pass to skip the logic implementaiton we use pass
name='modi'
for val in name:
    pass   # if we dont write the implementaion then it will through error to overcome the error we use pass
