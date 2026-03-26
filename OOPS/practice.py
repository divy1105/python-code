#1.
# input = ['hi','hello','how','are','you']
# func2 = lambda n:n[0]+n[-1]
# print(list(map(func2,input)))


#2.
# class A:
#     def __init__(self,value):
#         self.value = value

#     def __add__(self, other):
#         print(self.value++other.value)

#     def __sub__(self, other):
#         print(self.value--other.value)

# s1=A(20)
# s2=A(10)
# print(s1+s2)
# print(s1-s2)

#3. List
# a=[10,20,30,40,50]
# a.append(60)
# a.append(80)
# a.insert(2,70)
# a.pop(0)
# a.remove(80)
# print(a)

# 4. tuple
# a=(10,20,30,10,10,40,50)
# print(a.count(10),a.index(40))

# 5.set
# a={10,20,30,40}
# print(a.add(60),a.remove(40),a.pop())

# 6. Dictionary
# a={'a':10,'b':20,'c':30}
# print(a.keys(),a.values(),a.items(),a.update({'d':40}),a.pop('a'),a.popitem())
# print(a)

# 7. 
class B:
    def __init__(self,value):
        self.value=value

    def __add__(self,other):
         return self.value+other.value

    def __mul__(self,other):
        return self.value*other.value

s1=B(10)
s2=B(20)
print(s1+s2)
print(s1*s2)
