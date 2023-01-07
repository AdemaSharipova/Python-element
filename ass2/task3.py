# 3) Выведите все натуральные делители числа x в порядке возрастания
x = int(input())
for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=' ')
