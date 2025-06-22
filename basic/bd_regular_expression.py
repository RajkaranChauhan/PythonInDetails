# (555)-555-5555
# r"(\d\d\d)-\d\d\d-\d\d\d"
import re

text="the phone number is 555-555-5555"
pattern="phone"
restult= re.search(pattern,text)
print(restult) #<re.Match object; span=(4, 9), match='phone'>

print(restult.span()) #(4, 9)
print(restult.start()) # 4
print(restult.end())# 9

"""
NOTE: if we have multiple match then it will only give us only first match
"""

text="my phone one my phone twice"
result=re.findall("phone",text)
print(result) #['phone', 'phone']

"""
Character	    Description	        Pattern         Example	Matches
\d	            A digit	            file_\d\d	    file_25
\w	            Alphanumeric	    \w-\w\w\w	    A-b-b1
\s	            Whitespace	        a\s\b\s\c	    a b c
\D	            Non-digit	        \w\W\W\W	    x-=+
\S	            Non-whitespace	    \S\S\S\S	    yoyo
"""

text =" my phone number is 408-555-5555"
phone_num=re.search(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)',text)  # the round bracket () in the number are creating groups
print(phone_num) # <re.Match object; span=(20, 32), match='408-555-5555'>
print(phone_num.group()) #408-555-5555
print(phone_num.group(1))
print(phone_num.group(1))
print(phone_num.group(2))



"""
few other methods of reg expression are given below

or operator
re.search(r'cat|dog', "that is a cat")
#match either cat or dog

re.findall(r'at',"cat hat sat")

wild card
re.findall(re'.at'," cat hat sat mmm")
output: [cat, hat, sat]

starts with number
re.findall(r'^\d',"1 is a number")
['1']

ends with number
re.findall(r'^\d'$," number is 2")
['2']

"""


