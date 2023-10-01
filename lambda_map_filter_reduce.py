# def findOdd(num):
#   if num % 2 == 0:
#     return False
#   else:
#     return True
  
# def change_list(list, func):
#   oddList = []
#   for i in list:
#     if func(i):
#       oddList.append(i)
#   return oddList

# aList = range(1, 20)

# print(change_list(aList, findOdd))

#! Function Annotations
# def army_specs(name: str, age: int, weight: float) -> str:
#   print("Name: ", name)
#   print("Age: ", age)
#   print("Weight: ", weight)
  
#   return "{} is {} years old and can throw a punch worth {} kgs.".format(name, age, weight)

# print(army_specs("Ochego", 21, 79))
# print(army_specs("Ogweno", 23, 55))

# print(army_specs.__annotations__)

#! Anonymou functions using Lambda
# sum = lambda x, y: x + y
# print("Sum: ", sum(4, 6))

# can_vote = lambda age: True if age >= 18 else False

# print("Can Vote: ", can_vote(17))

# powerList = [lambda x: x ** 2,
#              lambda x: x ** 3,
#              lambda x: x ** 4]
# for func in powerList:
#   print(func(4))
  
# #* Lambdas can also be stored inside of dictionaries.

# attack = {'Power': lambda: print('Power Attack'),
#           'Quick': lambda: print('Quick Attack'),
#           'Silent': lambda: print('Silent Attack')}

# import random

# attackKey = random.choice(list(attack.keys()))

# attack[attackKey]()

#!Create a list that holds 100 Hs and Ts and outputs the number of Hs and Ts.
# import random
# #* Create the list
# flipList = []
# #* Populate the list with 100 Hs and Ts
# for i in range(1, 101):
#   flipList += random.choice(['H', 'T'])
  
# #* Output the numbers
# print('Heads: ', flipList.count('H'))
# print('Tails: ', flipList.count('T'))

#!! Map function

# oneTo10 = range(1, 11)

# def dbl_num(num):
#   return num * 2

# print(list(map(dbl_num, oneTo10)))

# #* using map with lambda
# print(list(map((lambda x: x * 3), oneTo10))) 

# aList = list(map((lambda x, y: x + y), [1, 2, 3], [2, 4, 6]))
# print(aList)


#!! Filter
# #* In this example we use filter to only print even values

# print(list(filter((lambda x: x % 2 == 0), range(1, 11))))

# #* Find the multiples of 9 from a 100 value list if the range of the values is 1 and 1000:
# import random
# randList = list(random.randint(1, 1001) for i in range(100))
# print(list(filter((lambda x: x % 9 == 0), randList)))

#!! Reduce 
from functools import reduce

print(reduce((lambda x, y: x + y), range(1, 6)))
