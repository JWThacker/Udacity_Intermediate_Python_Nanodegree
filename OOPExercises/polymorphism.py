class Point:
    """ Implement your Point class in here"""
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
    def __str__(self):
        result = f"Point({self._x}, {self._y})"
        return result

    def __add__(self, other):
        sum_x = self._x + other._x
        sum_y = self._y + other._y
        return Point(sum_x, sum_y) 

if __name__ == '__main__':
    origin = Point()
    point = Point(4, 1)
    other_point = Point(3, -3)
    third_point = point + other_point

    print(point)
    print(other_point)
    print(third_point)
