
#! Exception Handling:

#* It is a process of handling the error in the program.

#* Error is two types:
#* 1. Syntax error
#* 2. logical error

#~ Syntax error                                   Exception error
#* It is generated because of incorrect syntax.    It is generated because of incorrect logic.
#* It is occured before execution.                It is occured during execution.
#* It is occured at compile time.                 It is occured at runtime.
#* It is idetified by interpreter.                It is identified by compiler not by interpreter.

#* keywords of exception:
#* 1. try
#* 2. except
#* 3. finally
#* 4. else

# try:
#     p =int(input("Enter the number: "))
#     n = eval(input("Enter the number: "))
#     r=10
#     si=(p*r*n)/100
#     print(si)
# except Exception as e:
#     print(e)


class MyException(Exception):
    pass
def food(item):
    try:
        if item == 'pizza':
            print("i am eating pizza")
        elif item == 'burger':
            print("i am eating burger")
        else:
            raise MyException("non-veg food")
    except MyException as e:
        print("exception is handled",e)
    
def main():
    food('egg')
if __name__ == '__main__':
    main()