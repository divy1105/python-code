
#! It is a preocess of creating a new collectionusing single line of code.
#! It is only applicatable for mutable collections.
#~ 1. list comprehension
#~ 2. set comprehension
#~ 3. dictionary comprehension

#~ 1. list comprehension - 
#* It is a process of creating a new list using single line of code.

#! Syntax :
#* var = [var for var in collection]
#* var = [ var for var in collection if condition]
#* var = [T.S.B if condition else F.S.B for var in collection]
#* var = [val1,val2 for val1,val2 in zip(collection1,collection2)]
#* var = [val1,val2 for val1 in collection1 for var2 in collection2]

#! Programs:
#$ 1.write a program to create list on 1 to 20.

#@ normal
# out =[]
# for i in range(1,21):
#     out.append(i)
# print(out)

#@ list comprehension
# out = [i for i in range(1,21)]
# print(out)

#$ 2.write a program to create list consists of squares of each and every intergeter between 1 to 20 only if it is multiple of 3.

#@ normal
# out =[]
# for i in range(1,21):
#     if i%3==0:
#         out.append(i**2)
# print(out)

#@ list comprehension
# out = [i**2  for i in range(1,21) if i%3==0]
# print(out)

#$ 3.write a program to store the square of the number between 1 to 20 if is divisiable by 4 or else store the cube.

#@ normal
# out =[]
# for i in range(1,21):
#     if i%4==0:
#         out.append(i**2)
#     else:
#         out.append(i**3)
# print(out)

#@ list comprehension
# out = [i**2 if i%4==0 else i**3 for i in range(1,21)]
# print(out)

#$ 4.write a program to get the following output.
# a= [(A,1),(A,2),(B,1),(B,2),(C,1),(C,2)]

#@ normal
# a="ABC"
# b=[1,2]
# out=[]
# for i in a:
#     for j in b:
#         out.append((i,j))
# print(out)

#@ list comprehension
# l = [(i,j) for i in "ABC" for j in range(1,3)]
# print(l)

#! -----------------or----------------
# l = [(i,j) for i in "ABC" for j in [1,2]]
# print(l)

#$ 5.write a program to extract string from the list only if it is palidrome.
# a=["hii",100,3.2,"madam","appa","bye"]

#@ normal
# out =[]
# for i in a:
#     if type(i)==str:
#         if i==i[::-1]:
#             out.append(i)
# print(out)

#@ list comprehension
# out = [i for i in a if type(i)==str and i==i[::-1]]
# print(out)

#$ 6.write a program to get the following output.
# s="programs based open comprehension happy"
# out=['programs','bd','open','cn','hy']

#@ normal
# out=[]
# for i in s.split():
#     if len(i)%2==0:
#         out.append(i)
#     else:
#         out.append(i[0]+i[-1])
# print(out)

#@ list comprehension
# out = [i if len(i)%2==0 else i[0]+i[-1] for i in s.split()]
# print(out)

#! zip() - It is used to itrate over multiple collection at once.

#! Syntax: for var1,var2.... in zip(collection1,collection2....collectionN)

#! Program:

# students=['A','B','C']
# marks=[90,80,70,60]
# d={}
# for i,j in zip(students,marks):
#     d[i]=j
# print(d)

#! 2. program extract string if it has palidrome.
# l=['hii',100,3.2,"madam","appa","bye"]

# out = [i for i in l if type(i)==str and i==i[::-1]]
# print(out)

#! 3. program to get the following output.
# s="programs based open comprehension happy"

# out = [i if len(i)%2==0 else i[0]+i[-1] for i in s.split()]
# print(out)

#! 4. program to get the following output.
# out=[('A',1),('A',2),('A',3),('B',1),('B',2),('B',3)]

# out = [(i,j) for i in "AB" for j in range(1,4)]
# print(out)

#! 5. program to get the following output.
# temp=[0,20,37,100]
# F=(C*9/5)+32

# out=[(i*9/5)+32 for i in temp]
# print(out)

#! 6. program to get the following output.
students = ["Ananya", "Rohit", "Sneha","Aarav","Meera","Karan","Isha","Vivek", "Tanya","Rahul"]

marks = [85, 72, 90, 67, 88,76, 95, 60, 82, 78]

## 1. Extract the names of students whose names start with A

## 2. Give a list consisting the name followed by the marks of  particular student

## 3. list of the names of students getting more than average marks

## 4. Create a list of grades (`"A"`, "B", `"C"`) for each student based on their marks:

# - A → Marks ≥ 85
# - B → 70 ≤ Marks < 85
# - C → Marks < 70

#! 1.
# out = [i for i in students if i.startswith("A")]
# print(out) 

#^ ------------------or---------------
# out = [i for i in students if i[0]=='A']
# print(out)

#! 2.
# out = [(i,j) for i,j in zip(students,marks)]
# print(out)

#! 3.
# avg = sum(marks)/len(marks)
# a=[i for i,j in zip(students,marks) if j>avg]
# print(a)


#^ ------------------or---------------
#! 3.
# sum=0
# for i in marks:
#     sum+=i
# avg=sum/len(marks)
# a=[i for i,j in zip(students,marks) if j>avg]
# print(a)

#! 4.
# out = ["A" if i>85 else "B" if i>70 else "C" for i in marks]
# print(out)

#^ ------------------or---------------

#!4.
# a=[i for i,j in zip(students,marks) if j>=85]
# b=[i for i,j in zip(students,marks) if j>=70 and j<85]
# c=[i for i,j in zip(students,marks) if j<70]
# print(a,b,c)

#~ 2. set comprehension - creating new set using single line of code is called set comprehension.

#* Syntax a. var = {var for var in collection}
#*        b. var = {var for var in collection if condition}
#*        c. var = {T.S.B if condition else F.S.B for var in collection}
#*        d. var = {val1,val2 for val1,val2 in zip(collection1,collection2)}
#*        e. var = {val1,val2 for val1 in collection1 for var2 in collection2}

#~ 3. Dictionary comprehension - creating new dictionary using single line of code is called dictionary comprehension.

#* Syntax a. var = {key:val for key in collection}
#*        b. var = {key:val for key in collection if condition}
#*        c. var = {kry:val1 if conditon else val2 for key in collection}
#*        d. var = {key:val for var1,var2 in zip(collection1,collection2)}
#*        e. var = {key:val for var1,var2 in zip(collection1,collection2) if condition}

#~ Type - a:

#^ 1. write a program to get Following output.
#^ {1:1,2:4,3:9,4:16,5:25}

# d = {i:i**2 for i in range(1,6)}
# print(d)

#~ Type - b:

#^ 2. write a program to get following output.
#z = 'hello baby are you fine'
#^ output = {'hello':5,'are':3,'you':3}

# d = {i:len(i) for i in z.split() if len(i)%2!=0}
# print(d)

#~ Type - c:

#^ 3. write a program to get following output.
# i = ['nayan','abcd','data','appa']
# output = {'nayan':5,'abcd':'dcba','data':'atad','appa':'4}

# d = {i:len(i) if i==i[::-1] else i[::-1] for i in i}
# print(d)

#~ Type - d:

#^ 4. write a program to get following output.
# a = [1,2,3]
# b=[4,5,6]
# output={1:4,2:5,3:6}

# d={a:b for a,b in zip(a,b)}
# print(d)

#^ normal
#^ 5. write a program to get following output.
# output = {1:1,2:4,3:27,4:16,5:125,6:36,7:343,8:64,9:729,10:100}

# d={i:i**2  if i%2==0 else i**3 for i in range(1,11)}
# print(d)

#! ----------------------program------------------------------

#^ 1. From string "Python" , create a dictionary where key = character, value = ASCII value.

# s = 'Python' 
# d = {char:ord(char) for char in s}
# print(d)

#^ 2. Given  nums = [10, -5, 8, -3, 0, 12] , create a dictionary with key = number,value = "Positive" only for positive numbers.

# nums = [10, -5, 8, -3, 0, 12]

# output = {num: "Positive" for num in nums if num > 0}
# print(output)

#^ 3. Get the following output
a=["Apple", "Banana", "Cherry", "Dates","Orange","Ice apple"]
# output={'Apple':"A","Banana":"b","Cherry":"c","Dates":"D","Orange":"O","Ice apple":"I"}

# d={i:chr(ord(i[0])+32) if len(i)%2==0 else i[0] for i in a}
# print(d)

