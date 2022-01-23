if __name__ == '__main__':
    # input
    N, M = map(int, input().split())
    # output
    print("\n".join([" ".join(map(str, [i*j for j in range(1, M + 1)])) for i in range(1, N + 1)]))
