class Animal:   #Parent class/ Super class/ Base class
    isMammal = True
    gender = "male"
    age = 2

    def movement(self):
        print("Animal is moving with 4 legs")

class Cow(Animal) :#Whatever is in Animal comes to class Cow (inheritance), it is the child class/ Subclass/ Derived class
    def moow(self):
        print("Cow is moowing")

class Cat(Animal):
    def hunt(self):
        print("The cat is hunting rats in the backyard")

        #objects
myCow = Cow()
myCow.moor

myCat = Cat()
myCat.hunt
