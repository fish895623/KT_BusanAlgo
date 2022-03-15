n = int(input())

data = []
for i in range(n):
    a, b=  map(int, input().split())
    data.append([a, b])
dp = [0] * (n+5)
for j in range(n-1, -1, -1):
    if j+data[j][0] <= n:
        try:
            dp[j] = max(dp[j+1], dp[j+data[j][0]]+data[j][1])
        except:
            dp[j] = max(dp[j+1], data[j][1])
    else:
        if dp[j+1]>0:
            dp[j] = dp[j+1]
print(max(dp))
