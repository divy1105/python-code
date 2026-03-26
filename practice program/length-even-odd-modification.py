n = eval(input("Enter the number: "))

if len(n) % 2 == 0:
    print("The length of the number is even.")
else:
    print("The length of the number is odd.")
    a = len(n)//2  
    print("the index of mid value is :",n[a] )