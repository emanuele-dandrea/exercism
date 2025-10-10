def equilateral(sides):
    a, b, c = sides
    return is_triangle(sides) and a == b and a == c

def isosceles(sides):
    a, b, c = sides
    return is_triangle(sides) and (a == b or a == c or b == c)


def scalene(sides):
    a, b, c = sides
    return is_triangle(sides) and a != b and a != c and b != c

def is_triangle(sides):
    for side in sides:
        if side == 0:
            return False
    a, b, c = sides
    return a + b >= c and b + c >= a and c + a >= b