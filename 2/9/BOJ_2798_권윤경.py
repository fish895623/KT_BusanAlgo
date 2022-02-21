from itertools import combinations

n, m = map(int,input().split())
arr = list(map(int,input().split()))

comb = list(combinations(arr,3))
result = 0
for c in comb:
    tmp = sum(c)
    if tmp <= m and result < tmp:
        result = tmp
print(result)