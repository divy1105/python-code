from class1 import login
from class2 import followers
# import program.class1
# import program.class2

class social_media(followers,login):
    def __init__(self,name,Pass,followers,post):
        self.Username=name
        self.Password=Pass
        self.followers=followers
        self.post=post

s1 = social_media("DEV","1234",500,15)
s1.login()
s1.display()
s1.add_follwers()
s1.display()