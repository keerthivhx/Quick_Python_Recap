#all the function concept of python is called as Precedural function
#here attributes are variable and behavior is a method
#all the oops deals with logics, data and methods 
#class is  instance of object and object is instance of class
#class is a blueprint of
# object and object is a real world entity
class book:
    def __init__(self,w_book,cast):
        print("the detail of book")
        self.w_book=w_book
        self.cast=cast
    def display(self):
        print("the details of book")
book1=book("c",90)
book2=book("c++",80)
book1.display()
book2.display()

#constructor is a special method which is used to initialize the object
#two types are thier parameterized and default
#also fixes the default values
# class Student:#parameterized
#     def __init__(self,name,n_class):
#         self.name=name
#         self.n_class=n_class
# k=Student("kkethi",10)
# print(k.name)
#four pillars of oops
#absraction -hide complex logics and working only shows the essential working
# class student:
#     def going(self):
#         print("she is going")
#     def went(self):
#         print("she went ")
#     def will_go(self):
#         print("she will go")
# s=student() #object
# student.going(s)
#encapsulation is binding the methods and attributes together in a single unit
#inheritence -is udes to inherit the chracter from the parents to child
class water(book):
    def __init__(self,name):
        self.name=name
water1=water("aqua")
water2=book("c",90)
print(water1.name)
print(water2.cast)
#polymorpism

#class are Static instance classes
#static are global level declaration and instance are local level declaration and static are accessed my any where
#destructor is called when destructor is called by __del__