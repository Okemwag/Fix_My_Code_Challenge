#!/usr/bin/python3
"""
This is a square class I'm debugging
"""


class square():
    """ Printing a square """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ instance initializer """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.width

    def perimeter(self):
        """ perimeter printer """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returning the str format """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ driver code """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter())
