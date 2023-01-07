def Election(x, y, z):
    count_false: int = 0
    count_true: int = 0
    set = (x, y, z)

    for i in range(0, 3):
        if set[i] == 1:
            count_true += 1
        elif set[i] == 0:
            count_false += 1

    if count_true > count_false:
        return int(True)
    return int(False)




def main():
    i = input().split(' ')
    x, y, z = int(i[0]), int(i[1]), int(i[2])
    print(Election(x, y, z))

main()