#!/usr/bin/python3

#! A set is an unordered collection of unique items, you cannot have duplicates in sets.
# numList = [1, 2, 3, 4, 5, 5, 6]

# first = set(numList)
# second = {1, 7}

# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# #** Items in a set are not ordered hence you cannot access them with index. 
# # If you try:

# # print(first[0])

# # you get the following error: TypeError: 'set' object is not subscriptable

# if 1 in first:
#   print(True)
  
#! DICTiONARIES

#Keys used should be unique and immutable
# syntax = {key:'value'}

data = {1:"Ochego", 2:"Zayne"}
print(data)

# If you want to fetch the value, you have to specify the key
print(data[2])

# You can also use data wth several differen functions E.g:

print(data.get(1))

#If you try to fetch a data that hasn't been defined, you will not get any response
#If you want to print something when a data doesn't exist you can try this:
data.get(3, "Not Found")
print(data.get(3, "Not Found"))

#If you try this with a key that contains a data already, it will return the value of the key

#** You can create dicts from lists e.g

keys = ['Ochego', 'Joseph', 'Zayne', 'Pie']
Values = ['Broke', 'Happy', 'Status Unknown', 'Sweet']

#We can combine the two lists in one set using zip as follows:
data = zip(keys, Values)
print(set(zip(keys, Values)))
#But this is not a dictionary, to create a dictionary, we use the dict function as follows:

data = dict(zip(keys, Values))
print(data) 

#** Adding to the dict

data['Mary'] = 'Mother'

print(data)

#You can also delete values from the dict using del and the value's key

del data['Zayne']
print(data)

#** You can also nest lists and dicts inside a dictionary
# Here we try this with a dictionary that stores the programming languages and the IDEs they use:

prog = {'HTML': 'VS', "JS": 'Atom', 'Python':['Pycharm', 'Sublime', 'VS'], 'JAVA': {'JSE': 'NetBEans', 'JEE': 'Eclipse'}}

print(prog)

print(prog['JS'])

print(prog.get('CSS'))

print(prog['Python'])

print(prog['Python'] [1])

print(prog['JAVA']['JEE'])

