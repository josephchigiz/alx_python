"""Task 3"""


class BaseGeometry:
    """This is a BaseGeometry Class"""

    def __dir__(self) -> None:
        """This will control inherited attribute access"""
        attributes = super().__dir__()
        return [
            attribute for attribute in attributes if attribute != "__init_subclass__"
        ]


def main():
    print(dir(BaseGeometry))


main()
