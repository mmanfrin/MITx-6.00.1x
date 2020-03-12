class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        self.result = []
        for i in self.vals:
            if i in other.vals:
                self.result.append(i)
        return '{' + ','.join([str(f) for f in self.result]) + '}' 
    
    def __len__(self):
        """Loops through the list, counting the number of items, and returns the number of items
           as an int"""
        self.counter = 0
        for i in self.vals:
            self.counter += 1
        return self.counter

s1 = intSet()
s1.insert(1)
s1.insert(2)
s1.insert(5)

s1.member(2)
s1.member(4)

s1.remove(2)
# s1.remove(4)

s2 = intSet()
s2.insert(1)
s2.insert(3)
s2.insert(4)
s2.insert(5)

s2.member(3)
s2.member(5)

s2.remove(3)

print(s1)
print(s2)
print(len(s1))
print(s1.intersect(s2))