# enumarator: is assign index to the valuse
lt=['apple','banana','cat']
for val in enumerate(lt):
    print(val)
    # (0, 'apple')
    # (1, 'banana')
    # (2, 'cat')

lt=['apple','banana','cat']
for k,v in enumerate(lt):
    print(k)
    print(v)
# 0
# apple
# 1
# banana
# 2
# cat