if __name__ == "__main__":
    D = input()

    N = len(D)
    Left = 0
    Right = 0
    Count = 0
    Location = 0

    for i in range(N):
        if D[i] == "(":
            Left += 1
            Count += 1
        else:
            Right += 1
            Count -= 1

        if Count <= 1:
            Left = 0

        if Count == -1:
            Location = Right
            break

    if Count > 0:
        Location = Left

    print(Location)
