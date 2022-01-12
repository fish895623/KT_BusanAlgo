"""
https://www.acmicpc.net/problem/1325

효율적인 해킹

"""
#------------------------------------------
# BFS로 데이터를 다 받아오자.
#
from collections import deque

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result_data = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]



for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


# bfs 진행
for i in range(1, n+1):

    visited = [False] * (n+1)
    queue = deque([i])
    cnt = 0
    while queue:
        q = queue.popleft()
        if not visited[q]:
            visited[q] = True
            cnt += 1
            for j in graph[q]:
                if not visited[j]:
                    queue.append(j)

    result_data[i] = cnt

# result = []
result_max = max(result_data)
# result_count = result_data.count(result_max)
# result_index = 0
# result_sum = 0
# for n in range(result_count):

#     print((result_data[result_index:].index(result_max)+result_sum), end=" ")
#     result_index = result_data[result_index:].index(result_max)
#     result_sum += (result_index + 1)
for i, j in enumerate(result_data):
    if j == result_max:
        print(i, end = " ")