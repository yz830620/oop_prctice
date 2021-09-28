from math import hypot
from typing import Tuple, List

class Point:
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
    def distance(self, other:"Point") -> float:
        return hypot(self.x - other.x, self.y - other.y)

Polygon = List[Point]

def distance(p1: Point, p2: Point):
    return hypot(p1[0]-p2[0], p1[1]-p2[1])

def perimeter(polygon: Polygon):
    pairs = zip(polygon, polygon[1:]+polygon[:1])
    return sum(distance(p1, p2) for p1, p2 in pairs)

if __name__ == "__main__":
    point1 = Point(3,4)
    point2 = Point(5,7)
    point3 = Point(6,2)
    point4 = Point(7,7)
    poly1 = Polygon(point1, point2, point3, point4)
    tri1 = Polygon(point1, point2, point3)

    print("distance of p1 and p2 is: ", distance(point1, point2))
    print("perimeter of poly1 is: ", perimeter(poly1))
    print("perimeter of tri1 is: ", perimeter(tri1))