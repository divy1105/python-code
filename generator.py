
#! Generator:
# Generator are used to generate a sequence or collection of values.
# it is used in the concept of function.
# Instead of using return keyword we use yield keyword.
# yield will pause the execution of the function and return the value.
# Generator will return generator object

# Yield : 
# it will pause the execution.
# At last when no element is present then it will return collection.
# it return generator object.
# we can use malti yield keyword

# return :
# it will stop the execution.
# It  return value immediately.
# it return value.
# we can use only one return keyword.


# generator obj ----> actual value
# 1.Typecasting - list,set,tuple
# 2.next()

# def multiply(a,b):
#     yield a+b
#     yield a-b
#     yield a*b
#     yield a/b

# # print(set(multiply(10,20)))
# a = multiply(10,20)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# st='hello how are you and how was your day.?'
# def extract_vowels(st):
#     for i in st:
#         if i in 'aeiouAEIOU':
#             yield i

# res=extract_vowels(st)
# next(res)
# next(res)
# next(res)
# next(res)
# print(list(set(res)))

