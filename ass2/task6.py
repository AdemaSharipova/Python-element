def power(a, n):
    if n == 0:
        return 1
    return power(a, n -1) * a

i = input().split(' ')
a = float(i[0])
n = int(i[1])
print(power(a, n))


