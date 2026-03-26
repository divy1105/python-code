

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

# class college:
#     college_name="GLs University"
#     def __init__(self,no_of_courses,president,established_year):
#         self.no_of_courses=no_of_courses
#         self.president=president
#         self.established_year=established_year

#     def display_college(self):
#         print(self.college_name,self.no_of_courses,self.president,self.established_year)

# class Foc(college):
#     def __init__(self,no_of_courses,president,established_year,no_of_subjects,fees):
#         super().__init__(no_of_courses,president,established_year)
#         self.no_of_subjects=no_of_subjects
#         self.fees=fees

#     def display_foc(self):
#         print(self.college_name,self.no_of_courses,self.president,self.established_year,self.no_of_subjects,self.fees)

# class Facit(college):
#     def __init__(self,no_of_courses,president,established_year,no_of_subjects,fees,staff):
#         super().__init__(no_of_courses,president,established_year)
#         self.no_of_subjects=no_of_subjects
#         self.fees=fees
#         self.staff=staff

#     def display_facit(self):
#         print(self.college_name,self.no_of_courses,self.president,self.established_year,self.no_of_subjects,self.fees,self.staff)

# class students(Foc,Facit):
#     def __init__(self, no_of_courses, president, established_year, no_of_subjects, fees,course_name,stu_name):
#         super().__init__(no_of_courses, president, established_year, no_of_subjects, fees)
#         self.course_name=course_name
#         self.stu_name=stu_name

#     def display_student(self):
#         print(self.college_name,self.no_of_courses,self.president,self.established_year,self.no_of_subjects,self.fees,self.course_name,self.stu_name)

# s1=students(7,"DEV",1999,7,10000,"MBA","DEV")
# s1.display_student()

# eg 2.
# class a:
#     property1=38

# class b(a):
#     property2=39

# class c(a):
#     property3=40

# class d(b,c):
#     property4=41

#     def display(self):
#         print(self.property1,self.property2,self.property3,self.property4)

# d1=d()
# d1.display()
# print(d.mro())

# Eg 3.
class college:
    def __init__(self, name, president, established_year):
        self.name = name
        self.president = president
        self.established_year = established_year

    def display_college(self):
        print("--- College Information ---")
        print(f"Name: {self.name}")
        print(f"President: {self.president}")
        print(f"Established: {self.established_year}")

class chemistry(college):
    def __init__(self, name, president, established_year, faculty_name, total_students):
        # Call college directly
        college.__init__(self, name, president, established_year)
        self.chem_faculty = faculty_name
        self.chem_students = total_students

    def display_chemistry(self):
        print(f"Chemistry Faculty: {self.chem_faculty}, Total Students: {self.chem_students}")

class maths(college):
    def __init__(self, name, president, established_year, faculty_name, total_students):
        # Call college directly
        college.__init__(self, name, president, established_year)
        self.math_faculty = faculty_name
        self.math_students = total_students

    def display_maths(self):
        print(f"Maths Faculty: {self.math_faculty}, Total Students: {self.math_students}")

class students(chemistry, maths):
    def __init__(self, name, president, established_year, faculty_name, total_students, enrollmentNo, stu_name):
        # We initialize via chemistry, which handles the college info too
        chemistry.__init__(self, name, president, established_year, faculty_name, total_students)
        # We can also initialize maths if it has different data
        maths.__init__(self, name, president, established_year, faculty_name, total_students)
        
        self.enrollmentNo = enrollmentNo
        self.stu_name = stu_name

    def display_student(self):
        # Calling display methods from all parent levels
        self.display_college()
        self.display_chemistry()
        self.display_maths()
        print("--- Student Details ---")
        print(f"Student Name: {self.stu_name}")
        print(f"Enrollment No: {self.enrollmentNo}")

# Creating the object
s1 = students("GLS University", "DEV", 1999, "Dr. Smith", 500, 240442214115, "DEV_STUDENT")

# Calling the combined display method
s1.display_student()
print(students.mro())