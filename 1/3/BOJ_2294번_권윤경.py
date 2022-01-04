import sys
input = sys.stdin.readline

n, k =  map(int, input().split())
array = [int(input()) for _ in range(n)]

dp = [sys.maxsize] * (k+1)
dp[0] = 0

for i in array:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i]+1)

if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])
