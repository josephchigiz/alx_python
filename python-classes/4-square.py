"""This is a square module"""
class Square:
  """This class represents a square"""
  def __init__(self, size=0):
    """Initialize the square with the given size"""
    self.__size = size
    
    if not type(size) is int:
      raise TypeError("size must be an integer")
    elif size < 0:
      raise ValueError("size must be >= 0")
  
  @property
  def size(self):
    return  self.__size
      
  @size.setter
  def size(self, value):
    self.__size = value
    
    if not type(value) is int:
      raise TypeError("size must be an integer")
    elif value < 0:
      raise ValueError("size must be >= 0")
    
  def area(self):
    sq = int(self.__size) * int(self.__size)
    return sq 
  
  def my_print(self):
    
    if self.__size == 0:
      print()
    else:
      for _ in range(self.__size):
        print("#" * self.__size)
      