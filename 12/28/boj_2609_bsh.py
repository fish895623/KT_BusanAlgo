from sys import stdin

input = stdin.readline


def least_com_mul(a, b) -> int:
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def great_com_factor(a, b) -> int:
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i


if __name__ == "__main__":
    a1, b1 = map(int, input().rstrip().rsplit())
    print(least_com_mul(a1, b1))
    print(great_com_factor(a1, b1))
