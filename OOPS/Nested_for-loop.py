
#! 1. basic program

# a = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# counter=0
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         print(i,j)
#         counter+=1
#     print()
# print("The Counter is:" , counter)

#! 2.
# n =int(input("Enter a number:"))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,"|",j,"|",i*j)
#     print()

#! 3. write a program to print perfect number .
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     counter = 0
#     for j in range(1,i):
#         if i%j == 0:
#             counter+=j
#     if counter == i:
#         print(i)

#! 4. write a program to print strong number.
#^ sum of factorial off every digit is equal to original number.
#^ eg.145 = 1! + 4! + 5!
#^       = 1 + 24 + 120
#^       = 145

# n = int(input("Enter a number: "))
# sum=0
# for i in str(n):
#     num=int(i)
#     fact= 1
#     for j in range(1,num+1):
#         fact=fact*j
#     sum+=fact
# if sum==n:
#     print("Strong number")
# else:
#     print("Not a strong number")

#! 5. write a program to print strong number upto n.

# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     sum = 0
#     temp = i
#     while temp > 0:
#         digit = temp % 10
#         fact = 1
#         for j in range(1, digit+1):
#             fact *= j
#         sum += fact
#         temp //= 10
#     if sum == i:
#         print(i, end=' ')

#! 6. Write a program to print armstrong number or not.

# n = int(input("Enter a number:"))
# temp=str(n)
# sum=0

# for i in temp:
#     sum += int(i)**len(temp)
# if sum == n:
#     print(n,'Is a Armstrong Number')
# else:
#     print(n,'Is not a Armstrong Number')

#! 7. Write a program to print armstrong number or not upto n.

# n = int(input("Enter a number:"))
# for i in range(1,n+1):
#     temp=str(i)
#     sum=0
#     for j in temp:
#         sum += int(j)**len(temp)
#     if sum == i:
#         print(i)


#! 8. Write a program to print prime number upto n.

# n = int(input("Enter a number: "))
# out = []

# for i in range(2, n+1):
#     is_prime = True
#     for j in range(2, int(i**0.5) + 1):  
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(i)
#         out.append(i)   

# print("Prime numbers up to", n, ":", out)

#! 9. Write a program to find sum of factorial of only intergers from the given list.
# a = [5,True,'hii',3,9.6,2]
# # out=128
# fact=0
# sum=0
# for i in a:
#     if type(i)== int:
#         fact=1
#         for j in range(1,i+1):
#             fact=fact*j
#         sum+=fact
# print("the sum is:",sum)

#! 10. write a program to extract only perfect numbers from the given list.
# b=[6,12,28,44,60]
# out=[]
# for i in b:
#     counter=0
#     for j in range(1,i):
#         if i%j==0:
#             counter+=j
#     if counter==i:
#         out.append(i)
# print(out)


#! 11. Write a program to extract only prime number.
# a = [7,3,12,15,17]
# b = []

# for i in a:
#     for j in range(2, int(i**0.5) + 1):  
#         if i % j == 0:
#             break
#     else:
#         b.append(i)
# print("prime number is:", b)

# ----------------------or---------------------
# a=[7,3,12,15,17]
# out=[]
# for i in a:
#     sum=0
#     for j in range(2,i):
#         if i%j==0:
#             sum+=1
#     if sum==0:
#         out.append(i)
# print(out)