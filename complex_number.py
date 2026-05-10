# it is combination both real(8) and complex number(8j)
num=1+2j 
num.real # it will give real part of the complex number
num.imag
print(f"the real num is {int(num.real)} and the imaginary number is {int(num.imag)}") # this i want to print in the integer number
# union of two complex number
# intersection of two complex number
num1 = 1 + 2j
num2 = 3 + 2j

# Convert real and imaginary parts into sets
set1 = {int(num1.real), int(num1.imag)}
set2 = {int(num2.real), int(num2.imag)}

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))
# is, not is , in , not in
l=[1,2,3,4,5]
# print(4 in l)
# print(4 not in l
num3=1
num4=2
print(num3 is num4)
print(num3 is not num4)
