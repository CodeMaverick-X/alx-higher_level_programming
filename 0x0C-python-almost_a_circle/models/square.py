#!/usr/bin/python3
"""
modlule square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    sqaure class that represents a sqaure
    inherits from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """instance constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """strin print"""
        message = "[Square] ({}) {}/{} - {}"
        return message.format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the object sqaure"""
        attr = ["id", "size", "x", "y"]

        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for i in kwargs:
                setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """returns the sqaure dict"""

        dic = {"id": self.id, "size": self.size,
               "x": self.x, "y": self.y}

        return dic
