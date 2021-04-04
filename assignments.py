#my way sandwich
print("<---------MyWay Sandwich--------->")
list = ["Onion","lettuce","Tomato","Olives","Peppers","Tomatoes"]
print("Toppings:",list)
print("Select Only 3 Toppings:")
list1=[]
for i in range(3):
    list1.append(input())
print("Your choice:",list1)
a=int(input("How may Sandwiches you want to order:"))
print("Your Bill for",a,"Sandwiches with toppings",list1,"is $",a*5)

#result of student
print("Enter Marks:-")
maths=float(input("Maths:"))
physics=float(input("Physics:"))
chemistry=float(input("Chemistry:"))
if maths>=35 and physics>=35 and chemistry>=35:
    print("You have been passed. Congrats!")
else:
    print("Opps! You are failed. Better luck next time")
average=(maths+physics+chemistry)/3
if average<=59:
    print("You scored 'C'")
elif average<=69:
    print("You scored 'B'")
else:
    print("You scored 'A'")

