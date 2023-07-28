def fibonacci_sequence(n):
  """This function will print the fibonacci sequence to the value of n"""
  f_list = []
  a, b = 0, 1
  while a < n:
    f_list.append(a)
    a, b = b, a+b
  return f_list
