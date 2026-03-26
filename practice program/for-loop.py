
#! For Loop Program

#~ 1. write a program to print natural numbers upto n

# a = int(input("enter the starting number: "))
# n = int(input("enter the ending number: "))

# for i in range(a,n):
#     print(i)

# --------------------------------------------------------------------------------------------------------------------------------

#~ 2. write a program to print even numbers upto n

# a = int(input("enter the starting number: "))
# n = int(input("enter the ending number: "))

# for i in range(a,n+1):
#     if i % 2 == 0:
#         print(i)

#! --------------------------------------or----------------------------------

# n = int(input("Enter the number:"))
# for i in range(2,n+1,2):
#     print(i)

#--------------------------------------------------------------------------------------------------------------------------------

#~ 3. write a program to reverse the string using for loop.

# a=input("Enter a String:")
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

#! -----------------------------or---------------------------

# a=input("Enter a String:")
# out=''
# for i in a:
#     out=i+out
# print(out)

# --------------------------------------------------------------------------------------------------------------------------------

#~ 4. write a program to access only characters present at odd index using for loop.

# a=input("Enter a String:")
# for i in range(1,len(a),2):
#     print(a[i])

# ----------------------or-----------------------

# a = input("Enter a String:")
# for i in range(len(a)):
#     if i % 2 != 0:
#         print(a[i])

# --------------------------------------------------------------------------------------------------------------------------------

#~ 5. write a program to reverse the number using for loop.

# n = (input("Enter the number:"))
# a=''
# for i in n[::-1]:
#     a+=i
# print(a)

# --------------------------------------------------------------------------------------------------------------------------------

#~ 6. write a program to count number of times a perticular character is repeated in a string using for loop.

# a=input("Enter a String:")
# n=input("Enter the character:")
# count=0
# for i in a:
#     if i == n:
#         count+=1
# print(count)

#~ 7. write a program to check if a given number is perfect number or not.(sum of all divisors is equal to the number itself).

# n = int(input("Enter the number:"))
# sum=0
# for i in range(1,n):
#     if n % i == 0:
#         sum+=i
# if sum==i:
#     print("it is a perfect number")
# else:
#     print("it is not a perfect number")

#~ 8. write a program to print factorial or a number using for loop.

# n=int(input("Enter the number:"))
# fact = 1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

#~ 9. Write a Program to check if a given number is prime or not.

# n = int(input("Enter the number:"))
# for i in range(2,n):
#     if n % i == 0:
#         print("It is not a prime number")
#         break
#else:
#    print("It is a prime number")

#! ---------or-----------

# n = int(input("Enter the number:"))
# counter=0
# for i in range(2,n):
#     if n % i == 0:
#         counter+=1
# if counter ==0:
#     print("It is a Prime number")
# else:
#     print("It is not prime number")

#~ 10. Write a program to check if a given list is homogoneous or heterogoneous.

# n=eval(input("Enter the number:"))
# counter=0
# for i in range(1,len(n)):
#     if type(n[0]) != type(n[i]):
#         counter+=1
# if counter==0:
#     print("It is a homogoneous list")
# else:
#     print("It is heterogoneous list")

#^ IMP
#~ 11.Write a program to remove the duplicate from the below list.[IMP]
# a = [12,34,56,34,34,8+9j,15,12]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

#~ 12.Create a list of cuble of numbers 1 to 30.

# n=30
# l = []
# for i in range(1,n+1):
#     l.append(i**3)
# print(l)

#~ 13.extract all the interger from the list which are multiple of 5 and is 3-digit number from list.
#~ input=[12,34,'lemon',50,200,9+8j,550]
#~ output=[200,550]

# l=[12,34,'lemon',50,200,9+8j,550]
# ans=[]
# for i in l:
#     if type(i) == int and i % 5 ==0 and len(str(i))==3:
#         ans.append(i)

# print(ans)


#! ------------or-----------

# l=[12,34,'lemon',50,200,9+8j,550]
# ans=[]
# for i in l:
#     if type(i) == int:
#         if i%5 == 0 and 100<=i<=999:
#             ans.append(i)
# print(ans)

#^ Theory questions
# 1.Explain range() along with the syntax
# 2.Advantages of for loop over while loop.
# 3.How to access the keys and values from a dictionary using for loop.


#~ 14. write a program to print fibonacci series using for loop.

# n=5
# a=0
# b=1
# print(a)
# print(b)

# for i in range(1,n-1):
#     print(a+b)
#     a,b = b,a+b

#!---------------or---------------------

# n=int(input("Enter the number:"))
# a=0
# b=1
# for i in range(1,n+1):
#     print(a)
#     a,b = b,a+b

#~15. write a program to print fibonacci series sum upto n.

# n=int(input("Enter the number:"))
# a=0
# b=1
# sum=0
# for i in range(0,n):
#     sum+=a
#     a,b = b,a+b
# print(sum)

#~ 16. write a program to find hcf of 2 numbers.

# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))

# hcf=1
# p=0
# if a>b:
#     p=b
# else:
#     p=a
# for i in range(2,p+1):
#     if a%i == 0 and b%i == 0:
#         hcf=i
# print(hcf)

#~ 17. write a program to find LCf of 2 numbers.

# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# p=0
# factors=[]
# if a>b:
#     p=b
# else:
#     p=a
# for i in range(2,p+1):
#     if a%i == 0 and b%i == 0:
#        factors.append(i)
# print(factors[0])

#~ 18. write a program to find using split function.
#~ s = 'example on for loop'
#~ out = 'ee on fr lp'

# a = 'example on for loop'
# out = ''
# s=a.split()
# for i in s:
#     out+=i[0]+i[-1]+' '

# print(out)

#~ 19. write a program to print
#~ a=' hii I am on holiday' 
#~ r1=['hi','holiday']
#~ r2=['I','am','on']


# a = ' hii I am on holiday'

# s = list(a.split())
# # print(s)
# for i in s:
#     r1=s[0]+' '+s[-1]
#     r2=s[1:-1]
# print(r1.split())
# print(r2) 

#! ------------or--------------

# a = ' hii I am on holiday'

# s = a.split()
# # print(s)
# for i in s:
#     r1=s[0]+' '+s[-1]
#     r2=s[1:-1]
# print(list(r1.split()))
# print(list(r2)) 

#~ 20. write a program to print following o/p
#~ input = ['hii','byee','holiday']
#~ output = {'hii':3,'byee':4,'holiday':7}

# l=['hii','byee','holiday']
# d ={}
# for i in l:
#     d[i] = len(i)

# print(d)

#~ 21. Write a program to print the following o/p
#~ input = 'python is easyi to learn'
#~ output = {'python':6,'is':2,'easyi':'iysae','to':2,'learn':'nrael'}

# s = 'python is easyi to learn'
# d={}
# b = s.split()
# for i in b:
#     if len(i) == 5:
#         d[i]=i[::-1]
#     else:
#         d[i]=len(i)
# print(d)

#! ------------or--------------

# s = 'python is easyi to learn'
# d={}
# b = s.split()
# for i in b:
#     if len(i) %2==0:
#         d[i]=len(i)
#     else:
#         d[i]=i[::-1]
# print(d)

#~ 22. Write a program to print the following o/p
#~ output = {'A':65,'B':66,......,'Z':90}

# d= {}
# for i in range(65,91):
#     d[chr(i)] = i
# print(d)

#! ------------or--------------

# d= {}
# for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#     d[i] = ord(i)
# print(d)

#~23. Write a program to print the following o/p
#~ input = [12,3.4,'hello',False,'bye','python',8+9j]
#~ output= {'hello':'ho','bye':'be','python':'pn'}

# l=[12,3.4,'hello',False,'bye','python',8+9j]
# d={}
# for i in l:
#     if type(i) == str :
#         d[i] = i[0]+i[-1]
# print(d)

#~ 24. Write a program to print the following o/p
#~ input = {'star':10,'byee':30,'moon':80}
#~ output = {10:'star',30:'byee',80:'moon'}

# d={'star':10,'byee':30,'moon':80}
# d1={}
# for i in d:
#     d1[d[i]]=i
# print(d1)

#! ---------or--------

# d={'star':10,'byee':30,'moon':80}
# d1={}
# for i in d:
#    key=i
#    value=d[i]
#    d1[value]=key
# print(d1)

#^ IMP
#~ 25. Write a program to print the following o/p
#~ input = ['red','black','yellow']
#~ output = ['c','red','c','black','c','yellow']

l = ['red','black','yellow']
d=[]
for i in l:
   d.append('c')
   d.append(i)
print(d) 