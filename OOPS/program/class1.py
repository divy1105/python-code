
class login:
    def login(self):
        user_input=input("Enter username:")
        password_input=input("Enter password:")
        
        if self.Username==user_input:
            if self.Password==password_input:
                print("Login successful")
            else:
                print("Incorrect password")
        else:
            print("Incorrect username")