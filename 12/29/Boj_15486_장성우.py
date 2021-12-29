"""
https://www.acmicpc.net/problem/15486

"""

import sys

input = sys.stdin.readline

day = []
work = []

n = int(input())

dp = [0] * (n+1)

for _ in range(n):
    a, b = map(int, input().split())
    day.append(a)
    work.append(b)


for i in range(n-1, -1, -1):

    # 일을 할 수 있다면
    if day[i] + i <= n:

        # 자신과 다음값을 비교 범위는 day를 나가는 경우가 있을수도 있으므로 try except로 막기..
        try:
            dp[i] = max(work[i] + dp[i+day[i]], dp[i+1])

        except:
            dp[i] = max(work[i], dp[i+1])

    # 일은 할 수 없지만 다음값이 있는경우
    else:
        if dp[i+1] > 0:
            dp[i] = dp[i+1]

# print(dp)
print(max(dp))