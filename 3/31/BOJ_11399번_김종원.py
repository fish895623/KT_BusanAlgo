# 사람들이 1번부터 N번까지 줄을 서있다.
# i번 사람이 인출하는데 걸리는 시간이 Pi이다.
# 사람들이 줄을 서는 순서에 따라서 돈을 인출하는 필요한 시간의 합이 다라진다.

# 2,5,1,4,3
# 1 2 3 3 4
import sys

person = int(sys.stdin.readline().strip())
time = list(map(int,sys.stdin.readline().strip().split()))

# 총 걸린 시간 정보를 담는다.
dp = [0] * person

time.sort()

total = 0 # 누적합 업데이트
for i in range(person):
    total += time[i]
    dp[i] = total

print(sum(dp))