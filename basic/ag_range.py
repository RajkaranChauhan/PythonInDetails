# range(5)- it starts from 0 and ends by 4 skips 5
for val in range(5):
    print(val)
    # 0
    # 1
    # 2
    # 3
    # 4
for val in range(2,5):
    print(val)
    # 2
    # 3
    # 4

for val in range(1,11,2):
    print(val)
    # 1
    # 3
    # 5
    # 7
    # 9


li=list(range(5))
print(li) #[0, 1, 2, 3, 4]

index_count=0
for val in 'abcd':
    print(f"At index '{index_count}' the value present is '{val}'")
    index_count=index_count+1

    # At index '0' the value present is 'a'
    # At index '1' the value present is 'b'
    # At index '2' the value present is 'c'
    # At index '3' the value present is 'd'




