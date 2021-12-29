if __name__ == "__main__":
    N = int(input())

    T_LIST = []
    P_LIST = []

    m = [0 for i in range(N)]
    print(m)

    for i in range(N):
        T, P = map(int, input().rsplit())
        assert 1 <= T and T <= 50
        assert 1 <= P and P <= 1000
        T_LIST.append(T)
        P_LIST.append(P)

    _MAX = 0
    for i in range(N):
        _MAX = max(_MAX, m[i])
        if i + T[i] 
