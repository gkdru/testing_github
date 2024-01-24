class Cat:
    def __init__(self, weight: float, name: str):
        self.weight = weight
        self.name = name

    def __add__(self, another_cat):
        return f"name:{self.name} name2:{another_cat.name}"


barsik = Cat(10, "Barsik")
mursik = Cat(10, "Mursik")

print(barsik + mursik)


class Point:
    def __init__(self, x: float, y: float, length):
        self.x = x
        self.y = y
        self.__length = length

    def __add__(self, another_point):
        return f"x:{self.x+another_point.x} y:{self.y+another_point.y}"

    def __eq__(self, b):
        return self.x == b.x and self.y == b.y

    def __sub__(self, b):
        return self.x - b.x, self.y - b.y

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, new_length):
        self.__length = new_length


a = Point(1, 2, 0)
b = Point(0, 3, 0)
a.length = 30
print(a.length)