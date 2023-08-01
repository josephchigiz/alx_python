def safe_print_division(a, b):
  
  try:
    result = a / b
    return print("Inside result: {}".format(result))
  except (ZeroDivisionError, RecursionError):
    return None
  finally:
    return result
  
