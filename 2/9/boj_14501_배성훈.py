import sys

sys.stdin = open(
    r"D:\KT_BusanAlgo\2\9\14501", "r"
)

N = int(input())

M = []
Q = []
for i in range(N):
    M.append(list(map(int, input().split())))

for i in M:
    Q.append(i[1])

Q.append(0)

TEST = int(input())
result = 0

for i in range(N - 1, -1, -1):
    if M[i][0] + i > N:
        Q[i] = Q[i + 1]
    else:
        Q[i] = max(Q[i + 1], M[i][1] + Q[i + M[i][0]])
result = Q[0]

assert TEST == result
