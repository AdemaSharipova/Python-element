# 2) Найдите самый маленький натуральный делитель числа x, отличный от 1
x = int(input())
if x == 1 or x == 0:
    print(x)
    exit()
for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        exit()
