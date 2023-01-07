# Даны действительные числа a, b, c. Найдите все решения квадратного уравнения ax2 + bx + c = 0.

a, b, c = int(input()), int(input()), int(input())

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** 0.5) / 2 * a
    x2 = (-b - d ** 0.5) / 2 * a
    print(x1, x2)
elif d == 0:
    print(-b/ (2 * a))
