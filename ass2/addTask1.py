def bubbleSort(size, list):
    for i in range(0, size-1):
        for j in range(0, size-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def main():
    size = int(input())
    list = []
    for i in range(0, size):
        list.append(int(input()))
    print(list)
    print(bubbleSort(size, list))

main()
