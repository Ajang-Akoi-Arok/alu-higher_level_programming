#!/usr/bin/python3
"""Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance"""
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """Return string representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """Getter for size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """Assign arguments to each attribute"""
        if args and len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
    
    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
