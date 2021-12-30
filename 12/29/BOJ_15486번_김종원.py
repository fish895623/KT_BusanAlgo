n = 7
sch = [
    (0,0),
    (3,10),
    (5,20),
    (1,10),
    (1,20),
    (2,15),
    (4,40),
    (2,200),   
]

import sys

n = int(input())
sch = []
for i in range(n):
    n1,n2 = map(int,sys.stdin.readline().rstrip().split())
    sch.append((n1,n2))
sch.insert(0,(0,0))

dp = [0] * (15000000+1)

for i in range(len(sch)-1,0,-1):
    if (i + sch[i][0]) > n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],  sch[i][1] + dp[i + sch[i][0]])
    

print(max(dp))
