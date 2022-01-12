"""
https://www.acmicpc.net/problem/13305

1. start oil은 무조건 넣는다.
2. oil 넣는 양은 자신의 다음 oil값이 작은 값이 나올때 까지 진행

결국 n만큼 돌면서 계산하면된다,

"""

import sys

input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split())) 
oil = list(map(int, input().split())) 

min_oil_val = 10000000000000

result = 0
min_index = 0



for num, oil_price in enumerate(oil):

    if oil_price <= min_oil_val:

        # 오일 값 더해주기
        result += min_oil_val*sum(road[min_index : num])
        # 최소 오일값 바꾸기
        min_oil_val = oil_price
        # 인덱스값 바꾸기
        min_index = num

if min_index != n-1:
    result += min_oil_val*sum(road[min_index :])

print(int(result))


