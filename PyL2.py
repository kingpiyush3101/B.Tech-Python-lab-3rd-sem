#Patterns
'''for i in range(8):
    for j in range(i):
        print(i,end=' ')
    print()

for i in range(7):
    for j in range(i):
        print(j+1,end=' ')
    print()

a=1
for i in range(5):
    for j in range(i):
        print(a,end=' ')
        a+=1
    print()

for i in range(5):
    for j in range(i):
        print("*",end=' ')
    print()

print("\n")'''

#length of string
'''a=input("Enter any string:")
print("The lenght of string {",a,"} is ",len(a)) #strln in c
print("\n")'''

#max and min value
'''a=int(input("Enter No. of elements:"))
list=[]
print("Enter Values:")
for i in range(a):
    list.append(input())
print("The maximum value in ",list,"is ",max(list))
print("The minimum value in ",list,"is ",min(list))'''

#sorting
'''print("\n")
a=int(input("Enter No. of elements:"))
list1=[]
print("Enter Values:")
for i in range(a):
    list1.append(input())
list1.sort(reverse=True)
n=len(list1)
print(list1)
print("max value:",list1[0])
print("min value:",list1[n-1])'''

#factorial of number
'''def fact(a):
   if a==1 or a==0:
       return (a)
   else:
       return (a*fact(a-1))
a=int(input("Enter No. to find factorial:"))
if a<0:
   print("It is a negative no.""\n""Try Again.")
else:
   print("The factorial of",a,"is :",fact(a))
print("\n")
'''
#count no. of characters
'''a=input("Enter any string:")
count=0
for i in a:
    if i!=" ":
        count=count+1
    else:
        continue
print("No. of characters in",a,"is",count)
'''
#fibonacci series
'''print("\n")
n=int(input("Enter Range:"))
a=0
b=1
c=0
print("Fibonacci series:")
print(a)
print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(b)
'''

#linear search
list=[]
a=int(input("Enter the no. of elements:"))
print("Enter Elements:")
for i in range(a):
    list.append(input())
b=input("What to find:")
for i in range(a):d
    if list[i]==b:
        print(b,"is at position",i+1)
if b not in list:
    print(b,"not found")



