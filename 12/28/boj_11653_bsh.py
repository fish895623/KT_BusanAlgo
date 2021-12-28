from sys import stdin

input = stdin.readline


if __name__ == "__main__":
    N = int(input().rstrip())

    num = 2
    while num <= N:
        if N % num == 0:
            print(num)
            N = N / num
        else:
            num = num + 1
