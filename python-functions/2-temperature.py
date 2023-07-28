#!/usr/bin/env python3

def convert_to_celsius(fahrenheit):
  """This function converts the given temperature from fahrenheit to celsius"""
  f = int(fahrenheit)
  celsius = 5/9*(f-32)
  return celsius

print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))