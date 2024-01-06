def equilateral(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] == sides[2]
    return False


def isosceles(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]
    return False


def scalene(sides):
    if is_triangle(sides):
        return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
    return False

def is_triangle(sides):
    for side in sides:
        if side == 0:
            return False
            
    con_one = (sides[0] + sides[1]) >= sides[2]
    con_two = (sides[1] + sides[2]) >= sides[0]
    con_three = (sides[0] + sides[2]) >= sides[1]
    
    return con_one and con_two and con_three
