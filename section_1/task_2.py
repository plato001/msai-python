import sys
sys.setrecursionlimit(3500)


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


if __name__ == '__main__':
    num = 3000
    print(factorial(num))