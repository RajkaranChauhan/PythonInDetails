#open the .csv file
#reformat it into a python object list of lists
import csv

data = open('csv_file/users.csv',encoding="utf-8")
csv_data=csv.reader(data)
data_lines=list(csv_data)

print(data_lines)
# [['first_name', 'last_name', 'age', 'sex', 'email'], ['Amit', 'Verma', '22', 'Female', 'amit.verma@example.com'], ['Divya', 'Patel', '22', 'Male', 'divya.patel@example.com'], ['Aisha', 'Sharma', '36', 'Male', 'aisha.sharma@examp
# le.com'], ['Rahul', 'Verma', '48', 'Female', 'rahul.verma@example.com'], ['Aisha', 'Joshi', '18', 'Male', 'aisha.joshi@example.com'], ['Karan', 'Rao', '48', 'Female', 'karan.rao@example.com'], ['Vikas', 'Joshi', '29', 'Male', 'v
# ikas.joshi@example.com'], ['Vikas', 'Mehta', '18', 'Male', 'vikas.mehta@example.com'], ['Karan', 'Nair', '40', 'Male', 'karan.nair@example.com'], ['Divya', 'Joshi', '32', 'Male', 'divya.joshi@example.com']]


print(data_lines[0])
# ['first_name', 'last_name', 'age', 'sex', 'email']

print(len(data_lines))
# lenght is 11, where line 1 is header and 2-11 are data


for val in data_lines[:5]:
    print(val)
# ['first_name', 'last_name', 'age', 'sex', 'email']
# ['Amit', 'Verma', '22', 'Female', 'amit.verma@example.com']
# ['Divya', 'Patel', '22', 'Male', 'divya.patel@example.com']
# ['Aisha', 'Sharma', '36', 'Male', 'aisha.sharma@example.com']
# ['Rahul', 'Verma', '48', 'Female', 'rahul.verma@example.com']

print(data_lines[3][4])
# aisha.sharma@example.com

print("-----------------------------------------------------")
#Now print all the emails present in the file
for val in data_lines[1:]:
    print(val[4])

# amit.verma@example.com
# divya.patel@example.com
# aisha.sharma@example.com
# rahul.verma@example.com
# aisha.joshi@example.com
# karan.rao@example.com
# vikas.joshi@example.com
# vikas.mehta@example.com
# karan.nair@example.com
# divya.joshi@example.com


print("--------------print all the full names----------------")
for val in data_lines[1:]:
    print(val[0]+ " "+val[1])

# Amit Verma
# Divya Patel
# Aisha Sharma
# Rahul Verma
# Aisha Joshi
# Karan Rao
# Vikas Joshi
# Vikas Mehta
# Karan Nair
# Divya Joshi


"""
writing data in csv file back

file_to_output=open('to_save_file.csv', mode='w',newline='')
csv_write=csv.writer(file_to_output,delimiter',')
csv_write.writerow(['a','b','c'])
csv_write.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()



now if we want to append not overwrite then

f=open('to_save_file.csv', mode='a', newline='')
csv_writer=csv.writer(f)
csv_writer.writerow(['1','2','3'])
f.close()

"""