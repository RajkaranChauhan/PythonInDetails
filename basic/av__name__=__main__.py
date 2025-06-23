#the below code requried to create two .py script so writing it here in one script with comment out to understand

#  one.py
# def fun():
#     print("Fun in one.py")
# print("Top level in one.py")
# if __name__=='__main__':
#     print('one.py is run directly')
# else:
#     print('one.py is imported')
#
#
#
#
#  two.py
#
# import one
# print("Top level in two.py")
# one.fun()
# if __name__=='__main__':
#     print('two.py is run directly')
# else:
#     print('two.py is imported')
#
#
#
# cmd
# python one.py
# output:
# Top level in one.py
# one.py is run directly
#
# python two.py
# Top level in one.py
# one.py is imported
# Top level in two.py
# Fun in one.py
# two.py is run directly