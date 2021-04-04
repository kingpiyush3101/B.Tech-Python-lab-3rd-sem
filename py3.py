#exception handling
'''import sys
list=['c',12,0]
for i in list:
    try:
        a=int(input("enter a value:"))
        print('the entered value is:',a)
        div=10/a;
        break
    except:
        print("hey some error is plotted here",sys.exc_info()[0])
        print("please put some other value")
        print()
print('entered vaild value is:',a,'divided output will be',div)'''        


#conditional statement (used when we have no. of choices)
'''i=0
while (i==0):
    a=int(input("enter 1st no.:"))
    b=int(input("enter 2st no.:"))
    if(a>b):
        print(a,"is greater then",b)
    else :
        print(b,"is greater then",a)
    c=int(input("press 1 to exit and 0 to continue:"))    
    if(c==1):
        break
    if(c==0):
        continue
    else:
        print("enter the right command")'''
#for loop
'''l=[1,2,3,4,5]
for i in l :
    print("the value of i is:",i)'''
'''for i in range(1,10):
    print("the value of i is:",i)'''
'''for i in range(1,10,2):
    print("the value of i is:",i)'''
'''for i in range(10,1,-2):
    print("the value of i is:",i)'''
#while loop
'''j=1
while j<10:
    print('Piyush :',j)
    j=j+2'''

#table of any number
'''print("----------------------------MULTIPLICATION TABLE----------------------------")
print("INSTRUCTIONS :-"'\n'"Press 'any key' to 'continue'"'\n'"Press '0' to 'exit'")
while 1:
     a=int(input("Table of :"))
     for i in range(1,11):
        c=a*i
        print(a,"*",i,"=",c)
     j=input("Enter Choice:")
     if (j=="0"):
        break
     else:
        continue
print("Thank You")
print("-------------------------------------------------------------by Piyush Bhatt")'''
#square of any number
'''i=0
while i==0:
    a=int(input("Enter No.:"))
    print(a*a)
    b=input("press 0 to 'exit' and any key to 'continue'")
    if b=="0":
        break
    else:
        continue'''
#Perimeter And Area 
'''print("                        Perimeter & area                          ")
print("INSTRUCTIONS:""\n""1:Rectangle""\n""2:Square""\n""3:||gm""\n""4:Rhombus""\n""5:Circle""\n""0:Exit""\n")
while 1:
    ch=int(input("\n""Enter Choice:"))
    if ch==1:
        l=float(input("Enter Length:"))
        w=float(input("Enter Width:"))
        print("Perimeter:",2*(l+w))
        print("Area:",l*w)
    elif ch==2:
        s=float(input("Enter side:"))
        print("Perimeter:",4*s)
        print("Area:",s*s)
    elif ch==3:
        ch1=input("Enter 'a' for area or 'p' for perimeter:")
        if ch1=="a":
            b=float(input("Enter Base:"))
            h=float(input("Enter Height:"))
            print("Area:",b*h)
        elif ch1=="p":
             a=float(input("Enter Side:"))
             b=float(input("Enter Base:"))
             print("Perimeter:",2*(a+b))
    elif ch==4:
        ch2=input("Enter 'a' for area or 'p' for perimeter:")
        if ch2=="a":
            d1=float(input("Enter Diagonal 1:"))
            d2=float(input("Enter Diagonal 2:"))
            print("Area:",0.5*d1*d2)
        elif ch2=="p" or "P":
             s=float(input("Enter Side:"))
             print("Perimeter:",4*s)
    elif ch==5:
        r=float(input("Enter Radius:"))
        print("Circumference:",2*3.14*r)
        print("Area:",3.14*r*r)
    elif ch==0:
        break
    else:
        print("\n""W@rning : Enter correct choice !")
print("Thank You")
print("                                                   by Piyush Bhatt")'''
        
        


