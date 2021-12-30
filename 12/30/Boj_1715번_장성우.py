"""
https://www.acmicpc.net/problem/1715


"""

import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    heapq.heappush(heap,int(input()))



result = 0
while len(heap) > 1:

    first_data = heapq.heappop(heap)
    second_data = heapq.heappop(heap)

    sum_data = first_data + second_data
    result += (sum_data)

    heapq.heappush(heap,sum_data)

print(result)