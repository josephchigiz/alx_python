"""This is task 1"""


def inherits_from(obj, a_class):
    """This returns true if the object an instance of, or if the object is an
    instance of a class that inherited from, the specified class"""
    some_class = type(obj)

    return issubclass(some_class, a_class) and some_class is not a_class
