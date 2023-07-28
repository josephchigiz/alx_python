def is_prime(number):
  """This function returns true if a number is prime and false if otherwise"""
  n = int(number)
  if n == 2 or n == 3:
    return True
  
  for i in range(2, n):
    if n % i == 0:
      return False
    
print(is_prime(3))