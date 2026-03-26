

#! It is a combination of more than one type of inheritance.

# eg.

#                 A
#                / \
#               B   c
#               \   /
#                 D

# Explaination: A is a parent class of B & C so it is called hirearchical inheritance.
#               B & C is a parent class of D so it is called multiple inheritance.


# Eg. hybrid inheritance

class college:
    college_name="GLs University"
    def __init__(self,no_of_courses,president,established_year):
        self.no_of_courses=no_of_courses
        self.president=president
        self.established_year=established_year

    def display_college(self):
        print(self.college_name,self.no_of_courses,self.president,self.established_year)

class Foc(college):
    def __init__(self,no_of_courses,president,established_year,no_of_subjects,fees):
        super().__init__(no_of_courses,president,established_year)
        self.no_of_subjects=no_of_subjects
        self.fees=fees

    def display_foc(self):
        print(self.college_name,self.no_of_courses,self.president,self.established_year,self.no_of_subjects,self.fees)

class Facit(college):
    def __init__(self,no_of_courses,president,established_year,no_of_subjects,fees,staff):
        super().__init__(no_of_courses,president,established_year)
        self.no_of_subjects=no_of_subjects
        self.fees=fees
        self.staff=staff

    def display_facit(self):
        print(self.college_name,self.no_of_courses,self.president,self.established_year,self.no_of_subjects,self.fees,self.staff)

class students(Foc,Facit):
    def __init__(self, no_of_courses, president, established_year, no_of_subjects, fees,course_name,stu_name):
        super().__init__(no_of_courses, president, established_year, no_of_subjects, fees)
        self.course_name=course_name
        self.stu_name=stu_name

    def display_student(self):
        print(self.college_name,self.no_of_courses,self.president,self.established_year,self.no_of_subjects,self.fees,self.course_name,self.stu_name)

s1=students(7,"DEV",1999,7,10000,"MBA","DEV")
s1.display_student()

