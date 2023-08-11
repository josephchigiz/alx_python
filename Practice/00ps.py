#! OOPs Practice
'''
Classes and objects are the two main aspects of object oriented programming. 
A class creates a new type where objects are instances of the class.
'''
#* Note that even integers are treated as objects (of the int class)
#* Variables that belong to a class or object are called fields
# Fields are of two types - they can belong to each instance/object of the class or they can 
# belong to the class itself. They are called instance variables and class variables respectively.


#! Self
#The code:

# class MyClass:
#   myobject = ()
#   myobject.method(arg1, arg2)  #will be converted by python to:👇🏾
  
#   #* MyClass.method(myobject, arg1, arg2)
  

# #! Classes
# #An example of a simple class:

# class Person:
#   pass # An empty block

# p = Person()
# print(p)

'''
We create a new class using the class statement and the name of the class.
Then, we created an object/instance of this class using the name of the class 
followed by a pair of parentheses. For our verification, we confirm the type of the variable
by simply printing it. It tells us that we have an instance of the Person class in the __main__ module
'''

#! Methods
# class Person:
#   def say_hi(self):
#     print('How are you?')
    
# p = Person()
# p.say_hi() 
# #The two lines above can also be written as 
# #* Person().say_hi()

#! The __init__ method
# This method is run as soon as an object of a class is created
# The method is useful to do any initialization you want to do 
# with your object:

# class Person:
  
#   def __init__(self, name):
#     self.name = name
    
#   def say_hi(self):
#     print('Hello, how are you', self.name)

# p = Person('Ochego')
# p.say_hi()


#! Class and Object Variables
# The data part, i.e. fields, are nothing but ordinary 
# variables that are bound to the namespaces of the classes and objects.

# There are two types of fields - class variables and object 
# variables which are classified depending on whether the class or the 
# object owns the variables respectively.

#* `Class variables` are shared - they can be accessed by all instances of that class.

#* `Object variables` are owned by each individual object/instance of the class. In this 
#* case, each object has its own copy of the field

#!Combo Example

# class Robot:
#   """Represents a robot with a name"""
  
#   # A class variable counting the number of robots
#   population = 0
  
#   def __init__(self, name):
#     """Initialize the data"""
#     self.name = name
#     print("(Initializing {})".format(self.name))
    
#     # When this person is created the robot
#     # is added o the population
#     Robot.population += 1
    
  
#   def die(self):
#     """I am dying"""
#     print("{} is being destroyed!".format(self.name))
    
#     Robot.population -= 1
    
#     if Robot.population == 0:
#       print("{} was the last one.".format(self.name))
#     else:
#       print("There are still {:d} robots.".format(Robot.population))
      
  
#   def say_hi(self):
#     """Greetings by the robot.
#     yes, they can do that"""
#     print("Greetings, my masters call me {}.".format(self.name))
    
    
#   @classmethod
#   def how_many(cls):
#     """Print current population"""
#     print("Currently, we have {:d} robots.".format(cls.population))
    
    
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()

# droid2 = Robot("C-3PO")
# droid2.say_hi()
# Robot.how_many()

# print("\nRobots can do some work here.\n")

# print("Robots have finished their work. So let's destroy them")
# droid1.die()
# droid2.die()

# Robot.how_many()

#! Dog Example

# class Dog:
  
#   def __init__(self, name, height, weight):
#     self.name = name
#     self.height = height
#     self.weight = weight
    
#   def run(self):
#     print("{} the dog runs so fast.".format(self.name))

#   def eat(self):
#     print("{} the dog eats too much and is now {}kgs.".format(self.name, self.weight))

#   def bark(self):
#     print("{} the dog has a very fierce bark.".format(self.name))
    
# def main():
#   spot = Dog("Spot", 66, 26)
#   spot.bark()
#   spot.eat()
  
# main()


#!! GETTERS and SETTERS
# class Square:
  
  
#   def __init__(self, height="", width=""):
#     self.height = height
#     self.width = width
    
#   @property # allows us to refer to these individual fields
#   def height(self):
#     print("Receiving the height")
    
#     return self.__height
  
#   @height.setter
#   def height(self, value):
    
#     if value.isdigit():
#       self.__height = value
#     else:
#       print("Please only enter numbers for height")

#   @property # allows us to refer to these individual fields
#   def width(self):
#     print("Receiving the width")
    
#     return self.__width
  
#   @width.setter
#   def width(self, value):
    
#     if value.isdigit():
#       self.__width = value
#     else:
#       print("Please only enter numbers for width")
      
#   def getArea(self):
#     return int(self.__height) * int(self.__width)
  
  
# def main():
#   aSquare = Square()
  
#   height = input("Enter height : ")
#   width = input("Enter width : ")
  
#   aSquare.height = height
#   aSquare.width = width
  
#   print("Height : ", aSquare.height)
#   print("Width : ", aSquare.width)
  
#   print("The are of the square is : ", aSquare.getArea())
  
  
# main()

#!! Sam and Paul
'''
Sam attacks paul and deals 9 damage
Paul is down to 10 health
Paul attacks sam and deals 7 damage
Sam is down to 7 health
Sam attacks paul and deals 19 damage
Paul is down to -9 health
Paul is dead and sam is victorious
Game Over
'''

# import random
# import math

# # Warrior and Battle Class
# class Warrior:
  
#   def __init__(self, name="Warrior", health=0, attkMax=0, blckAmt=0):
#     self.name = name
#     self.health = health
#     self.attkMax= attkMax
#     self.blckAmt = blckAmt
    
#   def attack(self):
#     attkMax = self.attkMax * (random.random() + .5)
    
#     return attkMax
  
#   def block(self):
#     blckAmt = self.blckAmt * (random.random() + .5)
    
#     return blckAmt
    
# # Warriors have name, health, attack and block maximums
# # They will have the capabilities to block and attack random amounts

# # Attack random() 0.0 to 1.0 * maxAttack +.5

# # Block will also use random()

# # Battle class capability of looping until 1 warrior dies

# class Battle:
  
#   def startFight(self, warrior1, warrior2):
    
#     while True:
#       if self.getAttackResult(warrior1, warrior2) == "Game Over":
#         print("Game Over")
#         break
      
#       if self.getAttackResult(warrior2, warrior1) == "Game Over":
#         print("Game Over")
#         break
      
      
#   @staticmethod
#   def getAttackResult(warriorA, warriorB):
    
#     warriorAAttkAmt = warriorA.attack()
#     warriorBBlockAmt = warriorB.block()
    
#     damage2WarrioB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
#     warriorB.health = warriorB.health - damage2WarrioB
    
#     print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage2WarrioB))
#     print("{} is down to {} health".format(warriorB.name, warriorB.health))
    
#     if warriorB.health <= 0:
#       print("{} has died and {} is vicorious".format(warriorB.name, warriorA.name))
#       return "Game Over"
#     else:
#       return "Fight Over"

# def main():
  
#   ochego = Warrior("Ochego", 50, 20, 10)
#   ogweno = Warrior("Ogweno", 50, 20, 10)
  
#   battle = Battle()
#   battle.startFight(ochego, ogweno)
  
# main()
#     #warriorBAttkAmt = warriorB.attack()
      
# # Warriors will each get a turn to attack each other


# # Function gets 2 warriors
# # 1 warrior attacks the other 

#!! Socratica: Dive into Classes and Objects
# import datetime

# class User:
#   """We are storing simple user data for now,
#    but we'll progress to more intrusive data later"""
#   def __init__(self, full_name, birthday):
    
#     self.full_name = full_name
#     self.birthday = birthday  #yyyymmdd
    
#     #Extract first and last names
#     sep_names = full_name.split(" ")
#     self.first_name = sep_names[0]
#     self.second_name = sep_names[-1]
    
    
#   def age(self):
#     """Returns the age of the user in years"""
#     today = datetime.date(2023, 8, 11)
#     yyyy = int(self.birthday[0:4])
#     mm = int(self.birthday[4:6])
#     dd = int(self.birthday[6:8])
#     dob = datetime.date(yyyy, mm, dd) #date of birth
    
#     age_in_days = (today - dob).days
#     age_in_years = (age_in_days/365)
    
#     return int(age_in_years)
    
# help(User)
# user = User("Joseph Ochego", 20020802)
# print(user.full_name)
# print(user.birthday)
# print(user.age())

# print("Wow, {} is a beautiful first name - {} is also a beautiful second name".format(user.first_name, user.second_name))

#!! Test

class User:
    id = 89
    name = "no name"
    __password = None
    
    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

u = User("John")
u.id