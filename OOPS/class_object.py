
#! 1. create a class car which consist of 3 class members and also create 2 objects each consisting of 2 object members.
 
# class car:
#     company_name='BMW'  #*class member
#     ceo='Satya Nadella' #*class member
#     branch='Ahmedabad'  #*class member

# t1=car() #*object
# t2=car() #*object

# print(t1.company_name,t1.ceo,t1.branch)
# print(t2.company_name,t2.ceo,t2.branch)

# t1.color='Black'       #*object member
# t1.model_year='2020'   #*object member
# print(t1.color,t1.model_year)

# t2.color='Blue'       #*object member
# t2.model_year='2008'  #*object member
# print(t2.color,t2.model_year)

#! 2.

# class car:
#     company_name='BMW'  #*class member
#     ceo='Satya Nadella' #*class member
#     branch='Ahmedabad'  #*class member

#     def __init__(self,color,model_year,model_name):
#         self.color= color            #*object member
#         self.model_year=model_year   #*object member
#         self.model_name = model_name

# t1=car('Black','2020','BMW i8') #*object
# t2=car('gray','2018','BMW M4') #*object


# print(t1.color,t1.model_year,t1.model_name)
# print(t2.color,t2.model_year,t2.model_name)


#! 3.

class car:
    company_name='BMW'  #*class member
    ceo='Satya Nadella' #*class member
    branch='Ahmedabad'  #*class member

    def __init__(self,color,model_year,model_name):
        self.color= color            #*object member
        self.model_year=model_year   #*object member
        self.model_name = model_name
    
    def display(self):
        print(self.color,self.model_year,self.model_name)

    def update(self,new_color):
        self.color=new_color
        

t1=car('Black','2020','BMW i8') #*object
t2=car('gray','2018','BMW M4') #*object

t1.display()         #*object method
t1.update('purple')  #*object method
t1.display()         #*object method


t2.display()
t2.update('red')
t2.display()


print(t1.color,t1.model_year,t1.model_name)
print(t2.color,t2.model_year,t2.model_name)
