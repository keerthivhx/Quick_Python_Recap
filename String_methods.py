g_name=input("Enter a girls name:")
# print("The girls name is "+g_name)
# print(f"the girls age is {g_name}")
# g_age=int(input("Enter the girls age:"))
b_name=input("enter a boy name:")
# # print("the boy name is "+b_name)
# print(f"the boy name is {b_name}")
# b_age=int(input("Enter the  boys age:"))
# print("the diffrence between the ages is "+str(g_age-b_age))
# print(f"the age diffrence btw the girl and boy is {b_age-g_age}")
# print(b_name+" loves "+g_name)
print(" ".join(f"{b_name}loves{g_name}"))
print(f"{b_name}loves{g_name}".split())
print(f"    {b_name} loves {g_name}   ".strip())
#There are diffrent string methodes are there like upper(),lower(),title(),capitalize() etc
"""
text = " Hello World! "
# Case conversion
print(text.upper()) # ' HELLO WORLD! '
print(text.lower()) # ' hello world! '
print(text.title()) # ' Hello World! '
# Trimming whitespace
print(text.strip()) # 'Hello World!'
print(text.lstrip()) # 'Hello World! '
print(text.rstrip()) # ' Hello World!'
# Search and replace
print(text.find("World")) # 8
print(text.replace("World", "Python")) # ' Hello Python! '
# Checks
print("abc123".isalnum()) # True
print("abc".isalpha()) # True
print("123".isdigit()) # True
# Joining and splitting
words = ["Python", "is", "fun"]
print(" ".join(words)) # 'Python is fun'
print("one,two,three".split(",")) # ['one', 'two', 'three']
"""