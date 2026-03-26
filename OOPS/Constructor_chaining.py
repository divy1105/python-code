
#! It is a process of calling the constructor of parent class into the constructor of child class.

#~ Syntax : super().__init__(args)'

# eg.
#class reservation:
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

#! Method chaining : It is a process of calling the method of parent class into the method of child class.

#~ Syntax : super().method(args)