class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getradius(self):
        return f"Значение радиуса: {self.radius}"
    def setradius(self, new_radius):
        self.radius = new_radius
circle1 = Circle(5)
print(circle1.getradius())
circle1.setradius(10)
print(circle1.getradius())