
#! write a program to print the following pattern.

#        *
#      * *
#    * * *
#  * * * *
#* * * * *

# n=5
# for i in range(1,n+1):
#     for s in range(1,(n-i)+2):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


#! write a program to print the following pattern.

# * * * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *

# n=6
# for i in range(1,n+1):
#     for s in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,(n-i)+1):
#         print("*",end=" ")
#     print()

#^ -----------------or-------------------

# rows = 6
# for i in range(rows, 0, -1):
#     # Print leading spaces
#     print("  " * (rows - i), end="")
    
#     # Print stars
#     print("* " * i)

#~ --------------------------------------------------------------
#^ Write a program to print the following pattern.

# 65 66 67 68 69 
#    70 71 72 73 
#       74 75 76
#          77 78
#             79


# n=5
# start=65
# for i in range(1,n+1):
#     for s in range(1,i):
#         print(" ",end="  ")
#     for j in range(1,(n-i)+2):
#         print(start,end=" ")
#         start+=1
#     print()
#~ --------------------------------------------------------------

#^ write a program to print the following pattern.

# A B C D E 
#   F G H I 
#     J K L
#       M N
#         O


# n = 5
# start=65
# for i in range(1,n+1):
#     for s in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,(n-i)+2):
#         print(chr(start),end=" ")
#         start+=1
#     print()

#^ Write a program to print the following pattern.
# A B C D E 
#   E F G H 
#     H I J
#       J K
#         K

# n = 5
# start=65
# for i in range(1,n+1):
#     for s in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,(n-i)+2):
#         print(chr(start),end=" ")
#         start+=1
#     start-=1
#     print()

#& ------------------or-----------------------
# n = 5
# start = 65   
# for i in range(1, n + 1):
#     for s in range(1, i):
#         print(" ", end=" ")
#     temp = start   
#     for j in range(1, (n - i) + 2):
#         print(chr(temp), end=" ")
#         temp += 1
#     start = temp - 1
#     print()

#~ --------------------------------------------------------------

#^    12 13 14 15 
#^       23 24 25 
#^          34 35
#^             45

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i < j:
#             print(f"{i}{j}", end=" ")
#         else:
#             print("  ", end=" ")
#     print()

#& -------------------------------------------------------------------

#^ 21
#^ 31 32
#^ 41 42 43
#^ 51 52 53 54

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i > j:
#             print(f"{i}{j}", end=" ")
#         else:
#             print("  ", end=" ")
#     print()

#& --------------------------------------------------------------------

#^ 11
#^    22
#^       33
#^          44
#^            55
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == j:
#             print(f"{i}{j}", end=" ")
#         else:
#             print("  ", end=" ")
#     print()
 
#& ------------------------------------------------------------------------

#^ 11 12 13 14 15 
#^ 21 22 23 24 25 
#^ 31 32 33 34 35
#^ 41 42 43 44 45
#^ 51 52 53 54 55

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i < j:
#             print(f"{i}{j}", end=" ")
#         elif i == j:
#             print(f"{i}{j}", end=" ")
#         elif i > j:
#             print(f"{i}{j}", end=" ")
#         else:
#             print("  ", end=" ")
#     print()

#~ ------------------------------------------------------------

#^ 1 
#^ 2 3 
#^ 4 5 6
#^ 7 8 9 10
#^ 11 12 13 14 15

# n=5
# start = 1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i >=j:
#             print(start,end=" ")
#             start+=1
#     print()

#~ --------------------------------------------------------------

# n=5 
# start = 1

# for i in range(1, n+1):
#     for j in range(n-i+1):
#         print(start, end="  ")
#         start += 1
#     print()

#~ ---------------------------------------------------------------


# 10000
# 01000
# 00100
# 00010
# 00001

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i == j:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()

#~ ----------------------------------------------------------

#^ 65 66 67 68 69 
#^    70 71 72 73 
#^       74 75 76
#^          77 78
#^             79

# n=5
# start = 65
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i <= j:
#             print(start, end=" ")
#             start+=1
#         else:
#             print("  ", end=" ")
#     print()

#~ ------------------------------------------------------------

#^ 65 66 67 68 69 
#^ 70 71 72 73 
#^ 74 75 76
#^ 77 78
#^ 79

# n = 5
# num = 65

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i + j <= n + 1:  
#             print(num, end=" ")
#             num += 1
#     print()

#~ -------------------------------------------------------------

#^ D E F G H 
#^ H I J K 
#^ K L M
#^ M N
#^ N

# n = 5
# num = 68

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i + j <= n + 1:  
#             print(chr(num), end=" ")
#             num += 1
#     num-=1
#     print()

#! ------------------or--------------------------

#^ D E F G H 
#^ H I J K 
#^ K L M
#^ M N
#^ N

# n = 5
# num = ord("D")

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i + j <= n + 1:  
#             print(chr(num), end=" ")
#             num += 1
#     num-=1
#     print()

#~ ---------------------------------------------------------------

#^ D E F G H 
#^ I J K L 
#^ M N O
#^ P Q
#^ R

# n = 5
# num = ord("D")

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i + j <= n + 1:  
#             print(chr(num), end=" ")
#             num += 1
#     print()

#~ ---------------------------------------------------------------

n = 5
num = ord("D")

for i in range(1, n+1):
    for j in range(1, n+1):
        if i + j <= n + 1:  
            print(chr(num), end=" ")
            num += 1
        else:
            print(" ", end=" ")
    print()
