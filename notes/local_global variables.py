
#! Globle space----->the  area present outside the function is called as globle space.
#! Local space----->the area present inside the function or method area is called as local space.

#! global variables--->
#* in the case of globle variable we can accessed and modified in main space.
#* but inside the local space we can only access global variable but we can't modified it .

# a=10
# b=20
# print("before modification:",a)
# def demo():
#     global a
#     a=a+50
#     print(a)
#     print('hii')
# demo()
# print("After modification:",a)

# Inorder to modify the globle variable inside the local space we can use a keyword global. 
# it should be the first instruction inside the local space in function.

#! Local variable----->
#* A variable which declare inside the local space or method are is called as local variable.
#* In the case of local variable , it can be access as well as odified inside the local space.

# a=10
# b=20
# def demo():
#     c=90
#     def demo2():
#         print(c)
#     demo2()
# demo()

# o/p ---> 90

#~ --------------------------------------------
# a=10
# b=20
# c=190
# def demo():
#     def demo2():
#         print(c)
#     demo2()
# demo()

# o/p -->190

#~ -----------------------------------------------
# a=10
# b=20
# c=190
# def demo():
#     nonlocal c
#     c=c+90
#     def demo2():
#         print(c)
#     demo2()
# demo()

# o/p -->280

#~ -----------------------------------------------------

# def f():
#     global a
#     print(a)
#     a='Hello'
# a='World'
# f()
# print(a)

#~ -----------------------------------------------------

# def f(x):
#     print('outer')
#     def f1(a):
#         print('inner')
#         print(a,x)
#     f1(x)
# f(3)
