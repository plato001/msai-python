from math import factorial


def my_factorial(n):
    i = n
    while i > 1:
        i -= 1
        n *= i
    return n


if __name__ == '__main__':
    num = 3000
    print(my_factorial(num) == factorial(num))
