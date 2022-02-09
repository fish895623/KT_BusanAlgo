import sys

sys.stdin = open(
    r"D:\KT_BusanAlgo\2\9\2798", "r"
)

N, M = map(int, input().split())
S = list(map(int, input().split()))

MAX = 0
_sum = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            _sum = S[i] + S[j] + S[k]
            if _sum > M:
                continue
            else:
                MAX = max(MAX, _sum)
print(MAX)
