# 1) Выведите (через пробел) все четные числа от a до b (включительно).
a = int(input())
b = int(input())

for a in range(a, b + 1):
    if a % 2 == 0 and a != 0:
        print(a, end=' ')

