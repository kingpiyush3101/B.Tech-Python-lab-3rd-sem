# printing patterns
'''
for i in range(4):
     print("*",end=' ')

for i in range(8):
     for j in range(i):
         print("*",end=' ')
     print()  #cascade :prints nothing (space or new line)

for i in range(4):
    for j in range(4):
        print("*",end=' ')
    print()

for i in range(8):
    for j in range(i):
        print(i,end=' ')
    print()

for i in range(1,5):
    for j in range(4):
        print(i,end=' ')
    print()

for i in range(7):
    for j in range(i):
        print(j+1,end=' ')
    print()

list=["A","B","C","D"]
for i in range(5):
    for j in range(i):
        print(list[j],end=' ')
    print()

list=["A","B","C","D"]
for i in range(5):
    for j in range(i):
        print(list[i],end=' ')
    print()

for i in range(5):
    for j in range(i):
        print("x",end=' ')
    print()

for i in range(5):
    for j in range(j):
        print("x",end=' ')
    print()

a=1
for i in range(5):
    for j in range(i):
        print(a,end=' ')
        a+=1
    print()

for i in range(5):
    for j in range(i):
        print(i,end=' ')
        i=i-1
    print()

j=5
for i in range(25):
    for j in range(j):
        print("*",end=' ')
    print()

for i in range(5):
    for j in range(i):
        print("*",end=' ')
    print()
for i in range(i):
    for j in range(j):
        print("*",end=' ')
    print()

for i in range(5):
    for j in range(i):
        print(i,end=' ')
    print()
for i in range(5,8):
    for j in range(j):
        print(i,end=' ')
    print()

b='A'
for i in range(ord(b)+1,ord(b)+5):
    for j in range(ord(b),i):
        print(chr(i-1),end=' ')
    print()

'''
'''
#ASCII values
a='A'
b=chr(65)
print('The character',a,'having the ASCII value:',ord(a))
print('The ASCII value',ord(b),' having character:',b)
print('The next character value after ASCII value ',ord(b),'  is:',chr(ord(b)+1))

for i in range(ord(b)+1,ord(b)+5):
    for j in range(ord(b),i):
        print(chr(j),end=' ')
    print()
'''
# math module
'''import math
a=5
print(math.sqrt(a)) #we have to put module name with .function in order to acess
from math import sqrt
a=4
print(sqrt(a)) #we have imported sqrt function
print(math.sin(math.radians(90))) #return sine value of 30 degree
'''
# square root by user
'''from math import sqrt
print("<------------SQUARE ROOT------------>""\n")
print("Instructions:""\n""1.Press 0 to exit.""\n""2.Press any key to continue.""\n")
while 1:
    a=input("Enter a integer/float no.:")
    try:
        try:
            b=int(a)
            print("The Square root of",b,"is",sqrt(b))
        except:
            c=float(a)
            print("The Square root of",c,"is",sqrt(c))
    except:
        print("W@RN!NG: ",a,"is not a integer/float no. Please Try Again.")
    c=input("\n""choice:")
    if c=='0':
        break
    else:
        continue
print("\n""Thank you!""\n""visit us again.")'''


# Class : It is a blueprint of the individual object
# data(attributes,variables,parameters) / activity(active function those are responsible for perform actions functions/methods)
# Characteristics of class: 1.Atteributes(properties) 2.Activites(action events)
'''class animal:
    pass  # empty class
class simple:
    var = "This is a class."
print(simple.var)  # class to print a string'''
'''
class fun_c1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
a=fun_c1('Aditya',18)
print('The name of student is {} and age is {}'.format(a.name,a.age))
'''
'''class fruits: #fruits is class
    pass
apple=fruits() #apple is object
apple.name='apple'
apple.shape='round'
mango=fruits()
mango.name='mango' #name is instance
mango.shape='oval'
print(apple)
print(apple.name)
print(apple.shape)
print(mango)
print(mango.name)
print(mango.shape) 
'''
#Note this is not possible if there are 100 objects difficult to write and understand.
#alternative method:
'''class fruits:
    def __init__(self,name,shape):
        self.name=name
        self.shape=shape
    pass
apple=fruits('apple','round')
mango=fruits('mango','oval')
print(apple)
print(apple.name,apple.shape)
print('The name of Fruit is {} nd shape is {}'.format(apple.name,apple.shape))
'''
#Example of Employee record
'''class employee:
    def __init__(self,fname,lname,yoj,dept,salary):
        self.fname=fname
        self.lname=lname
        self.yoj=yoj
        self.dept=dept
        self.salary=salary #collection of instance attribute
nitin=employee('nitin','geholet','10-jan-19','Ml','80000')
mayank=employee('mayank','batra','20-mar-20','CSE','56000')
print(nitin.__dict__) #To find instance attributes if large in no.
nitin.extra = 'Team Leader' #To add extra attribute
print(nitin.__dict__)
print(mayank.__dict__)'''


#Students Introduction/Details
'''class students:
    def __init__(self,name,fname,dob,branch,id,r):
        self.name=name
        self.fname=fname
        self.dob=dob
        self.branch=branch
        self.id=id
        self.r=r
a=int(input("Enter No. of Students:"))
list_n=[]
print("Enter name of Students:")
for i in range(a):
        list_n.append(input())
print(list_n)
list_n[0]=students(int(i) for i in input("Enter Details of {}:".format(list_n[0])).split())
'''
'''
@classmethod
def ashita(cls, clrs):
    pass
@staticmethod
def aakshy():
    pass
'''

#Dunder method: It is magic method. They have their own defination to .we can inherit their properties.
'''a = 89
print(a.__add__(2))'''


