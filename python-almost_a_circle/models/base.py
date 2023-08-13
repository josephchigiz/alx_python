"""Base"""


class Base:
    """attribute __nb_objects = 0 is private"""

    __nb_objects = 0
    """ 
    ---
    """

    def __init__(self, id=None):
        """Used to avoid duplication by managing id"""
        if id is not None:
            """
            ---
            """
            self.id = id
        else:
            """
            ---
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
