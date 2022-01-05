# 2294번
# 3 15
# coinCnt = 3
# k = 15
# coins = [(1,1), (5,1), (12,1)]

import sys
coinCnt, k = map(int,input().split())
coins = []

for ct in coinCnt:
    coins.append(int(sys.stdin.readline().rstrip()))


coins = sorted(coins,reverse=False)
dp = [1000000000001] * (10001)
dp[0] = 0

for c in coins:
    for i in range(1,len(dp)):
        dp[i] = min(dp[i],dp[i-c[0]] + 1)
    # print(dp)
print(dp[k])