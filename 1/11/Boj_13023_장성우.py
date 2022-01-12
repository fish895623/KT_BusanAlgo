"""
https://www.acmicpc.net/problem/13023

ABCDE

DFS로 풀면될것같다.
"""
# import sys

# n, m = map(int, input().split())

# visited = [False] * (n+1)
# graph = [[] for _ in range(n+1)]
# flag = False
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# def dfs(graph, v, visited, cnt):

#     visited[v] = True
#     cnt += 1
#     if cnt == 5:
#         return True

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited, cnt)



# for i in range(n):
#     if dfs(graph, i, visited, 0):
#         flag = True
#         break
# if flag:
#     print("1")
# else:
#     print("0")

import sys
from collections import deque

n, m = map(int, input().split())
visited = [False] * (n)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    
for i in range(n):
    cnt = 0
    queue = deque([i])
    while queue:
        q = queue.popleft()
        if not visited[q]:
            visited[q] = True
            queue.append(graph[q])


