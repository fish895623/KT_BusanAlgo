# 적어도 C명 늘이기 위해 투자해야하는 돈의 최솟값을 구하는 프로그램
# 홍보할 수 있는 도시 개수 N
# 점화식
# dp[N명을 늘이기 위해 투자하는 비용] = min(dp[N명을 늘이기 위해 투자하는 비용], dp[N명을 늘이기 위해 투자하는 비용 - 현재 방문한 도시가 얻을 수 있는 고객 수] + 현재 도시의 홍보 비용)

import sys

input = sys.stdin.readline
C, N = map(int, input().split())
array = [list(map(int,input().split())) for _ in range(N)]
dp = [sys.maxsize] * (C+1000)
dp[0] = 0

for cost, peo in array:
    for j in range(peo, C+1000):
        dp[j] = min(dp[j], dp[j-peo] + cost)

print(min(dp[C:C+1000]))     

