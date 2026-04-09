
#* Polymorphism
#! the wod polymorphism is defined from the two greek words ---> poly (many) and morphs (forms).
#! When an object shows the different behavior at the different stages of life cycle then it is called as polymorphism.

#! polymorphism is achived by using method overloading and method overriding.


#* Method Overloading   
# class parent:
#     def add(self):
#         print('I am first method')

#     def add(self, a):
#         print('I am second method')

#     def add(self, a=0, b=0):        #if we use default argument then method overloading is  possible 50%
#         print('I am third method')

# p = parent()
# p.add()


# Real time example of polymorphism

class messenger:
    def use_keyboard(self):
        print('I am using keyboard')

    def send_message(self):
        print('I am using mouse')

    def receive_message(self):
        print('I am receiving message')

class whatsapp(messenger):
    def send_message(self):
        print('sending message using whatsapp')

    def receive_message(self):
        print('receiving message using whatsapp')

class facebook(messenger):
    def send_message(self):
        print('sending message using facebook')

    def receive_message(self):
        print('receiving message using facebook')

class instagram(messenger):
    def send_message(self):
        print('sending message using instagram')

    def receive_message(self):
        print('receiving message using instagram')


w = whatsapp()
f = facebook()
i = instagram()


w.use_keyboard()
w.send_message()
w.receive_message()

f.use_keyboard()
f.send_message()
f.receive_message()

i.use_keyboard()
i.send_message()
i.receive_message()