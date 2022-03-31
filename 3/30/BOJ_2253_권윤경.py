'''
# 점화식 : int((2*n)**0.5 +1) -> n번째 돌에서 경우가 +1 증가함

- int((2*N)^0.5)의 의미
    등차수열의 합 공식 = k(2a+(k-1)d) / 2  
    (a(첫 번째 수) = 1, d(공차) = 1)
    따라서 마지막에 있는 돌까지 가장 빠르게 갈 수 있는 돌들의 수의 합 N
    => k(k+1)/2
    k = (2N-k)^0.5 <= 2N^0.5
'''

import sys
import math

input = sys.stdin.readline
n, mm = map(int, input().split())
m = [int(input()) for _ in range(mm)]

dp  = [[math.inf]* (int((2*n)**0.5)+2)  for _ in range(n+1)]
dp[1][0] = 0
for i in range(2,n+1):
    if i not in m:
        for j in range(1, int((2*i)**0.5)+1):
            dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) +1
            
result = min(dp[n])
if result == math.inf:
    print(-1)
else:
    print(result)