# try--is used to try the first condition and if it is not satisfied then it will go to the except block and execute the code in that block.
# try:
#     a=10
#     b=0
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# except-- is used to find the particular error  and handle it
# finally-- is used to  print(wt ever is thier in the finally block) whether the error is there or not
try:
    a=10
    b=0
    c=a/b
    print(c)
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("This is the end of the program")