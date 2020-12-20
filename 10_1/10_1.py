class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getStr(self):
        s = self.x, self.y, self.width, self.height
        s_str = __class__.__name__ + ' (' + ', '.join(map(str, s)) + ')'
        return s_str


r1 = Rectangle(5, 10, 50, 100)

print(r1.getStr())
print(type(r1.getStr()))
