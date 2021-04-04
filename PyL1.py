#Program to add 3 numbers
'''print("Enter No. you want to add :")
a=int(input("1:"))
b=int(input("2:"))
c=int(input("3:"))
print("Sum of ",a,b,c,"is :",a+b+c)'''

#addition with single line input
'''print("enter values:")
a,b,c=int(input()),int(input()),int(input())
x=a+b+c
print(a,"+",b,"+",c,"=",x)'''

#Simple Intrest
'''print("Enter Values:")
a=int(input("Principal Ammount="))
b=int(input("Intrest Rate="))
c=int(input("Time="))
print("Simple Intrest is ",(a*b*c)/100)'''

#area and perimeter of rectangle
'''l=int(input("Enter length of Rectangle:"))
w=int(input("Enter width of Rectangle:"))
print("area of rectangle is:",l*w)
print("perimeter of rectangle is:",2*(l+w))'''

#celsius fahrenheit Conversion
'''print('\n'"°C to °F : 1"'\n'"°F to °C : 0"'\n'"exit : any key")
while 1:
    a=input("Enter:")
    if a=='1':
        c=float(input("Enter Temp. in Celsius:"))
        print(c,"°C is = ",(c * 9/5) + 32,"°F")
    elif a=='0':    
        f=float(input("Enter Temp. in Fahrenheit :"))
        print(f,"°F is = ",(f-32) * 5/9,"°C")
    else:
        break
print("Thank You")'''

#cheaking odd or even
'''a=int(input("Enter Number :"))
if a%2==0:
    print(a,"is a even no.")
else:
    print(a,"is a odd no.")'''

#gratest among three
'''list=[]
print("enter numbers:")
for i in range(0,3):
    list.append(input())
if list[0]>=list[1] and list[0]>=list[2]:
    print(list[0],"is greatest.")
elif list[1]>=list[0] and list[1]>=list[2]:
    print(list[1],"is greatest.")
else:
    print(list[2],"is greatest.")'''

#cheaking entered year is leap or not
'''a=int(input("Enter Year :"))
if a%4==0 or a%400==0 and a%100!=0:
    print(a,"is leap year.")
else :
    print(a,"is not leap year.")'''

#gratest among numbers in array
'''a=[]
b=int(input("Enter no. of elements:"))
print("Enter Elements:")
for i in range(0,b):
    a.append(int(input()))
print("greatest no. is ",max(a))
print("smallest no. is ",min(a))'''

#volume and surface area of sphare
'''pi=3.14
a=float(input("Enter radius of sphere:"))
print("Volume of Sphere with radius ",a,"is",(4/3)*pi*a**3)
print("Surface area of sphere eith radius ",a,"is",(4*pi*a**2))'''


