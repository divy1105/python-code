
# inheriting property from single parent class to multiple child class is called as hierarchical inheritance.

    #   ___________pc______________                   (PC=Parent Class)
    #   |           |               |  
    #   |           |               |
    #  CC1         CC2            CC3                  (CC=Child Class)






#! create a class parent which is acting as a parent class for  class son and class daughter also perform constructor chaning and method chaining from the parent class.

# class parent:   
#     def __init__(self,name,no_of_children):
#         self.name=name
#         self.no_of_children=no_of_children

#     def display_parent(self):
#         print(self.name,self.no_of_children)

# class son(parent):
#     def __init__(self,sname,sage):
#         # super().__init__(name,no_of_children)
        
#         self.sname=sname
#         self.sage=sage

#     def display_son(self):
#         print(self.sname,self.sage,self.name,self.no_of_children)
#         # super().display_parent()

# class daughter(parent):
#     def __init__(self,dname,dage):
#         # super().__init__(name,no_of_children)
#         self.dname=dname
#         self.dage=dage

#     def display_daughter(self):
#         print(self.dname,self.dage,self.name,self.no_of_children)
#         # super().display_parent()

# s1 = son("DEV",2)
# s1.display_son()

# d1 = daughter("Devika",2)
# d1.display_daughter()

#! ------------------------------------------------------------------------------------

#^ 2. create a class social media which cosist of 4 object members & perform hierarchical inheritance in other 2 classes facebook & instagram.

# class social_media:
#     def __init__(self,name,Pass,followers,following):
#         self.Username=name
#         self.Password=Pass
#         self.no_of_followers=followers
#         self.no_of_following=following

#     def display_social(self):
#         print(self.Username,self.no_of_followers,self.no_of_following)

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
        

#     def increase_followers(self):
#         self.no_of_followers=self.no_of_followers+1 

#     def change_password(self):
#         old_paassword=input("Enter old password:")
#         if old_paassword==self.Password:
#             new_password=input("Enter new password:")
#             self.Password=new_password
#             print("Password changed sucessfully")
#         else:
#             print("Old password is incorrect")


# class instagram(social_media):
#     def __init__(self,name,Pass,followers,following,close_frds,posts):
#         super().__init__(name,Pass,followers,following)
#         self.no_of_close_frds = close_frds
#         self.posts=posts
    
#     def display_instagram(self):
#         print(self.Username,self.no_of_followers,self.no_of_following,self.no_of_close_frds,self.posts)

# class facebook(social_media):
#     def __init__(self,name,Pass,followers,following,likes,dislikes):
#         super().__init__(name,Pass,followers,following)
#         self.likes=likes
#         self.dislikes=dislikes

#     def display_facebook(self):
#         print(self.Username,self.no_of_followers,self.no_of_following,self.likes,self.dislikes)


# f1 = facebook("DEV","123",100,200,25,13)
# f1.login()
# f1.display_facebook()
# f1.increase_followers()
# f1.display_facebook()
# f1.change_password()

# i1 = instagram("spider","web@110",300,219,50,10)
# i1.login()
# i1.display_instagram()
# i1.increase_followers()
# i1.display_instagram()
# i1.change_password()

# Eg 2. wap program to create the hierarchy for employees of company in the following manner.
# employee is parent class.
# manager,developer and tester are child class.
# child class contins properties name,salary,experience and mobile number.
# create some additional attributes also for each subclasses and methods for calculating salary



# ─── Parent Class ───
class Employee:
    def __init__(self, name, salary, experience, mobile):
        self.name       = name
        self.salary     = salary        # base salary
        self.experience = experience    # in years
        self.mobile     = mobile

    def display(self):
        print(f"  Name          : {self.name}")
        print(f"  Base Salary   : ${self.salary:,.2f}")
        print(f"  Experience    : {self.experience} year(s)")
        print(f"  Mobile        : {self.mobile}")

    def calculate_salary(self):
        return self.salary


# ─── Child Class 1: Manager ───
class Manager(Employee):
    def __init__(self, name, salary, experience, mobile, team_size, department):
        super().__init__(name, salary, experience, mobile)
        self.team_size  = team_size       # extra attribute
        self.department = department      # extra attribute

    def calculate_salary(self):
        bonus = 500 * self.team_size      # $500 bonus per team member
        hike  = self.salary * 0.20        # 20% experience hike
        return self.salary + bonus + hike

    def display(self):
        print("\n" + "=" * 42)
        print("         👔  MANAGER DETAILS           ")
        print("=" * 42)
        super().display()
        print(f"  Department    : {self.department}")
        print(f"  Team Size     : {self.team_size} members")
        print(f"  Team Bonus    : ${500 * self.team_size:,.2f}  ($500 × {self.team_size})")
        print(f"  Experience Hike: ${self.salary * 0.20:,.2f}  (20%)")
        print(f"  Total Salary  : ${self.calculate_salary():,.2f}")
        print("=" * 42)


# ─── Child Class 2: Developer ───
class Developer(Employee):
    def __init__(self, name, salary, experience, mobile, tech_stack, projects_done):
        super().__init__(name, salary, experience, mobile)
        self.tech_stack    = tech_stack      # extra attribute
        self.projects_done = projects_done   # extra attribute

    def calculate_salary(self):
        project_bonus = 200 * self.projects_done   # $200 per project
        exp_hike      = self.experience * 1000      # $1000 per year of experience
        return self.salary + project_bonus + exp_hike

    def display(self):
        print("\n" + "=" * 42)
        print("         💻  DEVELOPER DETAILS         ")
        print("=" * 42)
        super().display()
        print(f"  Tech Stack    : {self.tech_stack}")
        print(f"  Projects Done : {self.projects_done}")
        print(f"  Project Bonus : ${200 * self.projects_done:,.2f}  ($200 × {self.projects_done})")
        print(f"  Exp Hike      : ${self.experience * 1000:,.2f}  ($1000 × {self.experience} yrs)")
        print(f"  Total Salary  : ${self.calculate_salary():,.2f}")
        print("=" * 42)


# ─── Child Class 3: Tester ───
class Tester(Employee):
    def __init__(self, name, salary, experience, mobile, bugs_found, testing_type):
        super().__init__(name, salary, experience, mobile)
        self.bugs_found   = bugs_found      # extra attribute
        self.testing_type = testing_type    # extra attribute (Manual/Automation)

    def calculate_salary(self):
        bug_bonus = 50 * self.bugs_found    # $50 per bug found
        if self.testing_type.lower() == "automation":
            auto_bonus = 3000               # automation tester gets extra
        else:
            auto_bonus = 0
        return self.salary + bug_bonus + auto_bonus

    def display(self):
        print("\n" + "=" * 42)
        print("         🧪  TESTER DETAILS            ")
        print("=" * 42)
        super().display()
        print(f"  Testing Type  : {self.testing_type}")
        print(f"  Bugs Found    : {self.bugs_found}")
        print(f"  Bug Bonus     : ${50 * self.bugs_found:,.2f}  ($50 × {self.bugs_found})")
        if self.testing_type.lower() == "automation":
            print(f"  Auto Bonus    : $3,000.00")
        print(f"  Total Salary  : ${self.calculate_salary():,.2f}")
        print("=" * 42)


# ================================================================
#  MAIN
# ================================================================
if __name__ == "__main__":

    m1 = Manager("Rajesh Kumar", 8000, 10, "9876543210",
                 team_size=8, department="Engineering")
    m1.display()

    d1 = Developer("Priya Sharma", 6000, 5, "9123456780",
                   tech_stack="Python, Django, React",
                   projects_done=12)
    d1.display()

    t1 = Tester("Arjun Mehta", 5000, 3, "9001234567",
                bugs_found=45, testing_type="Automation")
    t1.display()

    t2 = Tester("Sneha Patel", 4500, 2, "9876501234",
                bugs_found=30, testing_type="Manual")
    t2.display()
