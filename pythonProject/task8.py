# 8)Даны три натуральных числа a, b, c, записанные в отдельных строках.
# Определите, существует ли треугольник.

a, b, c = int(input()), int(input()), int(input())

if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
