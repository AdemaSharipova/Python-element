
a = str(input())
j = 0
result: int = 0

for i in range(len(a) - 1, -1, -1):
    result += int(a[j]) * (2 ** i)
    j += 1


print(result)
