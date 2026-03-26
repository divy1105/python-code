
#!  1.
# a = ['hii','hello','byee']
# out = {'hii':3,'hello':5,'byee':4}
# b={}
# for i in a:
#     b[i]=len(i)
# print(b)

#! 2.
# a =['holiday','mam','sakshi','Naman']
# out = {'holiday':'yadiloh','mam':'mam','sakshi':6,'Naman':'naman'}
# b={}
# for i in a:
#     if len(i)%2==0:
#         b[i]=len(i)

#     else:
#         print(i[::-1])

# print(i)

#! 3. 
a = 'hii i am in ahmedabad '
# out = 'ahmedabad in am i hii'

# s = a.split()
# s.reverse()
# print(' '.join(s))

# s = a.split()
# for i in s[::-1]:
#     print(i,end=' ')
    
# s = a.split()
# out=''
# for i in s:
#     out = i + ' ' + out
# print(out)

#! 4.

a=['Main.py','demo.html','amazon.com','twitter.com','background.css']
# out=[py,html,com,com,css]

# s = a[-1].split('.')
# for i in s:
#     # print(i)
#     print(s[1])

# out=[]
# # s=a.split('.')
# for i  in a: 
#     s=a.split('.')
#     out.append(s[i])
# print(out)

#! 4.

# a = 'Main.py,demo.html,amazon.com,twitter.com,background.css'

#! 5. 
# a = ['Main.py','demo.html','amazon.com','twitter.com','background.css']
# out={'py':['Main'],'html':['demo','demo2'],'com':['amazon','twitter'],'css':['background']}

# a = ['Main.py','demo.html','amazon.com','twitter.com','background.css']
# d = {}
# for i in a:
#     e=i.split('.')
#     key=e[1]
#     value=e[0]
#     if key not in d:
#         d[key]=[value]
#     else:
#         d[key].append(value)

# print(d)

#! 6. 
# b = {'yash':90,'rohit':50,'Akshay':70,'Kusum':80}
# out = {90:'yash',50:'rohit',70:'Akshay',80:'Kusum'}

# b = {'yash':90,'rohit':50,'Akshay':70,'Kusum':80}
# out={}
# for i in b:
#     key=b[i]
#     if key not in out:
#         out[key]=i
# print(out)

#! 7.

# a='aabbacbc'
# out=''
# for i in a:
#     if i not in out:
#         out=out+i+str(a.count(i))
    # else:
    #     pass
#         #out=out
# print(out)



#^ Extraa
# b = {'yash':90,'rohit':50,'Akshay':70,'Kusum':90}
# out = {90: ['yash', 'Kusum'], 50: ['rohit'], 70: ['Akshay']}
# out = {}
# for i in b:
#     key=b[i]
#     if key not in out:
#         out[key]=[i]
#     else:
#         out[key].append(i)
# print(out)

#^ extraa

# a = 'code is easy'
# # b = 'Code Is Easy'
# b = ''
# for i in a:
#     e = a.split(' ')
#     if e[0][0] == 'c':
#         e[0][0].replace('C')
#     elif e[1][0] == 'i':
#         e[1][0].replace('I')
#     elif e[2][0] == 'e':
#         e[2][0].replace('E')
# print()


# a = 'code is easy'
# b = 'Code Is Easy'
# b = ''
# for i in a:
#     if i == 'c':
#         b=b+chr(ord('C'))
#     elif i == 'i':
#         b=b+chr(ord('I'))
#     elif i == 'e' and i != a[3] :
#         b=b+chr(ord('E'))
#     else:
#         b=b+i

# print(b)

#!8.

# a='HIi ThIs Is EAsY'
# b='Hii This Is Easy'

#! 9. write a program to print the table perticular able by user i/p.

# a= int(input("Enter a number:"))
# for i in range(1,11):
#     print(a,"*",i,"=",a*i) 

