#map is used to map the one list with defined function with the list
num=[1,2,3,4,5]
def tree(x):
    print(x*3)
num1=map(tree,num)
print(num1)