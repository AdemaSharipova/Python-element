# 3)Дано целое число n. Выведите следующее за ним четное число.

number = int(input())
print(number + 2 - number % 2)   # number+2 if number is odd minus 1 if not minus 0