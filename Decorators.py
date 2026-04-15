
#! Decorators

#* Decorators are functions that are used to modify the behaviour of other functions.

# def outer(func): #func=main address
#     def inner():
#         # pretask
#         print("i am performing task")
#         func() #main
#         # posttask
#         print("task completed")
#     return inner
# @outer
# def main():
#     print("Hello")
# main() #inner()     main=inner address


#! write a program to take 2 number and perform division operation but before to perform division we need to check first number is grater then second number if notthen swap the numberand perform operation.and us of decorator

# def check(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         func(a,b)
#         print("Division completed")
#     return inner

# @check
# def main(a,b):
#     print(a//b)

# main(10,20)


#! write a program to pass positional arg, keyword arg and print both positional and keyword arg.but before that print the length of positional arg.

def check(func): #func = main address
    def inner(*args,**kwargs):
        print("length of positional argument")
        print(len(args)) # 2
        func(*args,**kwargs) # main((49,50),{a=10,b=20})
        print("operation completed")
    return inner

@check 
def main(*args,**kwargs): #args=(49,50),kwargs={'a':10,'b':20}
    print(args,kwargs) # (49, 50) {'a': 10, 'b': 20}

main(49,50,a=10,b=20) #inner(49,50,a=10,b=20)