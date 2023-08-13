"""Task 3"""
from collections.abc import Iterable


class BaseGeometry:
    """This is a BaseGeometry Class"""

    # def __dir__(self) -> None:
    #     """This will control inherited attribute access"""
    #     attributes = super().__dir__()
    #     used_attr = []

    #     for att in attributes:
    #         if att != "__init_subclass__":
    #             used_attr.append(att)
    #     return used_attr
    def __dir__(self) -> None:
        """This will control inherited attribute access"""
        attributes = super().__dir__()
        return [
            attribute for attribute in attributes if attribute != "__init_subclass__"
        ]


def main():
    print(dir(BaseGeometry))


main()
