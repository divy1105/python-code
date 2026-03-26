##1. Program to reverse a number
##num = int(input("Enter a number: "))
##rev = 0
##
##while num > 0:
##    digit = num % 10       
##    rev = rev * 10 + digit 
##    num = num // 10        
##
##print("Reversed number:", rev)

##2. Write a program to find sum of digits of a number using 
##while loop

##num = int(input("Enter a number: "))
##total = 0
##
##while num > 0:
##    digit = num % 10       
##    total += digit         
##    num = num // 10     
##
##print("Sum of digits:", total)

##3. Write a program to print sum of factors of a number
##num = int(input("Enter a number: "))
##i = 1
##sum = 0
##
##while i <= num:
##    if num % i == 0:       
##        sum += i   
##    i += 1
##
##print("Sum of factors of", num, "is:", sum)

##4. Write a program to get the following output
##a=’PytHON@12%’ 
##output=’PHONyt@%12’

##a = 'PytHON@12%'
##upper = "" 
##lower = ""
##special = ""
##digit = ""
##
##i = 0
##while i < len(a):
##    ch = a[i]
##    if ch.isupper():
##        upper += ch
##    elif ch.islower():
##        lower += ch
##    elif ch.isdigit():
##        digit += ch
##    else:
##        special += ch
##    i += 1
##
##output = upper + lower + special + digit
##print("Output:", output)

##5. Consider a character input  if it is uppercase convert into 
##lowercase , if it is lowercase convert into uppercase , if it 
##is a digit print the remainder when divided by 3 and if it is 
##a special character , print it’s ASCII value

##ch = input("Enter a character: ")
##
##if ch.isupper():
##    print("Converted:", ch.lower())
##
##elif ch.islower():
##    print("Converted:", ch.upper())
##
##elif ch.isdigit():
##    num = int(ch)
##    print("Remainder when divided by 3:", num % 3)
##else:
##    print("ASCII value:", ord(ch))

##6.  Write a program to print the middle value of the list only 
##if it the middle value is of string datatype
##my_list = eval(input("Enter a List:"))
##
##length = len(my_list)
##mid_index = length // 2   
##
##middle_value = my_list[mid_index]
##
##if isinstance(middle_value, str):
##    print("Middle value is a string:", middle_value)
##else:
##    print("Middle value is not a string.")

## 8.Program to print prime numbers between a and b (using for loop)
##a = int(input("Enter the starting number (a): "))
##b = int(input("Enter the ending number (b): "))
##
##for num in range(a, b + 1):
##    if num > 1:   
##        for i in range(2, int(num**0.5) + 1):
##            if num % i == 0:
##                break
##        else:
##            print(num, end=" ")

## 12. $ 
##     * $ 
##     * * $ 
##     * * * $ 
##     * * * * $ 
##   Write a program to get the above pattern
##n = 5   
##
##for i in range(1, n + 1):
##    for j in range(i-1):
##        print("*", end=" ")
##    print("$")


##13.
##d = {}
##
##for i in range(65, 91):
##    d[chr(i)] = i
##
##print(d)

##14.
##a='Python is easyi to learn'
##words=a.split()
##
##output={}
##for word in words:
##    if len(word) % 2 != 0:
##        output[word]=word[::-1]
##    else:
##        output[word]=len(word)
##
##print(output)


# 15.
# rows = 5   # number of rows
# ch = 65    # ASCII code for 'A'

# for i in range(1, rows + 1):
#     for j in range(i):
#         print(chr(ch), end=" ")
#         ch += 1
#     print()

# nested for loop and find subarray from given  list
# a=[10,20,30,40,50]

# for i in range(len(a)):
#     for j in range(i+1,len(a)+1):
#         print(a[i:j])
