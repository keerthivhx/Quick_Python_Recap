#to check whether an entered number is even or odd
num=int(input("enter the number:"))
if num%2==0:
    print("it is even")
else:
    print("the entered number is odd")
"""Write a program to check if someone is eligible for a bus pass. If they are below 5 years, 
the bus pass is free. If they are 60 years or older, they get a senior citizen discount. 
Otherwise, they pay the full price."""
print("Welcome to check the eligibity for the bus pass")
age=int(input("enter your age:"))
if age<=5:
    print("your bus pass is free")
elif age>=60:
    print("You will get some discount if u have senior citizen cerfificate")
else:
    print("your are a young star, u should pay full amount")

"""Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
Breakfast: 8 AM
Lunch: 1 PM
Dinner: 8 PM
If none of these times, print "It's not meal time."
Simple Eligibility Check:"""
print("welcome to daily meal time table")
time=input("enter your current time so that i can suggets type of meals with AM/PM:")
if time=="8AM":
    print("Breakfast time")
elif time=="1PM":
    print("Lunch time")
elif time=="8PM":
    print("Dinner time")
else:
    print("it's ur snake time")
"""Write a program that checks whether a person is eligible for a library membership. If they are under 18, they get a student membership. If they are 60 or older, they get a senior citizen membership. Otherwise, they get a regular membership.
"""
print("Welcome to the library membership checker")
age=int(input("Enter your age:"))
if age<18:
    print("You are eligible for a student membership.")
elif age>=60:
    print("You are eligible for a senior citizen membership.")
else:
    print("You are eligible for a regular membership.")