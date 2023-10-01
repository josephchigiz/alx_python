# import random
# import math

# randlist = ['String', 1.234, 28]
# oneToTen = list(range(12))

# randlist = randlist + oneToTen

# print(randlist[0]) 
# print("List length: {}".format(len(randlist)))

# firstThree = randlist[0:3]

# for i in firstThree:
#     print("{} : {}".format(firstThree.index(i), i))

# #* Check if 'string' is contained in the firstThree variable 
# print('String' in firstThree)
# print("Index of 'String': {}".format(firstThree.index(28)))
# print("How many times does 'String' appear in the list: ", firstThree.count('String'))

# firstThree[0] = "New Item"
# for i in firstThree:
#     print("{} : {}".format(firstThree.index(i), i))
    

# #* Creating a random list of numbers
# numList = []

# for i in range(5):
#     numList.append(random.randrange(1,10))
    
# for i in numList:
#     print(i)

#! Bubble Sort
# import math 
# import random

# numList = []

# for i in range(5):
    
#     numList.append(random.randrange(1, 10))

# i = len(numList) -1

# while i > 1:
    
#     j = 0

#     while j < i:
        
#         print("\nIs {} > {}".format(numList[j], numList[j+1]))
        
#         if numList[j] > numList[j + 1]:
        
#             print("Switch")
                
#             temp = numList[j]
#             numList[j] = numList[j + 1]
#             numList[j + 1] = temp
            
#         else:
#             print("Don't Switch")
            
#         j += 1
        
#         for k in numList:
#             print(k, end=", ")
#         print()
    
    
#     print("END OF ROUND")   
    
#     i -= 1

# for k in numList:
#     print(k, end=", ")
# print()


#! More list functions

# import math
# import random

# numList = []

# for i in range(6):
#     numList.append(random.randrange(1, 11))

# numList.reverse()

# numList.insert(7, 10)

# numList.remove(10)

# numList.pop(3) #removes value at index 3

# for k in numList:
#     print(k, end=", ")

#! List Comprehension

import random
import math

# evenList = [i*2 for i in range(9)]

# for i in evenList:
#     print(i, end=", ")


#* Number Lists

# numList = [1, 2, 3, 4]

# listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
#            for m in numList]

# for i in listOfValues:
#     print(i)
    
#* Multidimensional Lists

