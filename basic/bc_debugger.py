import pdb


x='a'
y=2
z=3

print(y+z) # 5
#to debug the below we use
pdb.set_trace()
print(x+y) # TypeError: can only concatenate str (not "int") to str