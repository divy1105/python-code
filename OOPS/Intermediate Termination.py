
#! Intermediate Termination
#& 1. Continue - It is keyword which is used to skip a perticular iteration of the loop.
#^ 2. Break - It is a keyword which is used to terminate the loop prematurely based on the condition.
#^          - break keyword is used inside the loop along with if condition. and if the condition becomes true the loop will get terminated
#^          - loops else block will be only executed if the loop is not terminated by break keyword.

#! 1.
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

#! 2. 
# for i in range(1,11):
#     if i==7:
#         break
#     print(i)
# else:
#     print("i will be executed ")

#! 3. write a program to check if a given list is homogeneous or heterogenous.
# a=[10,12,4.3,True]
# for i in a:
#     if type(i) != type(a[0]):
#         print("heterogenous")
#         break
# else:
#     print("homogeneous")

#! 4. prime number using break
# n =int(input("enter a number:"))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")

#!5.  write a program to print all values except int data type from give list.
# a=[10,12,'holiday',3.4,True,'hii']
# for i in a:
#     if type(i) != int:
#         print(i)

#! 6. Write a program to convert int into binary

# num = int(input("Enter a number: "))

# binary = bin(num)

# print("Binary of", num, "is", binary[2:])

#! 7. Write a program to convert binary into int.

binary = input("Enter a binary number: ")

decimal = int(binary, 2)

print("Decimal of", binary, "is", decimal)