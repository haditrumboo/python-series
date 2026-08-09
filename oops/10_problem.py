class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}i + {self.y}j"


v = Vector(2, 3)

print(v)