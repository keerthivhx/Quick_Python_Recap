h1="hellO keerthi"
print(h1)
print(type(h1))
a=20
b=10
print("The operation choice")
print("enter the choice :\n")
choice=input()
operations=["+","-","*"]
print("the operations are",operations)
while (choice in operations):
    if choice=="+":
        print(a+b)
    elif choice=="-":
        print(a-b)
    else:
        print(a*b)
    exit()
print("your choice is not defined in the oeratopns")




