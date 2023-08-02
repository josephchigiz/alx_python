#!/usr/bin/python3
raise_exception_msg = __import__('5-raise_exception_msg').raise_exception_msg

try:
    message = "Python is cool"
    raise_exception_msg(message)
except NameError as ne:
    print(ne)