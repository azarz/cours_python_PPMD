class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def deplacer(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

class Point3D(Point2D):

    def __init__(self, x, y, z):
        Point2D.__init__(self, x, y)
        self.z = z
    
    def deplacer(self, dx, dy, dz):
        self.x = self.x + dx
        self.y = self.y + dy
        self.z = self.z + dz


point = Point3D(1, 1, 2)
point.getX()
>> 1
point.deplacer(1, 2, 3)
point.z
>> 5
point.y
>> 3
point.deplacer(1, 1)
>>"TypeError: deplacer() missing 1 required positional argument: 'dz'"

