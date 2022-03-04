import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
number = list(map(int, sys.stdin.readline().rstrip().split()))


dp = [0] * (sum(number)+2)  # 만약에 N이 1이고 숫자가 1이면 수열 S의 제일 작은 수는 2인데 +2를 안하면 구할수 없기에 +1이 아니라 2를 했다.
total=0
makeNumber = []
for i in range(1,n+1):
    for v in combinations(number,i):
        dp[sum(v)] = 1

dp.pop(0)
print(dp.index(0)+1)