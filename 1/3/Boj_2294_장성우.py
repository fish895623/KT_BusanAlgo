"""
https://www.acmicpc.net/problem/2294

큰 값부터 원하는 가치전까지 진행하며 작은 값

일단 큰 값부터 나누어지면 제일 작아진다.

i = 15
-> 1) 15/12 = 1 , 15%12 = 3
   2) 3/5 = 0, 3%5 = 3
   3) 3/1 = 3, 3%1 = 0

-> 12로 진행, 5로 진행, 1로 진행 후 가장 작은 값 넣기

 
"""

import sys

# 최대값 설정
INF = 10e9

input = sys.stdin.readline

n, m = map(int, input().split())

data = []

dp = [INF] * (m+1)
dp[0]= 0
for _ in range(n):
    data.append(int(input()))

# data 정렬
data.sort()

for i in data:
    for j in range(i, m+1):
        dp[j] = min(dp[j-i]+1, dp[j])

if dp[m] != INF:
    print(dp[m])
else:
    print("-1")






# def find_coin(coin_value_index, value, dp):

#     # coin_value_index = 들어온 데이터 값 하나씩
#     # max_value = m
#     coin_count = 0
#     max_v = value
#     for i in data[coin_value_index:]:
        
#         count = int(max_v / i)

#         # 나눈 값이 있다면
#         if count > 0:
#             coin_count += count
#             max_v %= i

#     dp[value] = min(coin_count, dp[value])


# for i in range(m, 0, -1):
#     for j in range(len(data)):
#         find_coin(j, i, dp)

# print(dp[m])