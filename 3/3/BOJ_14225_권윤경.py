#  수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수

s = int(input())
arr = list(map(int, input().split()))
tmps = []
from itertools import combinations

for i in range(1, s + 1):
    tmp = list(combinations(arr, i))
    for j in tmp:
        tmps.append(sum(j))

su = set(tmps)
notsu = [i for i in range(1, max(su) + 2)]
print(min(set(notsu) - su))
