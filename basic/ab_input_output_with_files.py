my_file=open("ab_input_output_with_files.txt")
# if the file was in different folder then i would have used folder/ab_input_output_with_files.txt
print(my_file.read())
# hello this is line 1
# hello this is line 2
# hello this is line 3
print(my_file.read()) # ' ' here nothing is shown as the cursor went till last line and to read it agian we need to reset the cursor

my_file.seek(0)
print(my_file.read())
# hello this is line 1
# hello this is line 2
# hello this is line 3

my_file.seek(0)
text=my_file.read()
print(text)
print(text)
# hello this is line 1
# hello this is line 2
# hello this is line 3
# hello this is line 1
# hello this is line 2
# hello this is line 3

print('---------')
my_file.seek(0)
print(my_file.readline()) #hello this is line 1
print(my_file.readline()) #hello this is line 2
print(my_file.readline()) #hello this is line 3
print(my_file.readline()) # ' '

my_file.close() # it is good practive to close the open file after use

print('best practice to open files')
## best practice to open files
# mode
# r = read only
# w = write only, override, create new
# a = append only
# r+= read and writing
# w+= writing and reading (override , create new)

print("append")
with open("ab_input_output_with_files.txt", mode='a') as a:
    a.write("\nI am fourth line")
    a.close()

with open("ab_input_output_with_files.txt", mode='r') as f:
    print(f.read())
    # hello this is line 1
    # hello this is line 2
    # hello this is line 3
    # I am fourth line
    print(f.read())
     # ' '
    f.close()

print("new file write and read")
with open("ab_new_files.txt", mode='w+') as w:
    w.write("I am new file")
    w.seek(0)
    print(w.read())
    # new file write and read
    # I am new file
    w.close()




