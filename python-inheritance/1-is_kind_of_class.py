"""This is task 1"""


def is_kind_of_class(obj, a_class):
    """This returns true if the object an instance of, or if the object is an
    instance of a class that inherited from, the specified class"""
    if issubclass(obj, a_class) == True:
        return True
    else:
        return False
