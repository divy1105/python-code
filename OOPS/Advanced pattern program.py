
#! pattern Programs

#~ ----------------------------------------------------------------------
#! Write a program to print the following pattern.
# * * * * * 
# *       * 
# *       *
# *       *
# * * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == 1 or j == 5 or i==1 or i==5 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
          
#     print()


#~ ---------------------------------------------------------------------------
# * * * * * * * * * * 
# * *     *       * * 
# *   *   *     *   *
# *     * *   *     *
# * * * * * * * * * *
# *       * *       *
# *     * *   *     *
# *   *   *     *   *
# * *     *       * *
# * * * * * * * * * *

# n=10
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i in(1,5,10) or j in (1,5,10) or i==j or i+j==n+1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
          
#     print()

#~ ---------------------------------------------------------------------------
 #! Write a program to print the following pattern.

# *       * 
#   *   *   
#     *
#   *   *
# *       *

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i+j==n+1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
          
#     print()

#~ ---------------------------------------------------------------------------
#! Write a program to print the following pattern.
# *
# * *       
# *   *
# *     *
# * * * * *

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i==5 or j==1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
          
#     print()

#~ ---------------------------------------------------------------------------
#! Write a program to print the following pattern.

# * * * * * 
#   *     * 
#     *   * 
#       * * 
#         * 

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i==1 or j==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
          
#     print()

#~ ---------------------------------------------------------------------------
#! Write a program to print the following pattern.

# *
# * *
# *   *
# *     *
# *   *   *
# * * * * * *

# n=6
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or i==6 or j==1 or (i==5 and j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
          
#     print()


#~ ---------------------------------------------------------------------------
#! Write a program to print the following pattern.

# *       * 
# *       * 
# * * * * *
# *       *
# *       *
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if  j==5 or j==1 or i==3:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
          
#     print()

#~ ---------------------------------------------------------------------------
#! Write a program to print the following pattern.
#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# n = 5
# for i in range(1, n+1):
#     for s in range(1,(n-i)+1):
#         print(" ",end=" ")
#     for j in range(1,i*2):
#         print("*",end=" ")
#     print()

#~ ---------------------------------------------------------------------------
#! Write a program to print the following pattern.

# * * * * * * * * * 
#   * * * * * * * 
#     * * * * *
#       * * *
#         *

# n = 5
# for i in range(n, 0, -1):
#     for s in range(1, n-i+1):
#         print(" ", end=" ")
#     for j in range(1, i*2):
#         print("*", end=" ")
#     print()

#~ ---------------------------------------------------------------------------
#! Write a program to print the following pattern.

#         * 
#       * * * 
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# n = 5

# for i in range(1, n):
#     for s in range(1, n-i+1):
#         print(" ", end=" ")
#     for j in range(1, i*2):
#         print("*", end=" ")
#     print()

# for i in range(n, 0, -1):
#     for s in range(1, n-i+1):
#         print(" ", end=" ")
#     for j in range(1, i*2):
#         print("*", end=" ")
#     print()
