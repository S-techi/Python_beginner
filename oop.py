#Object orientend programming - writing programs using classes and objects
#Class - blueprint
#object - instance of a class

#creating a class
class Employee:
    #a class has a attributes which are written as variables
    #self means every value assigned to a variable be given to a specific object
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    #  class has behaviours which are written as functions
    def movement(self):
        print("Employee is walking")

# creating an object
employee1 = Employee("Alice",34,"Female")  #whatever is in Employee, give to employee 1
employee2 = Employee("Ken", 40, "Male")
employee3 = Employee("Wayne", 28, "Male")

print(employee1.name, employee1.age ,employee1.gender)
print(employee2.name, employee2.age, employee2.gender)
print(employee3.name, employee3.age, employee2.gender)

employee1.movement()
employee2.movement()
employee3.movement()

