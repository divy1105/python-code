
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

# t =('katerina','karina','yalina','sizuka','tuntunm')
# def extract_odd(t):
#     for i in t:
#         if (len(i))%2==1:
#             yield i

# res = extract_odd(t)
# print(next(res))

#key(i):len(key)
# t =('katerina','karina','yalina','sizuka','tuntunm')
# def count_ele(t):
#     for i in t :
#         yield i,len(i)
# print(dict(count_ele(t)))

#key(i):len(key)
# t =('katerina','karina','yalina','sizuka','tuntunm')
# def count_ele(t):
#     for i in t :
#         yield i[0]+i[-1],i
# print(dict(count_ele(t)))

# t =('katerina','iarina','yalina','eizuka','tuntunm')
# def count_ele(t):
#     for i in t :
#         if i[0] not in 'aeiouAEIOU':
#             yield i[0],i
# print(dict(count_ele(t)))

#! square root
# a=[25,36,49,81,9,16]
# def sqrt(a):
#     for i in a:
#         yield int(i**0.5)

# print((list(sqrt(a)))) #[5, 6, 7, 9, 3, 4]

#! word:len(word)
# l=['instagram','facebook','twitter','whatsapp','meta','oracle']
# def word_len(l):
#     for i in l:
#         yield (i,),len(i)

# print(dict(word_len(l)))  #{('instagram',): 9, ('facebook',): 8, ('twitter',): 7, ('whatsapp',): 8, ('meta',): 4, ('oracle',): 6}

#! generate onlu numeric value in given list.
# l=['flipcart','amazon',78,[2,3,4],78,9.87,(5,3),45.36]

# def numeric(l):
#     for i in l:
#         if type(i) in [int,float,complex,bool]:
#             yield i

# print(list(numeric(l))) #[78, 78, 9.87, 45.36]

#! generate the first letter of the word as key and words starting with letter as value.
s='python is a programming language and programming is part of life'
# def first_letter(s):
#     result = {}
#     for word in s.split():
#         if word[0] not in result:
#             result[word[0]] = [word]
#         else:
#             result[word[0]].append(word)
#     return [{k: v} for k, v in result.items()]

# print(first_letter(s))

    