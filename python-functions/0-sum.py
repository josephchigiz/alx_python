#!/usr/bin/env python3
def add(a, b):
  
  return a + b
  
  match a, b:
    case (1, 2):
      print(add(1, 2))
    case (98, 0):
      print(add(98, 0))
    case (100, -2):
      print(add(100, -2))
    case (0,0):
      print(add(0, 0))
      
print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
print(add(0, 0))


