"""This is task 1"""


def is_kind_of_class(obj, a_class):
    if issubclass(obj, a_class) == True:
        return True
    else:
        return False
