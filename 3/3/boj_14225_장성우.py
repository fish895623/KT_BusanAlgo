"""
https://www.acmicpc.net/problem/14225


sort -> 2개 합이 그 다음 숫자보다 작다면 그 사이의 작은 숫자가 답이다.

아무리커도 2,000,000 보단 작다.

하나씩 키워가며 더해간다.

"""

from itertools import combinations

dp = [0] * 2000001
dp[0] = 1

n = int(input())
data = list(map(int, input().split()))

for i in range(1, n + 1):  # n번 돌면서
    for j in combinations(data, i):  # i개 뽑아내는 조합을 가져온다.
        dp[sum(j)] = 1

print(dp.index(0))
