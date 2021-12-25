from sys import stdin

if __name__ == '__main__':
    n, m = map(int, stdin.readline().rstrip().split())
    set_ = set()
    set_1 = set()
    cnt = 0
    for _ in range(n):
        s = stdin.readline().rstrip()
        set_.add(s)
    for _ in range(m):
        s = stdin.readline().rstrip()
        if s in set_:
            cnt += 1
    print(cnt)