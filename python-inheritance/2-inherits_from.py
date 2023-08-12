"""This is task 1"""


def inherits_from(obj, a_class):
    """This returns true if the object an instance of, or if the object is an
    instance of a class that inherited from, the specified class"""

    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
