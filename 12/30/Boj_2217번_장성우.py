"""
https://www.acmicpc.net/problem/2217




"""

import sys

input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

# 데이터 정렬
data.sort()
result = 0
"""
(작은 수 * 밧줄갯수) -> 수가 커지면서 밧줄 갯수도 하나씩 빠짐

w/k -> 에서 각 밧줄이 버틸 수 있는 가장 큰 값이 버틸 수 있는 힘이 가장 작은 밧줄 * k 이다.
"""

for i in range(n):
    result = max(data[i] * (n - i), result)


print(result)