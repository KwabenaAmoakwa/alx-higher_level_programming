#/usr/bin/python3
"""Implementation of sqaure class module"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    class Square.

    Args:
        None

    Returns:
        None
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size
    
    def __str__(self):
        """
        Display string version of class
        """
        s = f"{self.x}/{self.y}"
        return f"[Rectangle] ({self.id}) {s} - {self.__size}"
