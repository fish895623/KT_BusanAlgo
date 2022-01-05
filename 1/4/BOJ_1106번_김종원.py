# BOJ 1106번
import sys

cityInfo = []
target, Node = map(int,sys.stdin.readline().rstrip().split())
for i in range(Node):
    n1,n2 = map(int,sys.stdin.readline().rstrip().split())
    cityInfo.append((n1,n2))

dp = [10001] * (target+100000)

# 인원 기준으로 정렬
cityInfo = sorted(cityInfo,key=lambda x: x[1])

dp[0] = 0
for money,cnt in cityInfo:
    for j in range(1, target+100):
        dp[j] = min(dp[j],  dp[j -cnt] + money)
    # print(dp)
print(min(dp[target:]))