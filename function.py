# def any_fun(name):#arguments
#     print(f"Hello,{name}")
# any_fun("keerthi")#positional argument
# any_fun("keerthi1")
# any_fun(name="keerthi2")#keyword argument
# any_fun(name="keerthi3")#keyword argument
# let me write the multiple of 3
def multiple(i,h="ii"):
    for j in range(1,11,1):
        print(f"{i}*{j}={i*j}")
        print(h)
multiple(3)
# multiple(5)
# multiple(7)
multiple(3)
#retrun function
def add(a,b):
    return a+b
result=add(10,20)
print(result)
# Greet Function: Write a function greet() that takes no arguments and prints a greeting message.
def greet():
    print("Hello keerthi!! how r u??")
greet()
# Parameterized Greet: Write a function greet_user() that takes a name as input and prints a custom greeting.
def greet1(name):
    print(f"hello {name}")
greet1("keerthi")