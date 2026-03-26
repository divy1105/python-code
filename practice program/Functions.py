
#! function programs

#* 1.write a program to extract vowels from a string.

#! ----------------------------------------------------------------------
#~ 1. function without args and  without return .

# def vowel():
#     a=input("Enter a String:")
#     for i in a:
#         if i in 'AEIOUaeiou':
#             print(i)

# vowel()

#! ----------------------------------------------------------------------

#~ 2. function with args and  without return .
# def vowel(a):
#     out=[]
#     for i in a:
#         if i in 'AEIOUaeiou':
#             out.append(i)
#     print(out)
# vowel('yash')


#^ Number of arguments prsent in function declaration should be equal to number of value passed during function calling.

#& 1. create a fuction to count number of times a perticular character is repeated in a string.

# def count(a:str,n:str):
#     count=0
#     for i in a:
#         if i == n:
#             count+=1
#     print(count)

# count('yash','a')

#! isinstance()-> to check datatype of a variable.

# def count(a:str,n:str):
#     if isinstance(a,str) and isinstance(n,str):
#         count=0
#         for i in a:
#             if i == n:
#                 count+=1
#         print(count)
#     else:
#         print("Invalid Input")
# count('yash','a')
#! ----------------------------------------------------------------------

#~ 3. function without args and  with return .
# def add(a:int,b:int):
#     return a,b,a+b
#     print(a+b)

# a=(add(2,3))
# b=(add(4,5))

# print(a)
# print(b)

#! ex. 
# def demo():
#     return 'hii'
#     return 'hello'
# print(demo())
# a=demo()
# print(a)
#! ----------------------------------------------------------------------

#~ 4. function with args and  with return .

# make a function to check whether a number is prime number or not

# def prime(a:int):
#     for i in range(2,a):
#         if a%i==0:
#             return 'It is not a prime number'
#     else:
#         return 'It is  a prime number' 

# a=prime(13)
# print(a)

#! ----------------------------------------------------------------------

# create a function to check if a given number is strong number or not.if it is strong number is give true otherwise false.

# def isstrong(a:int):
#     sum=0
#     temp=str(a)
#     for i in temp:
#         fact=1
#         for j in range(1,int(i)+1):
#             fact*=j
#         sum+=fact
#     if sum==a:
#         return True
#     else:
#         return False
    
# a=isstrong(145)
# print(a)

#! ----------------------------------------------------------------------

# write a programe to move the target element at the first at given list.
# a = [1, 5, 8, 15, 70, 8]
# b = 8
# c = []
# for i in a:
#     if i == b:
#         c = [i] + c
#     else:
#         c = c + [i]

# print(c)

#! -----------or-------------------
# a = [1, 5, 8, 15, 70, 8]
# b = int(input("Enter a number: "))
# counter = 0
# for i in range(0,len(a)):
#     if a[i] == b:
#         a[counter],a[i] = a[i],a[counter]
#         counter+=1

# print(a)

# write a program to the end 0 from the list.
 
# a=[16,0,17,39,48,0,52,94,0]
# b=int(input("Enter a number:"))
# counter=-1
# for i in range(0,len(a)):
#     if a[i] == b:
#         a[counter],a[i] = a[i],a[counter]
#         counter-=1
# print(a)