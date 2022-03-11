import sys

try:
    sys.stdin = open("3/10/14594.txt", "r")
except:
    pass

N = int(input())
M = int(input())
ACT = [list(map(int, input().split())) for _ in range(M)]

DICT = {i + 1: True for i in range(N)}

for a, b in ACT:
    for i in range(a, b):
        DICT[i] = False

count = 0
for _, k in DICT.items():
    if k:
        count += 1

print(count)
