# %%
if __name__ == "__main__":
    N = int(input())

    T_LIST = []
    P_LIST = []

    m = [0 for _ in range(N + 1)]

    # %%
    for _ in range(N):
        T_input, P_input = map(int, input().split())
        T_LIST.append(T_input)
        P_LIST.append(P_input)

    k = 0

    for i in range(N):
        k = max(k, m[i])
        if i + T_LIST[i] > N:
            continue
        m[i + T_LIST[i]] = max(k + P_LIST[i], m[i + T_LIST[i]])
        print(k, m[i], T_LIST[i], m[i+T_LIST[i]])

    print(max(m))
