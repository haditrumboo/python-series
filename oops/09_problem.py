class Complex:
    def __init__(self, n, b):
        self.n = n
        self.b = b

    def __add__(self, other):
        return Complex(self.n + other.n, self.b + other.b)


c1 = Complex(2, 3)
c2 = Complex(4, 5)

c3 = c1 + c2

print(c3.n, c3.b)