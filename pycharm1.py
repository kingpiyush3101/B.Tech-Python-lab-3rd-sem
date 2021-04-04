# operators
'''a=10.88
print(a*a)
print(a/3)
print(a//3) #provides floor value of dividing element
print(a%3)'''

# number data types
'''inta=125
floata=12.5
complexa=12.5j
longa=123456789
print(inta)
print(floata)
print(complexa)
print(longa)
print(complexa.imag,complexa.real)'''

# string: It is a continous set of characters.
'''print('Piyush Bhatt')
a="Piyush Bhatt"
print(a)
b=len(a)
print('The Entered String is:',a,"having",b,'no. of charaters')
print(a[0:10]) #for printing characters'''

# set: Unorderd collection of unique elements/objects.
# 1. Mutability: Declared variable have the capability to append the element.
# 2. Immutability: Declared variable haven't that much capability to append elements as per the requirements.
'''c={'toys',"vegetables",'fruits','shots','drinks'}
print(c)   #when same code run multiple times then output order changes eachtime i.e unordard list
print(len(c))
b="Piyush Bhatt"
d=set(b)   #to change string to set
print(d)   #each character is seprate out and considered as single element
d.add('23') #we cannot add in string it does not have add attribute so first change it to set and there can be mutability in string
print(d)
a={"A","B","C","D"}
b={"B","D"}
c=set(a)
d=set(b)
print(c-d) #gives element are not in b /d'''

# frozenset: If we want to immutability inside the set.
'''c={'toys',"vegetables",'fruits','shots','drinks'}
fs1=frozenset(c)
print(fs1)
fs2=fs1.add('snacks') #we can't add anything in frozen set
print(fs2)'''

# list: A set of elements that are orderd and not unique elements (we can provide frequencies of data in list) behaves like a array in c/c++ programming environment.It does not have homogeneous property.
'''list_1=['Piyush',15,15.5,'B.Tech','CSE-MLAI',15]
list_2=["Bhatt",123,123.123]
print(list_1) #no unique property
print(len(list_1))
print(list_1[0]) #To print the single element
print(list_1[0:3]) #TOo print element upto range
print(list_1*3) #To print contents n no. of times
print(list_2+list_1)
print(list_1+list_2) #concatenation: Addition(A+B||B+A) but in Append it is only A+B.
print(list_1[-1]) #Acces elements from right to left
for i in list_1:
    print(i)    #for printing elements one by  one '''

# built in functionof list in python 3.8
'''list_1=[1,2,3,4,5,6]
print(list_1)
print("The length of list 1 is ",len(list_1))
print("The minimum value in list 1 is ",min(list_1))
print("The maximum value in list 1 is ",max(list_1))
print("The sum of elements in list 1 is ",sum(list_1))
print("Average of elements in list 1 is ",(sum(list_1)/len(list_1)))'''

# average of elements of list using logic or without function
'''list1=[]
sum=0
b=int(input("Enter no. of elements:"))
print("Enter Elements:")
for i in range(0,b):
    list1.append(int(input("")))
print(list1)
for i in range(0,len(list1)):
    sum=sum+int(list[i])
print("Average of elements in list is ",(sum/b))'''

# To format specific point
'''str_1="MLAI has total strength of :{stren:} students"
str_2="And {stren:} students are taking class."
print(str_1.format(stren=45))
print(str_2.format(stren=20))
txt="For only {price:.2f} dollor!"
print(txt.format(price=45.6778))'''

# dictionary: key and their coressponding values.Mutable:we can change.Elements are in the form of pairs.(enum alternative in c)
'''dict_1={'R.no_1':'Piyush','R.no_2':'Ayush','R.no_3':'Ashita','R.no_4':'Anshul'}
dict_2={'Roll_no.':28,'Name':'Virat'} #hetrogenous(mixed)
print(dict_1)
print(dict_2)
print(len(dict_1))
print(dict_1.keys())
print(dict_1.values())
dict_1=dict({'1':'Akshy','2':'Ayush','3':'Aniket','4':'Anoop'})
print(dict_1) #decleration
print(dict_1['2']) #accesing the values using []
print(dict_1.get('1')) #accesing the values using get() method
dict_2=dict([('1','Akshy'),('2','Ayush'),('3','Aniket'),('4','Anoop')])
print(dict_2) #list to dictionary
dict_2[5]='Aditya'
print(dict_2) #append the dictionay
dict_2[5]='Aman'
print(dict_2) #we can edit values not keys
del dict_2[5]
print(dict_2) #delete elements in dictionary
'''
#     @H.W.   (Table of contents)    nested dictionary
'''dict_nested=dict({'1':'Akshy','2':'Ayush',
                  '3':{'4':'Aniket','5':'Anoop'}})
print(dict_nested) #nested dictionary'''

#user inputed dictionary
'''dict={}
list=[]
a=int(input("Enter the no. of elements:"))
for i in range(a):
    print("Enter the key:")
    list.append(input())
    print("Enter the value:")
    dict[list[i]] = input()
print("The Dictionary you created is:""\n",dict)
'''

# tuple: It is immutable type of data type initilize by ()
'''tuple_1=(123,"piyush","bhatt")
tuple_2=("ayush",321)
print(tuple_1)
print(tuple_1[0])
print(tuple_1[0:2]) #slicing
print(tuple_2 * 3)
print(len(tuple_1))
print(tuple_1 + tuple_2)
tuple=(3,)
print(type(tuple))
tuple_1[0]='Wow'  #not supported '''

# wap to print values from specific range provided by user:
# 1.seprate values via even and odd.
# 2.even and odd positions.
'''a=int(input("Starting limit:"))
b=int(input("End limit:"))
set1=set()
set2=set()
set3=set()
set4=set()
for i in range(a,b):
    if (i)%2==0 :
        set1.add(i)
        set3.add(i+1)
    else:
        set2.add(i)
        set4.add(i+1)
print("Even numbers between ",a,"to",b-1,"are:",set1)
print("Odd numbers between ",a,"to",b-1,"are:",set2)
print("Positions of even numbers are:",set3)
print("Positions of odd numbers are:",set4)'''

# search provided by user in list
'''list1=[]
b=int(input("Enter no. of elements:"))
print("Enter Elements:")
for i in range(0,b):
    list1.append(input(""))
print(list1)
c=input("Enter element to search:")
for i in range(0,b):
    if list1[i]==c:
        print(c,"found at position",i+1)
        break
    if i==b-1:
        print(c,"is not found")'''

# input in list using comprehension technique (omptimization) and typecasting technique.
'''list1=[]
list1=[int(i) for i in input("Enter Element:").split()]
print(list1)'''

# Python version
'''import sklearn
print('sklearn: {}'.format(sklearn.__version__))'''

#Date and Time is a libaray in python to access date and time of system and connected network
'''import datetime
a = datetime.datetime.now() #print both date and time
print("The current Date And Time is :",a)
print("year:",a.year)
print("month:",a.month)
print("day",a.day)
print("hour:",a.hour)
print("minute:",a.minute)
print("second:",a.second)
b=a.microsecond//10000 #for printing upto 2 digits
print("micro second:",b)
c = datetime.date.today() #print today's date
print("Today's Date is :",c)
d = datetime.date(2012,8,9) #To initialize the specific date
print("Specific date is :",d)
print(d.timetuple())
diff = c - d #difference between two specific dates
print(diff)'''