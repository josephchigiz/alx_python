#!/usr/bin/env python3
def convert_to_celsius(fahrenheit):
  """This function converts the given temperature from fahrenheit to celsius"""
  celsius = round(((fahrenheit - 32) * (5 / 9)), 2)
  return celsius
