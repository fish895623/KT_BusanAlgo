"""
https://www.acmicpc.net/problem/2798
블랙잭

1. sort
2. M보다 작은 수만 가져오기
3. 

3개 뽑기
"""

import sys

max_result = 0

n, m = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            if data[i] + data[j] + data[k] <= m and data[i] + data[j] + data[k] >= max_result:
                max_result = data[i] + data[j] + data[k]

print(max_result)



