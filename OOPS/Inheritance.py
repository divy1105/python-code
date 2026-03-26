
#! Inheritance
#% 11/02/2026
#^ 1. Single Inheritance

#~ class A:
#~    a=10
#~    b=20

#~ class B(A):
#~    c=50

#~ print(B.a,B.b,B.c)

#^ 1.Single Inheritance with Method Overriding
#~ class A:
#~     a=10
#~     b=20
#~ class B(A):
#~     c=50
#~     a=40
#~ print(B.a,B.b,B.c)

#^ 1. Single Inheritance with Method Overriding (Bank Example)

#~ class Bank:
#~     Bname='SBI'
#~     IFSCCODE='SBIN001'
#~     BRANCH='Ahmedabad'

#~     def __init__(self, NAME, MOBNUMBER, ACCNUMBER):
#~         self.NAME=NAME
#~         self.MOBNUMBER=MOBNUMBER
#~         self.ACCNUMBER=ACCNUMBER

#~     def Display(self):
#~         print(self.NAME,self.MOBNUMBER,self.ACCNUMBER)

#~ class Updated_Bank(Bank):
#~     pass

#~ b1=Updated_Bank("Sunny",1234567890,1234567890)
#~ b1.Display()  

#^ 1. Single Inheritance with Constructor Overriding (Bank Example).

#~ class Bank:
#~     Bname='SBI'
#~     IFSCCODE='SBIN001'
#~     BRANCH='Ahmedabad'

#~     def __init__(self, NAME, MOBNUMBER, ACCNUMBER):
#~         self.NAME=NAME
#~         self.MOBNUMBER=MOBNUMBER
#~         self.ACCNUMBER=ACCNUMBER

#~     def Display(self):
#~         print(self.NAME,self.MOBNUMBER,self.ACCNUMBER)

#~ class Updated_Bank(Bank):
#~     BRANCHMANAGER="JOHN"

#~     def __init__(self, NAME, MOBNUMBER, ACCNUMBER, ADHARNUMBER, PANNUMBER):
#~         self.NAME=NAME
#~         self.MOBNUMBER=MOBNUMBER
#~         self.ACCNUMBER=ACCNUMBER
#~         self.ADHARNUMBER=ADHARNUMBER
#~         self.PANNUMBER=PANNUMBER

#~     def DisplayCustomer(self):
#~         print(self.NAME,self.MOBNUMBER,self.ACCNUMBER,self.ADHARNUMBER,self.PANNUMBER)

#~     @classmethod
#~     def DisplayBank(cls):
#~         print(cls.Bname,cls.IFSCCODE,cls.BRANCH,cls.BRANCHMANAGER)

#~ b1=Updated_Bank("DEV",9845689654,56418919846,213541452369,"QUCB46925")
#~ b1.DisplayCustomer()  
#~ b1.DisplayBank()

#^ 1. Single Inheritance with Constructor Overriding Using super() Method(Bank Example).

# class Bank:
#     Bname='SBI'
#     IFSCCODE='SBIN001'
#     BRANCH='Ahmedabad'

#     def __init__(self, NAME, MOBNUMBER, ACCNUMBER):
#          self.NAME=NAME
#          self.MOBNUMBER=MOBNUMBER
#          self.ACCNUMBER=ACCNUMBER

#     def Display(self):
#          print(self.NAME,self.MOBNUMBER,self.ACCNUMBER)

# class Updated_Bank(Bank):
#      BRANCHMANAGER="JOHN"

#      def __init__(self, NAME, MOBNUMBER, ACCNUMBER, ADHARNUMBER, PANNUMBER):
#          super().__init__(NAME, MOBNUMBER, ACCNUMBER)
#          self.ADHARNUMBER=ADHARNUMBER
#          self.PANNUMBER=PANNUMBER

#      def DisplayCustomer(self):
#          print(self.NAME,self.MOBNUMBER,self.ACCNUMBER,self.ADHARNUMBER,self.PANNUMBER)

#      @classmethod
#      def DisplayBank(cls):
#          print(cls.Bname,cls.IFSCCODE,cls.BRANCH,cls.BRANCHMANAGER)

# b1=Updated_Bank("DEV",9845689654,56418919846,213541452369,"QUCB46925")
# b1.DisplayCustomer()  
# b1.DisplayBank()

#^ 1. create a class parent which consist of 3 class members and 3 object memebers which will be acting as a parent class for class son and also inmpliment constrouctor chaning and method chaining in child class.

# class parent:   
#     def __init__(self,name,no_of_children):
#         self.name=name
#         self.no_of_children=no_of_children

#     def display(self):
#         print(self.name,self.no_of_children)
    
# class son(parent):
#     def __init__(self,name,no_of_children,cname,cage):
#         super().__init__(name,no_of_children)
#         self.cname=cname
#         self.cage=cage

#     def display_child(self):
#         print(self.cname,self.cage,self.name,self.no_of_children)
#         # super().display()

# a = son("DEV",2,"JOHN",25)
# a.display_child()

#^ --------------------------------------------------------------------------------

#* 2. Multi-level inheritance

#^ --------------------------------------------------------------------------------

# class A:
#     property1=10
#     def __init__(self,value1):
#         self.value1=value1

# class B(A):
#     property2=20
#     def __init__(self,value2):
#         self.value2=value2

# class C(B):
#     property3=30
#     def __init__(self,value3):
#         super().__init__()
#         self.value3=value3
        

# print(C.property1,C.property2,C.property3)

#^ 2.

# class school:
#     school_name="ABC"
#     def __init__(self,name,no_of_subjects,percentage):
#         self.name=name
#         self.no_of_subjects=no_of_subjects
#         self.percentage=percentage
    
#     def display_school(self):
#         print(self.name,self.no_of_subjects,self.percentage)

# class college(school):
#     college_name="XYZ"
#     def __init__(self,name,no_of_subjects,percentage,course):
#         super().__init__(name,no_of_subjects,percentage)
#         self.course=course

#     def display_college(self):
#         print(self.name,self.no_of_subjects,self.percentage,self.course)

# class Degree(college):
#     degree_name="MBA"
#     def __init__(self,name,no_of_subjects,percentage,course,CGPA):
#         super().__init__(name,no_of_subjects,percentage,course)
#         self.CGPA=CGPA

#     def display_degree(self):
#         print(self.name,self.no_of_subjects,self.percentage,self.course,self.CGPA)

# d1=Degree("DEV",7,80,"MBA",8.5)
# d1.display_degree()

# #^ MRO (Method Resolution Order)
# print(Degree.mro()) 