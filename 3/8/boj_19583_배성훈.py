import sys

try:
    sys.stdin = open("3/8/19583.txt", "r")
except FileNotFoundError:
    pass

S, E, Q = input().split()
S = int("".join(S.split(":")))
E = int("".join(E.split(":")))
Q = int("".join(Q.split(":")))

check = set()
cnt = 0

while True:
    try:
        time, name = input().split()
        time = int("".join(time.split(":")))
        if time <= S:
            check.add(name)
        elif E <= time <= Q and name in check:
            check.remove(name)
            cnt += 1
    except EOFError:
        break

print(cnt)
