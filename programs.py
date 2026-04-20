#create a class mobile  and attributes brand and price 
#create a two  objects of class and display attributes of using methodes
# class mobile():
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#     def display(self):
#         print(f"the barnd {self.brand}")
#         print(f"the price {self.price}")
# mobile1=mobile("Apple",999)
# mobile2=mobile("Samsung",899)
# mobile1.display()
# mobile2.display()
#create a class student woth attribute of name and marks and display them and call the multiple objectives call each methode
class student():
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"the name {self.name}")
        print(f"the marks {self.marks}")
student1=student("kkethi",90)
student2=student("kkethi",80)
student1.display()
student2.display()