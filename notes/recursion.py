
#! Recursion --->



#~ without Rreturn value.

# def fname(args):
#     if termination_condition:
#         return 
#     fname(args)
# fname(values)

#~ with return value.

# def fname(args):
#     if termination_condition:
#         return value
#     return fname(args)
# print(fname(values))

# note : The program in which we need to display the o/p or store the o/p 
# we will be using with return value syntax or else we will be using without return value syntax. 

#*Steps to Convert any while loop program into recursion.

#! step-1: Initialize of all the variables of looping should be done in function declaration.
#! step-2: Termination condition should be return Exectly opposite to the looping condition.In the format of if statement.
#! step-3: Return the total result inside the termination condition.
#! step-4: Logic of the program should be kept or return as it is.
#! step-5: Updation of looping variable should be done in recursive call.

#*   | sign  | Opposite  |
#*   |       |           |
#*   |   >   |   <=      |
#*   |   <   |   >=      |
#*   |   <=  |   >       |
#*   |   >=  |   <       |
#*   |   ==  |   !=      |
#*   |   !=  |   ==      |