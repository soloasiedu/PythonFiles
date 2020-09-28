

class Rectangle:
    """A rectange class."""

    def __init__(self, length, width):
        """Create a new rectangle instance.

        length  the length of the rectangle
        width   the width of the rectangle
        """
        if length > 0:
            self._length = length
        else:
            self._length = 0
        if width > 0:
            self._width = width
        else:
            self._width = 0
        
        
    def get_length(self):
        """Return the length of the rectangle."""
        return self._length
    def get_width(self):
        """Return the width of the rectangle."""
        return self._width
    def area(self):
        """Calculates the area of the rectangle"""
        return self._length * self._width



rectangleList = []

rectangleList.append(Rectangle(-30,20))
rectangleList.append(Rectangle(10,-20))
rectangleList.append(Rectangle(40,-40))

for i in range(3):
    print('Rectange length = ' + str(rectangleList[i].get_length()) \
          + '\nRectangle width = '+ str(rectangleList[i].get_width()) +'\nArea = '+ \
          str(rectangleList[i].area()))
    print()




        
