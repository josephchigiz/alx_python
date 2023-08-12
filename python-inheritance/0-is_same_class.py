"""Task 0 module"""


def is_same_class(obj, a_class):
    """This returns true if the object is exactly an instance of the specified class"""
    if isinstance(obj, a_class) == True:
        return True
    else:
        return False
