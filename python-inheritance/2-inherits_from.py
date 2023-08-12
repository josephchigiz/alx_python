"""This is task 1"""


def inherits_from(obj, a_class):
    """This returns true if the object an instance of, or if the object is an
    instance of a class that inherited from, the specified class"""
    some_class = type(obj)

    return (
        isinstance(obj, a_class)
        or some_class == a_class
        or issubclass(some_class, a_class) == True
    )


a = [1, 2, 3]
print(inherits_from(a, list))
