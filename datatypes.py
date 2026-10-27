age = 34 #integer
height = 6.5 #float
name = "Hannah" #sring
IsPythonInteresting = True #Boolean

print(age)
print(height)


#Data Structures - A single variable stores multiple types

cars = ["Mercedes", "Ford", "Toyota","Audi"] #List -Ordered & Changeable
print(cars)
print(cars[3])

fruits = ("Apple","Banana","Orange","Mango") #Tuple - Ordered & Unchangeable
print(fruits)
print(fruits[1])

countries = {"Kenya","UK","Germany","Italy"} #Set - Unordered but changeable
print(countries)
print("Kenya" in countries) #sets are unordered and cannot be accessed by indexing

student = {"name" : "Hannah", "age" : 18, "Course" : "Computer Science"}#Dictionary - Ordered and changeable
                                                                         #{key: value}
print(student.keys())
print(student.values())
print(len(student))
print(student["name"])
print("mercy" in student.values())   #Boolean - checks whether the value does really exist
print("Hannah" in student.values())     # in checks keys


          #Arrays - stores many values of same type in same variable
from array import array

numbers = array("i", [1,2,3,4])  # i means integer
heights =  array("f", [1.0,2.0,3.0,4.0])  #f means float

print(numbers)
print(numbers[2])
print(heights)
print(heights[1])


         #Typecasting- converting a value from one datatype to another
age = "18" #it is a text
age = int(age) #it is now a number
print(age)  #18
print(age  + 2)  #20
print(int(6.2)) #converting a float, python removes the decimal, so it prints 6