"""
https://www.acmicpc.net/problem/2156

"""

import sys

input = sys.stdin.readline


n = int(input())

dp = [0] * (n + 1)
dp[0] = 0


data = [0]

for _ in range(n):
    data.append(int(input()))

if len(data) == 1:
    print(0)
elif len(data) == 2:
    print(data[1])
elif len(data) == 3:
    print(data[1] + data[2])
else:
    dp[1] = data[1]
    dp[2] = data[1] + data[2]

    for j in range(3, n+1):

        dp[j] = max(data[j] + data[j-1] + dp[j-3], data[j] + dp[j-2], dp[j-1])

    print(max(dp))



