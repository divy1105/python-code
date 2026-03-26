
#! write a program to given number is even or not.

# class simple:
#     @staticmethod
#     def even(num):
#         if num%2==0:
#             print("Number is even")
#         else:
#            print("Number is not even")
    
# num = int(input("Enter a number:"))
# simple.even(num)

#~ ----------------lambda function-----------------------------
# n = int(input("Enter a number:"))
# even = lambda n:print("Number is even") if n%2==0 else print("Number is not even")
# even(n)

#! 2. write a program to check palidraom or not.
# def palindrome(n):
#     if str(n) == str(n)[::-1]:
#         print("Number is palindrome")
#     else:
#         print("Number is not palindrome")

# n = int(input("Enter a number:"))
# palindrome(n)


#~---------------------lambda function--------------------------
# n = int(input("Enter a number:"))
# palindrome = lambda n:print("Number is palindrome") if str(n) == str(n)[::-1] else print("Number is not palindrome")
# palindrome(n)

#! 3. write a program to check if a string starts with vowel and ends which consonent.

# string = input("enter a string:")
# vowels = lambda string:string[0] in 'AEIOUaeiou' and string[-1] not in 'AEIOUaeiou'
# print(vowels(string))

#! 4. write a program to square of all elements in a list using map().

# list1 =[2,5,6,7,8,9]
# func = lambda n:n**2
# result = list(map(func,list1))
# print(list(result))

#~ -----------------------------------------
# input = ['abcd','start','data','science']
# func = lambda n:len(n)
# output = list(map(func,input))
# print(output)

# output=[4,5,4,7]

#~------------------or--------------------

# print(list(map(lambda n:len(n),['abcd','start','data','science'])))

#!-------------------------------------------

# input = 'hi hello how are you'
# print(list(map(lambda n:n[0]+n[-1],input.split())))

# output=['hi','ho','hw','ae','yu']
