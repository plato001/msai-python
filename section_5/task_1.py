if __name__ == '__main__':
    # input
    N, M = map(int, input().split())
    # output
    for i in range(1, N + 1):
        buf = []
        for j in range(1, M + 1):
            buf.append(i * j)
        print(" ".join(map(str, buf)))
