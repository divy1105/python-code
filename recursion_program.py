
# write a program to find factorial of a number using while loop.

#! Normal
# n = int(input("Enter a number:"))
# fact = 1
# while n>0:
#     fact = fact*n
#     n-=1
# print(fact)

#! Recursion

# def factorial(n,fact=1):
#     if n<=0:
#         return fact
#     return factorial(n-1,n*fact)

# print(factorial(5))


# write a program to extract only int datatype from the list.

#! normal
# l = [16,18.32,"hii",100,3.2,"bye",200,300]
# out=[]
# for i in l:
#     if type(i)==int:
#         out.append(i)
# print(out)

#! recursion
# def extract_int(l, result=None):
#     if result is None:
#         result = []
#     if len(l) == 0:
#         return result
#     if type(l[0]) == int:
#         result.append(l[0])
#         return extract_int(l[1:], result)
#     else:
#         return result + extract_int(l[1:], [])

# l=[16,18.32,"hii",100,3.2,"bye",200,300]
# print(extract_int(l))

# write  to print fibonacci numbers upto n. (while loop)

#! normal
# n= int(input("Enter the number:"))
# a=0
# b=1
# i=0
# print(a)
# print(b)
# while i<n:
#     print(a)
#     a+=b
#     a,b=b,a
#     i+=1

#! Recursion

# def fibonacci(n,a=0,b=1,i=0):
#     if i >= n:
#         return
#     print(a)
#     fibonacci(n,b,a+b,i+1)          

# fibonacci(10)

#~ Eg. 1. write a program to get following output.
#~ a = [1,3,5,7]
#~ target = 3       target = 4
#~ output = 1       output = 2

#! normal
# a = [1, 3, 5, 7]
# target = int(input("Enter the number:"))
# closest_index = None
# closest_diff = float('inf')
# for i in range(len(a)):
#     if a[i] == target:
#         print(i)
#         break
#     else:
#         diff = abs(a[i] - target)
#         if diff < closest_diff:
#             closest_diff = diff
#             closest_index = i + 1
# if closest_index is not None:
#     print(f"The closest number to {target} is {a[closest_index - 1]} at index {closest_index }")
# else:
#     print(f"The target number {target} is not in the list")

a = [1, 3, 5, 7]
target = int(input("Enter the number:"))
closest_index = None
closest_diff = float('inf')
for i, num in enumerate(a):
    diff = abs(num - target)
    if diff < closest_diff:
        closest_diff = diff
        closest_index = i
if closest_index is not None:
    if closest_index == len(a) - 1:
        print(f"The target number {target} is not in the list")
    else:
        print(f"The closest number to {target} is {a[closest_index]} at index {closest_index + 1}")
else:
    print(f"The target number {target} is not in the list")
