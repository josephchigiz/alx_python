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
<<<<<<< HEAD
    
    self.__size = int(value) 
     
=======
    self.__size = int(value)  
>>>>>>> a8a2011b731c7ee98d5a34c4acd281aae58e8756
    
  def area(self):
    sq = int(self.__size) * int(self.__size)
    return sq 
  

