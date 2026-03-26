
#^ basic concept Programs
#~ -----------------------------------------------------------
#! 1. variable creation
# class Demo:
#     a=10
#     b=20
# obj=Demo()
# obj2=Demo()
# print(obj.a)
# print(obj2.b)
# print(type(obj2))

#~ ------------------------------------------------------------
#! 2.

# class Company:
#     name="Google"
#     location="USA"
#     ceo="Satya"
#     no_of_employee = "300"

# c1=Company()
# c2=Company()
# c3=Company()

# print(c1.name,c1.location,c1.ceo,c1.no_of_employee)

# #* Moification using Class Name
# Company.name = "Amazon"
# Company.ceo = "Jeff"

# #* Modification using Object Name
# c1.no_of_employee = "100"
# c2.name = "Flipkart"
# c3.location = "New York"

# print(c1.name,c1.location,c1.ceo,c1.no_of_employee)
# print(c2.name,c2.location,c2.ceo,c2.no_of_employee)
# print(c3.name,c3.location,c3.ceo,c3.no_of_employee)

# #* Modification using Object
# c1.name = "Microsoft"
# c1.location = "India"
# c1.ceo = "Satya Narayana"
# c1.no_of_employee = "200"

# print(c1.name,c1.location,c1.ceo,c1.no_of_employee)
# print(c2.name,c2.location,c2.ceo,c2.no_of_employee)
# print(c3.name,c3.location,c3.ceo,c3.no_of_employee)

#~ ------------------------------------------------------------
#! 3. create a class car which consisst of of 3 class members and 4 object members along with 3 objects

# class Car:
#     model_year=2020
#     base_price=100000
#     no_of_wheels=4


# c1=Car()
# c2=Car()
# c3=Car()

# print(c1.model_year,c1.base_price,c1.no_of_wheels)
# print(c2.model_year,c2.base_price,c2.no_of_wheels)
# print(c3.model_year,c3.base_price,c3.no_of_wheels)

# c1.name = "BMW"
# c1.color = "Black"
# c1.price = 300000
# c1.feature = "Manual"

# c2.name = "Mercedes"
# c2.color = "White"
# c2.price = 400000
# c2.feature = "Automatic"

# c3.name = "lemborgini"
# c3.color = "Blue"
# c3.price = 5000000000
# c3.feature = "Manual"

# print(c1.name,c1.color,c1.price,c1.feature)
# print(c2.name,c2.color,c2.price,c2.feature)
# print(c3.name,c3.color,c3.price,c3.feature)

#     def __init__ (self,name,color,price,feature):
#         self.name = name
#         self.color = color
#         self.price = price
#         self.feature = feature

# c1=Car("BMW","Black",3000000,"Automatic")
# print(c1.name,c1.color,c1.price,c1.feature) 

# c2=Car("Mercedes","Blue",40000000,"Manual")
# print(c2.name,c2.color,c2.price,c2.feature)

# c3=Car("Lemborgini","Green",5000000000,"Automatic")
# print(c3.name,c3.color,c3.price,c3.feature)

#~ ---------------------------------------------------------------------------------------------------------
#! 4.create class bank which consist of 3 class members and 4 object members also use constroctor method to create object members.

# class bank:
#     country="India"
#     name="SBI"
#     ceo="abc"
#     def __init__(self,manager_name,branch,state,no_of_employees):
#         self.manager_name=manager_name
#         self.branch=branch
#         self.state=state
#         self.no_of_employees=no_of_employees


# b1=bank("sunny","ahmedabad","Gujarat",100)
# print(b1.manager_name,b1.branch,b1.state,b1.no_of_employees)

# b2=bank("heet","mumbai","Rajsathan",200)
# print(b2.manager_name,b2.branch,b2.state,b2.no_of_employees)

# b3=bank("dev","pune","Maharashtra",300)
# print(b3.manager_name,b3.branch,b3.state,b3.no_of_employees)

#~ ---------------------------------------------------------------------------------------------------------
#! 5. Create a class same as above program but using display method.
#^ object method

# class bank:
#     country="India"
#     name="SBI"
#     ceo="abc"
#     def __init__(self,manager_name,branch,state,no_of_employees):
#         self.manager_name=manager_name
#         self.branch=branch
#         self.state=state
#         self.no_of_employees=no_of_employees

#     def display(self):
#         print(self.manager_name,self.branch,self.state,self.no_of_employees)

# b1=bank("sunny","ahmedabad","Gujarat",100)
# b1.display()

# b2=bank("heet","mumbai","Rajsathan",200)
# b2.display()

# b3=bank("dev","pune","Maharashtra",300)
# b3.display()

#~ ---------------------------------------------------------------------------------------------------------
#! 6. Create a class same as above program but using display method.
#^ (class method)

# class Bank:
#     country = "India"
#     name = "SBI"
#     ceo = "abc"

#     def __init__(self, manager_name, branch, state, no_of_employees):
#         self.manager_name = manager_name
#         self.branch = branch
#         self.state = state
#         self.no_of_employees = no_of_employees

#     @classmethod
#     def display(cls):
#         print(f"Manager Name: {cls.manager_name}, Branch: {cls.branch}, State: {cls.state}, No of Employees: {cls.no_of_employees}")


# Bank.display()

#~ ---------------------------------------------------------------------------------------------------------
#! 7. Static Method


# class Bank:
#     country = "India"
#     name = "SBI"
#     ceo = "abc"

#     def __init__(self, manager_name, branch, state, no_of_employees):
#         self.manager_name = manager_name
#         self.branch = branch
#         self.state = state
#         self.no_of_employees = no_of_employees

#     @classmethod
#     def display(cls):
#         print(cls.country, cls.name, cls.ceo)
#     @staticmethod
#     def details():
#         print("This is a static method")

# Bank.display()
# Bank.details()


#~ ---------------------------------------------------------------------------------------------------------
#! 8. Create a class Hospital which consist of 3 class members and 4 object members , 3 class method and 3 object method along with that create 2 objects

# class Hospital:
#     # Class members
#     country = "USA"
#     name = "Johns Hopkins"
#     ceo = "Dr. Smith"

#     # Object members
#     def __init__(self, location, no_of_beds, no_of_doctors, no_of_patients):
#         self.location = location
#         self.no_of_beds = no_of_beds
#         self.no_of_doctors = no_of_doctors
#         self.no_of_patients = no_of_patients

#     # Class methods
#     @classmethod
#     def display_country(cls):
#         print("Hospital is located in", cls.country)

#     @classmethod
#     def display_name(cls):
#         print("Hospital name is", cls.name)

#     @classmethod
#     def display_ceo(cls):
#         print("Hospital CEO is", cls.ceo)

#     # Object methods
#     def display_location(self):
#         print("Hospital location is", self.location)

#     def display_beds(self):
#         print("Number of beds in the hospital is", self.no_of_beds)

#     def display_doctors(self):
#         print("Number of doctors in the hospital is", self.no_of_doctors)

# # Create 2 objects
# h1 = Hospital("New York", 500, 100, 200)
# # h2 = Hospital("Los Angeles", 600, 120, 250)

# # Call class methods
# Hospital.display_country()
# Hospital.display_name()
# Hospital.display_ceo()

# # Call object methods
# h1.display_location()
# h1.display_beds()
# h1.display_doctors()

# # h2.display_location()
# # h2.display_beds()
# # h2.display_doctors()

# create a class reservation which consist of reservationid ,customer name and date as object members also create subclass resort resevation which add addtion object members like room number and to modify reservation details.

# class reservation:
#     def __init__(self, reservationid, customername, date):
#         self.reservationid = reservationid
#         self.customername = customername
#         self.date = date

#     def display(self):
#         print(self.reservationid,self.customername,self.date)


# class resortreservation(reservation):
#     def __init__(self, reservationid, customername, date, roomnumber):
#         super().__init__(reservationid, customername, date)
#         self.roomnumber = roomnumber

#     def modifyreservation(self, newcustomername, newdate):
#         self.customername = newcustomername
#         self.date = newdate
    
#     def display(self):
#         print(self.reservationid,self.customername,self.date,self.roomnumber)


# r1 = resortreservation(int(input("Enter reservation id: ")), input("Enter customer name: "), input("Enter date: "), input("Enter room number: "))
# r1.display()

# r1.modifyreservation(input("Enter new customer name: "), input("Enter new date: "))
# print("Modified Customer Name:", r1.customername)
# print("Modified Date:", r1.date)

# r1.display()


#! menu driven program

class Reservation:
    def __init__(self, reservationid, customername, date):
        self.reservationid = reservationid
        self.customername = customername
        self.date = date

    def display(self):
        print("\nReservation ID:", self.reservationid)
        print("Customer Name:", self.customername)
        print("Date:", self.date)


class ResortReservation(Reservation):
    def __init__(self, reservationid, customername, date, roomnumber):
        super().__init__(reservationid, customername, date)
        self.roomnumber = roomnumber

    def display(self):
        super().display()
        print("Room Number:", self.roomnumber)

    def modifyreservation(self, newcustomername, newdate):
        self.customername = newcustomername
        self.date = newdate


# Add new reservation
def add_details():
    name = input("Enter the name: ")
    id = int(input("Enter the reservation id: "))
    date = input("Enter the date: ")
    roomno = int(input("Enter the room number: "))

    return ResortReservation(id, name, date, roomno)


# Show all reservations
def show_details(reservations):
    if not reservations:
        print("No reservation details found.")
        return

    print("\n===== ALL RESERVATIONS =====")
    for r in reservations:
        r.display()


# Search reservation by customer name
def search_by_name(reservations):
    if not reservations:
        print("No reservation details found.")
        return

    name = input("Enter customer name to search: ").strip().lower()
    found = [r for r in reservations if r.customername.lower() == name]

    if found:
        print(f"\n===== SEARCH RESULTS FOR '{name.title()}' =====")
        for r in found:
            r.display()
    else:
        print(f"No record found for name '{name.title()}'!")


# Modify by ID
def modify_details(reservations):
    rid = int(input("Enter reservation ID to modify: "))

    for r in reservations:
        if r.reservationid == rid:
            newcustomername = input("Enter new name: ")
            newdate = input("Enter new date: ")
            r.modifyreservation(newcustomername, newdate)
            print("Details updated successfully!")
            return

    print("Reservation ID not found!")


def main():
    reservations = []   # ✅ list to store multiple objects

    while True:
        print("\n====== MENU ======")
        print("1. Add Details")
        print("2. Search by Name")
        print("3. Modify Details")
        print("4. Show All Details")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            r = add_details()
            reservations.append(r)   # ✅ store multiple

        elif choice == 2:
            search_by_name(reservations)

        elif choice == 3:
            modify_details(reservations)

        elif choice == 4:
            show_details(reservations)

        elif choice == 5:
            print("EXITED SUCCESSFULLY!!!")
            break

        else:
            print("ENTER CORRECT OPTION!!!")


if __name__ == "__main__":
    main()