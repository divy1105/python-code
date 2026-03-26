##1.
##n = eval(input("Enter a collection:"))
##
##if len(n) % 2 == 0:
##    print("Length is even")
##else:
##    print("Length is odd")

##2.

##data = eval(input("Enter a collection:"))  
##
##mutable_types = (list, dict, set)
##
##if isinstance(data, mutable_types):
##    print("Mutable datatype")
##else:
##    print("Immutable datatype")

##3.
##ch = input("Enter a character: ")
##
##if ch.isupper():
##    print("Uppercase character")
##elif ch.islower():
##    print("Lowercase character")
##elif ch.isdigit():
##    print("Digit")
##else:
##    print("Special character")

##4.
##data = eval(input("Enter a collection:"))  # you can change this list
##
##mid_index = len(data) // 2
##mid_value = data[mid_index]
##
##if isinstance(mid_value, str):
##    print("Middle value is a string:", mid_value)
##else:
##    print("Middle value is not a string")

##6.
##n = int(input("Enter a number: "))
##i = 1
##total = 0
##
##while i <= n:
##    total += i
##    i += 1
##
##print("Sum of", n, "natural numbers is:", total)

##7.
##num = int(input("Enter a number: "))
##sum_factors = 0
##
##for i in range(1, num + 1):
##    if num % i == 0:
##        sum_factors += i
##
##print("Sum of factors of", num, "is:", sum_factors)


##8.
##data = eval(input("Enter a collection:"))   
##
##result = []
##for x in data:
##    if isinstance(x, int) and x % 5 == 0 and 100 <= x <= 999:
##        result.append(x)
##
##print("Three-digit integers multiple of 5:", result)

##9.
##n = input("Enter a string:")
##s=0
##for i in n:
##    if i not in 'AEIOUaeiou':
##        s+=1
##print(s)

##10.
##text = input("Enter a string: ")
##result = ""
##
##for ch in text:
##    if 'A' <= ch <= 'Z':   # uppercase
##        result += chr(ord(ch) + 32)
##    elif 'a' <= ch <= 'z': # lowercase
##        result += chr(ord(ch) - 32)
##    else:
##        result += ch       # keep digits/special chars unchanged
##
##print("Converted string:", result)

##11.
##num = int(input("Enter a number: "))
##sum_div = 0
##
##for i in range(1, num):
##    if num % i == 0:
##        sum_div += i
##
##if sum_div == num:
##    print(num, "is a Perfect Number")
##else:
##    print(num, "is not a Perfect Number")

##12.
##text = input("Enter a string: ")
##result = ""
##
##for i in range(len(text)):
##    if i % 2 != 0:   # odd index
##        result += text[i]
##
##print("Characters at odd index:", result)

