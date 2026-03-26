
#~ 1  write a program to find a student by there percentage. 
#~     80% + --> Class I
#~     60-80% --> Class II
#~     Below% --> Class III /

# n = eval(input("Enter the percentage:"))

# if n >= 80 :
#     print("Class I")
# elif n > 60 & n < 80:
#     print("Class II")
# else :
#     print("Class III")

# --------------------------------------------------------------------------------------------------------------------------------
#~ 2   write a program to find a number have single digit,two digit ,three digit and continue 
#     0-9 --> s.d
#     10-99 --> d.d
#     100-999 --> t.d
#     >999 --> m.d 

# n = int(input("Enter the digit:"))

# if n<0:
#     print("negative number")
# elif n >= 0 and n <= 9:
#     print("single Digit")
# elif n >= 10 and n <= 99:
#     print("Double digit")
# elif n>= 100 and n<=999 :
#     print("Triple digit")
# else:
#     print("multiple digit")

# --------------------------------------------------------------------------------------------------------------------------------
#~ 3. write a program to check if the given character is upper,lower,special character,digit

# n = input("enter a character:")
# if n in ['A-Z']:
#     print("upper case")
# else n in ['a-z']:
#     print("lower case")
# elif n in [0-9]:
#     print("digits")
# else:
#     print("special character")

# --------------------------------------------------------------------------------------------------------------------------------
#~ 4. find a number  which is greatest between 2 number

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# if a > b:
#     print(f"a is greater {a}")
# else:
#     print(f"b is greater {b}")

# --------------------------------------------------------------------------------------------------------------------------------
#~ 5. find a number  which is greatest between 3 number.

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# if a > b and a > c:
#     print(f"{a} is greater")
# elif b>a and b>c:
#     print(f"{b} is greater")
# else:
#     print(f"{c} is greater ")

# --------------------------------------------------------------------------------------------------------------------------------
#~ 6. write a program to check is givern character is vowel or consonant.

# a = input("Enter a character: ")
# if len(a) == 1 and ('A'<=a<='Z' or 'a'<=a<='z'):
#     if a in 'AEIOUaeiou':
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("Invalid input please enter a single character")

# --------------------------------------------------------------------------------------------------------------------------------
#~ 7.write a program to login into instagram by entering correct username and password

# Username = "abc123"
# Password = "abc@2000"

# a = input("Enter your username: ")
# b = input("Enter your password: ")

# if a == Username:
#     if a == Username and b == Password:
#         print("Login successful")
#     else:
#         print("Incorrect password")
# else:
#     print("Incorrect username")

# --------------------------------------------------------------------------------------------------------------------------------
#~ 8. write a program to print the reverse string only if it is starting vowel and ending consonant and having a middle value

# a = input("Enter a string: ")

# if a[0] in 'AEIOUaeiou':
#     if a[-1] not in 'AEIOUaeiou':
#         if len(a) % 2 != 0:   # ensure middle exists
#                 print("Reversed string:", a[::-1])
#         else:
#                 print("String too short for middle value")
#     else:
#             print("not consonant")
# else:
#         print("not vowel")
    
# --------------------------------------------------------------------------------------------------------------------------------
#~ 9. write a program to find greatest number between 3 number using nested if only

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# if a >= b:
#     if a >= c:
#         print(f"a is greater {a}")
#     else:
#         print(f"c is greater {c}")
# else:
#     if b >= c:
#         print(f"b is greater {b}")
#     else:
#         print(f"c is greater {c}")

# --------------------------------------------------------------------------------------------------------------------------------
#~ 10. write a program to find greatest number between 4 number using nested if only

# a= int(input("Enter a as the first number: "))
# b= int(input("Enter b as the second number: "))
# c= int(input("Enter c as the third number: "))
# d= int(input("Enter d as the fourth number: "))

# if a >= b:
#     if a >= c:
#         if a >= d:
#             print(f"a is greater {a}")
#         else:
#             print(f"d is greater {d}")
#     else:
#         if c>=d:
#             print(f"c is greater {c}")
#         else:
#             print(f"d is greater {d}")
# else:
#     if b>=c:
#         if b>=d:
#             print(f"b is greater {b}")
#         else:
#             print(f"d is greater {d}")
#     else:
#         if c>=d:
#             print(f"c is geater {c}")
#         else:
#             print(f"d is greater {d}")
        
# --------------------------------------------------------------------------------------------------------------------------------
#~ 11. write a program to print python for using while loop

# i = 0
# while i<10:
#     print("python")
#     i+=1

# --------------------------------------------------------------------------------------------------------------------------------
#~ 12. write a program to print natural numbers upto n

# n = int(input("enter the number for loop: "))

# i=1
# while i<=n:
#     print(i)
#     i+=1

# --------------------------------------------------------------------------------------------------------------------------------
#~ 13. write a program to print even numbers upto 20

# i = 2
# while i<=20:
#     print(i)
#     i+=2
    
# #! ---------------------or-----------------------

# i=1
# while i<=20:
#     if i%2==0:
#         print(i)
#     i+=1

# --------------------------------------------------------------------------------------------------------------------------------
#~ 14. write a program to print characters from string and take user input.

# a= input("Enter a string:")
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1

# --------------------------------------------------------------------------------------------------------------------------------
#~ 15. write a program to reverse the string using while loop.

# a = input("Enter a string:")
# out=''

# i = 0
# while i<len(a):
#     out = a[i]+out
#     i+=1
# print(out)

#! ----------------------or---------------------

# a = input("Enter a string:")
# out= ''

# i = len(a)-1
# out = ''
# while i>=0:
#     out = out+a[i]
#     i-=1
# print(out)

# --------------------------------------------------------------------------------------------------------------------------------
#~ 16. write a program to print palindrome using while loop.

# a = input("Enter a string:")
# out=''

# i = 0
# while i<len(a):
#     out = a[i]+out
#     i+=1
# if out == a:
#     print(f"it is a palindrome : {a}")
# else:
#     print(f"it is not a palindrome : {a}")

# --------------------------------------------------------------------------------------------------------------------------------

 #~ 17. write a program to reverse the number using while loop.  

# n = int(input("Enter the number :"))

# out=0
# while n>0:
#     r = n%10
#     out = out*10 + r
#     n = n//10
# print(out)

#! ----------------------or---------------------


# n=int(input("Enter the number :"))

# out=''
# temp=str(n)
# i=0
# while i<len(temp):
#     out=temp[i]+out
#     i+=1
# out=int(out)
# print(out)

# --------------------------------------------------------------------------------------------------------------------------------
#~ 18. write a program to find sum of digits of a number using while loop.

# n = int(input("Enter the number :"))

# out=0
# while n>0:
#     r = n%10
#     out = out+r
#     n = n//10
# print(out)

# --------------------------------------------------------------------------------------------------------------------------------
#~ 19. write a program to get following output.
#~ input is n = 'PyTHon@123'
#~ so find count of upper case letter,lower case letter,digit and special character.

#! n = 'PyTHon@123'

#* upper=3
#* lower=3
#* digit=3
#* special=1

# n = input("Enter the string :")
# upper=0
# lower=0
# digit=0
# special=0

# i=0
# while i<len(n):
#     if 'A'<=n[i]<='Z':
#         upper+=1
#     elif 'a'<=n[i]<='z':
#         lower+=1
#     elif '0'<=n[i]<='9':
#         digit+=1
#     else:
#         special+=1
#     i+=1
# print('upper :',upper)
# print('lower :',lower)
# print('digit :',digit)
# print('special :',special)

# --------------------------------------------------------------------------------------------------------------------------------
#~ 20. write a program to get following output.
#~ input is n = 'PyTHon@123'
#~ so find count of upper case letter,lower case letter,digit and special character.

#! n = 'PyTHon@123'

#^ upper=['P','Y','T']
#^ lower=['h','o','n']
#^ digit=['1','2','3']
#^ special=['@']

# n = input("Enter the string :")
# upper=[]
# lower=[]
# digit=[]
# special=[]

# i=0
# while i<len(n):
#     if 'A'<=n[i]<='Z':
#         upper.append(n[i])
#     elif 'a'<=n[i]<='z':
#         lower.append(n[i])
#     elif '0'<=n[i]<='9':
#         digit.append(n[i])
#     else:
#         special.append(n[i])
#     i+=1
# print('upper :',upper)
# print('lower :',lower)
# print('digit :',digit)
# print('special :',special)

# --------------------------------------------------------------------------------------------------------------------------------
#~ 21. n = 'PyTHon@123'
#~output is yonPTH123@

#! n = 'PyTHon@123'

#^ lower=''
#^ upper=''
#^ digit=''
#^ special=''

# i=0
# while i<len(n):
#     if 'A'<=n[i]<='Z':
#         upper = upper+n[i]
#     elif 'a'<=n[i]<='z':
#         lower = lower+n[i]
#     elif '0'<=n[i]<='9':
#         digit = digit+n[i]
#     else:
#         special = special+n[i]
#     i+=1
# print(lower+upper+digit+special)

# --------------------------------------------------------------------------------------------------------------------------------
#~ 22. write a program to print all divisors of a perticular number.

# n = int(input("Enter the number :"))
# i = 1
# while i<=n:
#     if n % i == 0:
#         print(i)
#     i+=1

#--------------------------------------------------------------------------------------------------------------------------------
#~23. write a program to check if a given number is perfect number or not.

# n= int(input("Enter the number:"))
# i=1
# sum=0
# while i<n:
#     if n % i == 0:
#         sum+=i
#     i+=1
# if sum==n:
#     print("it is a perfect number")
# else:
#     print("it is not a perfect number")

# --------------------------------------------------------------------------------------------------------------------------------
#~ 23. write a program to etract only int datatype from the below list.

# l=['python',3+8j,12,True,32]
# ans=[]
# i=0
# while i<len(l):
#     if type(l[i]) == int:
#         ans.append(l[i])
#     i+=1
# print(ans)

# --------------------------------------------------------------------------------------------------------------------------------
#~ 24. write a program to Print all the numbers divisible by 5 between a and b with while loop.

# a= int(input("Enter a as the first number:"))
# b= int(input("Enter b as the second number:"))

# while a<=b:
#     if a % 5 == 0:
#         print(a)
#     a+=1

# --------------------------------------------------------------------------------------------------------------------------------
#~ 25. Write a program to print total no of digits of present in a particular number 

#! Ex - 125
#^ Output - 3

# a = int(input("Enter the number:"))
# count = 0
# while a>0:
#     count+=1
#     a=a//10
# print(count)

# --------------------------------------------------------------------------------------------------------------------------------
#~ 26.Write a program to find sum of all even number upto n

n = int(input("Enter the number:"))
sum=0
i=1
while i<=n:
    if i%2 == 0:
        sum+=i
    i+=1
print(sum)