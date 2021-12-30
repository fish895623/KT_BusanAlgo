"""
https://www.acmicpc.net/problem/1715


1. 정렬을 하고 작은 값을 더한다.
2. 더한 값을 포함하여 정렬한다. -> 더한 값은 최종값에 계속 더해준다.
3. 1 ~ 2를 반복한다.
만약 남은 갯수가 1개면 반복문을 나간다.

--> 정렬을 sort를 통해서 했었는데 계속 nlogn의 정렬을 n-1만큼 반복해야하므로 O(n^2logn)이 나온다.

정렬을 좀더 빠르게 하는방법을 찾아보았을 때 PQ를 사용하면 들어가는 즉시 정렬이 되므로 빠르게 될 것이라 생각 heapq를 사용




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