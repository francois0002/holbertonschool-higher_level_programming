#!/usr/bin/python3
""" class that named Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Define a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Set/get the y coordinate of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set/get the y coordinate of the Square."""
        self.width = value
        self.height = value

    def __str__(self):
        """ return [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """change rectangle with variadic arguments"""
        argc = len(args)
        if argc > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except():
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """make a square dictionnary"""
        square_dict = {}
        square_dict["id"] = self.id
        square_dict["size"] = self.size
        square_dict["x"] = self.x
        square_dict["y"] = self.y
        return square_dict
