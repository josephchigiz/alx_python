def safe_print_division(a, b):
  
  division = a / b
  
  try:
    print("Inside result: {}".format(division))
  except ZeroDivisionError:
    print("None")
  finally:
    return print(safe_print_division(a, b))
  
safe_print_division(a,b)