from collections import Counter

my_list=['a','a','b','c','c','c']
print(Counter(my_list))
#Counter({'c': 3, 'a': 2, 'b': 1})


sentence="how are you raj you are"
print(Counter(sentence.split()))
# Counter({'are': 2, 'you': 2, 'how': 1, 'raj': 1})
print(Counter(sentence))
#Counter({' ': 5, 'o': 3, 'a': 3, 'r': 3, 'e': 2, 'y': 2, 'u': 2, 'h': 1, 'w': 1, 'j': 1})

print(Counter(sentence).most_common())
#[(' ', 5), ('o', 3), ('a', 3), ('r', 3), ('e', 2), ('y', 2), ('u', 2), ('h', 1), ('w', 1), ('j', 1)]

print(Counter(sentence).most_common(3))
#[(' ', 5), ('o', 3), ('a', 3)]

print(list(Counter(sentence)))
#['h', 'o', 'w', ' ', 'a', 'r', 'e', 'y', 'u', 'j']



"""
default dict
"""
from collections import defaultdict

d={"key1":"val1"}

print(d) #{'key1': 'val1'}
print(d["key1"]) # val1
# print(d["any"]) # it will throw an error as there is no key as 'any' in the dict d

# now for any wrong key we can assign a default value so that it will not throw error
a=defaultdict(lambda :'hahaha')
a["key2"]="val2"

print(a) #defaultdict(<function <lambda> at 0x0000019F242C8AE0>, {'key2': 'val2'})
print(a["key2"])#val2
print(a["any"])# hahaha


