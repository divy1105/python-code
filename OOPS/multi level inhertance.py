
#! Multi level inhertance

# practice questions

# 1.
# class a:
#     property1=10
#     property2=20

# class b(a):
#     property2=30

# class c(b):
#     property1=40

# print(c.property1,c.property2)
# print(c.mro())


# class resume:
#     def __init__(self,name,mobnumber,sscpercentage,sscpassout):
#         self.name=name
#         self.mobnumber=mobnumber
#         self.sscpercentage=sscpercentage
#         self.sscpassout=sscpassout

#     def display(self):
#         print('Name is:',self.name,
#         'Mobnumber is:',self.mobnumber,
#         'SSC Percentage is:',self.sscpercentage,
#         'SSC Passout is:',self.sscpassout)
        
# class resumehsc(resume):
#     def __init__(self,name,mobnumber,sscpercentage,sscpassout,hscpercentage,hscpassout):
#         super().__init__(name,mobnumber,sscpercentage,sscpassout)
#         self.hscpercentage=hscpercentage
#         self.hscpassout=hscpassout

#     def display(self):
#         super().display()
#         print('HSC Percentage is:',self.hscpercentage,'HSC Passout is:',self.hscpassout)

# class finalresume(resumehsc):
#     def __init__(self,name,mobnumber,sscpercentage,sscpassout,hscpercentage,hscpassout,cgpa,college,degree,skills):
#         super().__init__(name,mobnumber,sscpercentage,sscpassout,hscpercentage,hscpassout)
#         self.cgpa=cgpa
#         self.college=college
#         self.degree=degree
#         self.skills=skills

#     def display(self):
#         super().display()
#         print('CGPA is:',self.cgpa,'College is:',self.college,'Degree is:',self.degree,'Skills is:',self.skills)

    
# f1 = finalresume(input("Enter your name: "),input("Enter your mobnumber: "),input("Enter your sscpercentage: "),input("Enter your sscpassout: "),input("Enter your hscpercentage: "),input("Enter your hscpassout: "),input("Enter your cgpa: "),input("Enter your college: "),input("Enter your degree: "),input("Enter your skills: "))
# f1.display()

#! Questions 

# 1. Demonstrate a inheritance in the order grandparent->parent->child . also create appropriate methods in each class.

# class grandparent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display1(self):
#         print('Grandparent Name is:',self.name,'\n',
#         'Grandparent Age is:',self.age)

# class parent(grandparent):
#     def __init__(self,name,age,pname,page):
#         super().__init__(name,age)
#         self.pname=pname
#         self.page=page

#     def display2(self):
#         super().display1()
#         print('Parent Name is:',self.pname,'\n',
#         'Parent Age is:',self.page)

# class child(parent):
#     def __init__(self,name,age,pname,page,cname,cage):
#         super().__init__(name,age,pname,page)
#         self.cname=cname
#         self.cage=cage

#     def display3(self):
#         super().display2()
#         print('Child Name is:',self.cname,'\n',
#         'Child Age is:',self.cage)

# g1=grandparent(input("Enter your name: "),input("Enter your age: "))
# p1=parent(input("Enter your name: "),input("Enter your age: "),input("Enter your parent name: "),input("Enter your parent age: "))
# c1=child(input("Enter your name: "),input("Enter your age: "),input("Enter your parent name: "),input("Enter your parent age: "),input("Enter your child name: "),input("Enter your child age: "))

# g1.display1()
# p1.display2()
# c1.display3()


# 2. Write a Java program to create a class called "GymMembership" with attributes for member name, membership type, and duration. Create a subclass "PremiumMembership" that adds attributes for personal trainer availability and spa access. Implement methods to calculate membership fees and check for special offers based on membership type.

# Class definition: Defines the GymMembership class.
# Attributes: Declares three attributes: memberName (String), membershipType (String), and duration (int, in months).
# Constructor: Initializes the memberName, membershipType, and duration attributes with provided values.
# calculateFees() method:
# Sets a base fee of $50.0 per month.
# Returns the total fee by multiplying the base fee with the duration in months.
# checkSpecialOffers() method:
# Checks if the membership type is "annual".
# Returns a 10% discount message if the membership type is annual.
# Returns a message indicating no special offers for other membership types.
# displayDetails() method:
# Prints the member's name, membership type, and duration.
# Calls calculateFees() to print the total membership fees.
# Calls checkSpecialOffers() to print any applicable special offers.

# ─────────────────────────────────────────────
#  GymMembership – base class
# ─────────────────────────────────────────────
# class GymMembership:

#     def __init__(self, member_name, membership_type, duration):
#         """
#         member_name     : str  – name of the member
#         membership_type : str  – e.g. 'monthly', 'annual'
#         duration        : int  – number of months
#         """
#         self.member_name     = member_name
#         self.membership_type = membership_type
#         self.duration        = duration          # in months

#     # Calculate total membership fee
#     def calculate_fees(self):
#         base_fee = 50.0                          # $50 per month
#         return base_fee * self.duration

#     # Check for special offers
#     def check_special_offers(self):
#         if self.membership_type.lower() == "annual":
#             return "Special Offer: You get a 10% discount on your annual membership!"
#         return "No special offers available for your membership type."

#     # Display member details
#     def display_details(self):
#         print("===== Membership Details =====")
#         print(f"Member Name     : {self.member_name}")
#         print(f"Membership Type : {self.membership_type}")
#         print(f"Duration        : {self.duration} month(s)")
#         print(f"Total Fees      : ${self.calculate_fees():.2f}")
#         print(f"Special Offers  : {self.check_special_offers()}")


# # ─────────────────────────────────────────────
# #  PremiumMembership – subclass of GymMembership
# # ─────────────────────────────────────────────
# class PremiumMembership(GymMembership):

#     def __init__(self, member_name, membership_type, duration,
#                  personal_trainer_available, spa_access):
#         super().__init__(member_name, membership_type, duration)
#         self.personal_trainer_available = personal_trainer_available
#         self.spa_access                 = spa_access

#     # Override – premium adds $30/month surcharge
#     def calculate_fees(self):
#         premium_surcharge = 30.0
#         return super().calculate_fees() + premium_surcharge * self.duration

#     # Override – better deals for premium members
#     def check_special_offers(self):
#         if self.membership_type.lower() == "annual":
#             return "Premium Special Offer: You get a 15% discount + free spa sessions!"
#         return "Premium Perk: Complimentary personal training session this month!"

#     # Override – show extra premium attributes
#     def display_details(self):
#         super().display_details()
#         trainer_status = "Available"     if self.personal_trainer_available else "Not Available"
#         spa_status     = "Included"      if self.spa_access                 else "Not Included"
#         print(f"Personal Trainer: {trainer_status}")
#         print(f"Spa Access      : {spa_status}")


# # ─────────────────────────────────────────────
# #  Main – demonstration
# # ─────────────────────────────────────────────
# if __name__ == "__main__":

#     # Basic membership – monthly
#     basic = GymMembership("Alice", "monthly", 3)
#     basic.display_details()
#     print()

#     # Basic membership – annual (gets 10% discount message)
#     annual = GymMembership("Bob", "annual", 12)
#     annual.display_details()
#     print()

#     # Premium membership – annual (trainer + spa)
#     premium = PremiumMembership("Charlie", "annual", 12,
#                                 personal_trainer_available=True,
#                                 spa_access=True)
#     premium.display_details()
#     print()

#     # Premium membership – monthly, no spa
#     premium_monthly = PremiumMembership("Diana", "monthly", 6,
#                                         personal_trainer_available=True,
#                                         spa_access=False)
#     premium_monthly.display_details()


# ----------or-----

# ================================================================
#  GYM MEMBERSHIP MANAGEMENT SYSTEM
#  Demonstrates: Classes, Inheritance, Method Overriding, OOP
# ================================================================

class GymMembership:
    """
    Base class representing a standard gym membership.

    Attributes:
        member_name     (str) : Full name of the member
        membership_type (str) : Type - 'monthly', 'quarterly', 'annual'
        duration        (int) : Duration in months
    """

    # Class-level constant
    BASE_FEE_PER_MONTH = 50.0   # $50 per month

    def __init__(self, member_name, membership_type, duration):
        self.member_name     = member_name
        self.membership_type = membership_type.lower()
        self.duration        = duration       # in months

    # ----------------------------------------------------------
    #  Calculate total membership fees
    # ----------------------------------------------------------
    def calculate_fees(self):
        """Returns total fee = base fee × duration (in months)."""
        total = self.BASE_FEE_PER_MONTH * self.duration
        return total

    # ----------------------------------------------------------
    #  Check for special offers based on membership type
    # ----------------------------------------------------------
    def check_special_offers(self):
        """
        Rules:
          - annual      → 10% discount
          - quarterly   → 5% discount
          - monthly     → no discount
        """
        if self.membership_type == "annual":
            discount = self.calculate_fees() * 0.10
            return (f"🎉 Annual Member Offer: 10% discount applied!\n"
                    f"   You save: ${discount:.2f}  |  "
                    f"Final Price: ${self.calculate_fees() - discount:.2f}")

        elif self.membership_type == "quarterly":
            discount = self.calculate_fees() * 0.05
            return (f"🎊 Quarterly Member Offer: 5% discount applied!\n"
                    f"   You save: ${discount:.2f}  |  "
                    f"Final Price: ${self.calculate_fees() - discount:.2f}")

        else:
            return "❌ No special offers available for monthly membership."

    # ----------------------------------------------------------
    #  Display all membership details
    # ----------------------------------------------------------
    def display_details(self):
        print("=" * 45)
        print("        GYM MEMBERSHIP DETAILS         ")
        print("=" * 45)
        print(f"  Member Name     : {self.member_name}")
        print(f"  Membership Type : {self.membership_type.capitalize()}")
        print(f"  Duration        : {self.duration} month(s)")
        print(f"  Base Rate       : ${self.BASE_FEE_PER_MONTH:.2f}/month")
        print(f"  Total Fees      : ${self.calculate_fees():.2f}")
        print("-" * 45)
        print("  SPECIAL OFFERS:")
        print(f"  {self.check_special_offers()}")
        print("=" * 45)


# ================================================================
#  PremiumMembership – inherits from GymMembership
# ================================================================

class PremiumMembership(GymMembership):
    """
    Subclass for premium members.
    Adds:
        personal_trainer_available (bool) : Access to personal trainer
        spa_access                 (bool) : Access to spa facilities
    Premium surcharge: +$30/month on top of base fee.
    """

    PREMIUM_SURCHARGE_PER_MONTH = 30.0   # extra $30/month

    def __init__(self, member_name, membership_type, duration,
                 personal_trainer_available, spa_access):
        # Call parent constructor
        super().__init__(member_name, membership_type, duration)
        self.personal_trainer_available = personal_trainer_available
        self.spa_access                 = spa_access

    # ----------------------------------------------------------
    #  Override: Premium fee = base fee + surcharge
    # ----------------------------------------------------------
    def calculate_fees(self):
        """Premium total = (base + surcharge) × duration."""
        base_total    = super().calculate_fees()
        premium_extra = self.PREMIUM_SURCHARGE_PER_MONTH * self.duration
        return base_total + premium_extra

    # ----------------------------------------------------------
    #  Override: Better special offers for premium members
    # ----------------------------------------------------------
    def check_special_offers(self):
        """
        Rules:
          - annual    → 15% discount + free spa sessions
          - quarterly → 10% discount + 1 free PT session
          - monthly   → complimentary PT session
        """
        if self.membership_type == "annual":
            discount = self.calculate_fees() * 0.15
            return (f"🌟 Premium Annual Offer: 15% discount + FREE spa sessions!\n"
                    f"   You save: ${discount:.2f}  |  "
                    f"Final Price: ${self.calculate_fees() - discount:.2f}")

        elif self.membership_type == "quarterly":
            discount = self.calculate_fees() * 0.10
            return (f"⭐ Premium Quarterly Offer: 10% discount + 1 free PT session!\n"
                    f"   You save: ${discount:.2f}  |  "
                    f"Final Price: ${self.calculate_fees() - discount:.2f}")

        else:
            return "🎁 Premium Perk: 1 complimentary personal training session this month!"

    # ----------------------------------------------------------
    #  Override: Display – adds premium-specific info
    # ----------------------------------------------------------
    def display_details(self):
        print("=" * 45)
        print("     PREMIUM GYM MEMBERSHIP DETAILS     ")
        print("=" * 45)
        print(f"  Member Name       : {self.member_name}")
        print(f"  Membership Type   : {self.membership_type.capitalize()} (Premium)")
        print(f"  Duration          : {self.duration} month(s)")
        print(f"  Base Rate         : ${self.BASE_FEE_PER_MONTH:.2f}/month")
        print(f"  Premium Surcharge : ${self.PREMIUM_SURCHARGE_PER_MONTH:.2f}/month")
        print(f"  Total Fees        : ${self.calculate_fees():.2f}")
        print("-" * 45)
        print("  PREMIUM FACILITIES:")
        print(f"  Personal Trainer  : {'✅ Available'    if self.personal_trainer_available else '❌ Not Available'}")
        print(f"  Spa Access        : {'✅ Included'     if self.spa_access                 else '❌ Not Included'}")
        print("-" * 45)
        print("  SPECIAL OFFERS:")
        print(f"  {self.check_special_offers()}")
        print("=" * 45)


# ================================================================
#  MAIN – Test all membership combinations
# ================================================================

if __name__ == "__main__":

    print("\n>>> STANDARD MEMBERSHIPS <<<\n")

    # Monthly – no discount
    m1 = GymMembership("Alice Johnson", "monthly", 3)
    m1.display_details()
    print()

    # Quarterly – 5% discount
    m2 = GymMembership("Bob Smith", "quarterly", 6)
    m2.display_details()
    print()

    # Annual – 10% discount
    m3 = GymMembership("Carol White", "annual", 12)
    m3.display_details()

    print("\n>>> PREMIUM MEMBERSHIPS <<<\n")

    # Premium Monthly – PT available, no spa
    p1 = PremiumMembership("David Lee", "monthly", 3,
                           personal_trainer_available=True,
                           spa_access=False)
    p1.display_details()
    print()

    # Premium Quarterly – PT + Spa
    p2 = PremiumMembership("Eva Green", "quarterly", 6,
                           personal_trainer_available=True,
                           spa_access=True)
    p2.display_details()
    print()

    # Premium Annual – PT + Spa (best deal)
    p3 = PremiumMembership("Frank Brown", "annual", 12,
                           personal_trainer_available=True,
                           spa_access=True)
    p3.display_details()
