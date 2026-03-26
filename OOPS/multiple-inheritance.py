
#^ Multiple Inheritance
#$ 13/02/2023

# class login:
#     def login(self):
#         user_input=input("Enter username:")
#         password_input=input("Enter password:")
        
#         if self.Username==user_input:
#             if self.Password==password_input:
#                 print("Login successful")
#             else:
#                 print("Incorrect password")
#         else:
#             print("Incorrect username")
            

# class followers:
#     def add_follwers(self):
#         self.followers+=1
#     def remove_followers(self):
#         self.followers-=1

#     def display(self):
#         print(self.Username,self.Password,self.followers,self.post)

# class social_media(followers,login):
#     def __init__(self,name,Pass,followers,post):
#         self.Username=name
#         self.Password=Pass
#         self.followers=followers
#         self.post=post

# s1 = social_media("DEV","1234",500,15)
# s1.login()
# s1.display()
# s1.add_follwers()
# s1.display()

# Eg 2.
# class a:
#     property1=10
#     property2=20

# class b:
#     property2= 50


# class c(a,b):
#     property4=90

# print(c.property1,c.property2,c.property4)
# print(c.mro())

# Eg 3.
#* create a class calculator which inherits from multiple parent classes like sub,add,mul and div.

# class add:
#     @staticmethod
#     def add(*args):
#         total=0
#         for i in args:
#             total+=i
#         return total

# class sub:
#     @staticmethod
#     def sub(*args):
#         total=0
#         for i in args:
#             total-=i
#         total=abs(total)
#         return total

# class mul:
#     @staticmethod
#     def mul(*args):
#         total=1
#         for i in args:
#             total*=i
#         return total

# class div:
#     @staticmethod
#     def div(*args):
#         total=1
#         for i in args:
#             total/=i
#         return total

# class calculator(add,sub,mul,div):
#     pass

# c1 = calculator()
# print(c1.add(10,20))
# print(c1.sub(10,20))
# print(c1.mul(10,20))
# print(c1.div(10,20))


