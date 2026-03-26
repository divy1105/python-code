
# ! 1. write a program to extract int datatype from the list.
# l =[16,18.32,"hii",100,3.2,"bye",200,300]
# out=[]
# for i in l:
#     if type(i)==int:
#         out.append(i)
# print(out)

#* ------------------------------------------------
# l =[16,18.32,"hii",100,3.2,"bye",200,300]
# b = lambda i:type(i)==int
# print(b(20))
# out =filter(b,l)
# print(list(out))

#* ------------------------------------------------

# l =[16,18.32,"hii",100,3.2,"bye",200,300]
# # print(b(20))
# out =filter(lambda i:type(i)==int,l)
# print(list(out))

#* ------------------------------------------------

# l =[16,18.32,"hii",100,3.2,"bye",200,300]
# # print(b(20))
# print(list(filter(lambda i:type(i)==int,l)))

#~ --------------------------------------------------
#! 2.extract all the string values from tuple only if it is starting with uppercase and ending with lowercase

# a=(10,2.3,'Supritha','home','pythoN','Ugadi')
# print(list(filter(lambda i:type(i)==str and i[0].isupper() and i[-1].islower(),a)))

#~ --------------------------------------------------
#! 3. write a program to extract all the collection values which are of even length from the list.
# l=[10,2.3,'sakshi',[10,20,30],(7,8),{1,2,3,4}]
# print(list(filter(lambda i: type(i)==tuple or type(i)==set or type(i)==str and len(i)%2==0,l)))

#~ --------------------------------------------------
#! 4. write a program to find square of all even numbers from the list.
# l=['hii',1,2,27,14,'hahaha',3+7j]
# data=list(filter(lambda n: type(n)==int and n%2==0 ,l))
# new_data=list(map(lambda n:n**2,data))
# print(new_data)