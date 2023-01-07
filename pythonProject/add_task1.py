# Определите тип треугольника (остроугольный, тупоугольный, прямоугольный) с данными сторонами.
# right для прямоугольного треугольника, acute для остроугольного треугольника, obtuse для тупоугольного
# треугольника или impossible, если входные числа не образуют треугольника.

a, b, c = int(input()), int(input()), int(input())

if a**2+b**2 == c**2:
    print("right")
elif a**2+b**2 > c**2:
    print('acute')
elif a**2 + b**2 < c**2:
    print('obtuse')
elif a + b < c or a + c > b or b + c > a:
    print("impossible")