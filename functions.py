#Function is also called method

       #Categories
    #1. Standard-Library / Built-in Functions -Already exist

z = min(34, 67, 85, 74, 35, 36, 46)
print(z)

y = max(90, 65, 83, 847, 46, 37)
print(y)

    #2. User defined functions - Created and defined by the user, always start with def(define)
def school() :
    print("eMobilis")
school()  #You must call the function for it to display

#Parameters(x, y, z - they are no longer variables but parameters)
def multiply(x, y, z) : #passing parameters ensures they can be assigned different values
    print(x * y * z)
multiply(5, 10, 16)    #5, 10, 16 are arguments
multiply(2, 8 ,10)
