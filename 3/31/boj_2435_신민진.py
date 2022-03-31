import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
lst1 = []

for i in range(N-K+1):
    total = 0
    for j in range(i, i+K):
        total += lst[j]
    lst1.append(total)

print(max(lst1))