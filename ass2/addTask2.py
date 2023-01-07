def phi(n):
    if n == 1 or n == 2:
        return 1
    return phi(n-1) + phi(n-2)

def main():
    n = int(input())
    print(phi(n + 1))

main()