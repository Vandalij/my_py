import math



class Rectangle:


    def __init__(self, width, height):
        self.width = width
        self.height = height


    def get_square(self):
        return self.width * self.height


    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return math.isclose(self.get_square(), other.get_square(), rel_tol=1e-9)
        return False


    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_area = self.get_square() + other.get_square()
            side = math.sqrt(new_area)
            return Rectangle(side, new_area / side)
        return None

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            new_area = self.get_square() * n
            side = math.sqrt(new_area)
            return Rectangle(side, new_area / side)
        return None

    def __str__(self):
        return f"Rectangle({self.width:.4f} x {self.height:.4f}) = {self.get_square():.4f}"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

print("r1:", r1)
print("r2:", r2)

r3 = r1 + r2
print("r3:", r3)
print("r3 area:", r3.get_square())
assert math.isclose(r3.get_square(), 26, rel_tol=1e-9), 'Test3'

r4 = r1 * 4
assert math.isclose(r4.get_square(), 32, rel_tol=1e-9), 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
