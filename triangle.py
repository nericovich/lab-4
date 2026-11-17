import math


def validate(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны должны быть положительными")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Такого треугольника не существует")


def perimeter(a, b, c):
    validate(a, b, c)
    return a + b + c


def area(a, b, c):
    validate(a, b, c)
    p = perimeter(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
