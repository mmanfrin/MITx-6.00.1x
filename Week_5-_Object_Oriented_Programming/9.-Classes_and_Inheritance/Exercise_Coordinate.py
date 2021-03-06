class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):            
        if other.x == self.x and other.y == self.y:
            return True
        else:
            return False
           
    def __repr__(self):
        return 'Coordinate({},{})'.format(self.x, self.y)
    
c1 = Coordinate(1,2)
c2 = Coordinate(10,22)
c3 = Coordinate(1,2)

print(c1)
print(c2)
print(c1 == c2)
print(c1 == c3)
print(repr(c2))