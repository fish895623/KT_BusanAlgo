"""
문제 링크 : https://www.acmicpc.net/problem/17086
푼 날짜 : 220314
문제 유형 : 그래프


풀이 : 
일단 1 주변 방향으로 다 1로 만들어버리기
이후 0의 최대값을 확인하면된다. (dfs)
는 무슨 bfs로 풀어야했다
"""

import sys
from collections import deque
n, m = map(int, input().split())
graph = []
q = deque()
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == 1:
            q.append((i,j))
    graph.append(data)


def bfs():
    dx = [-1, -1, 0,  1,  1, 1, 0, -1]
    dy = [0, -1, -1 , -1, 0, 1, 1, 1]
    while q:
        x, y = q.popleft()
        for a in range(8):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0<= nx <= n-1 and 0<=ny<=m-1:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

bfs()
result = 0
for i in range(n):
    for j in range(m):
        result = max(graph[i][j], result)
print(result-1)
# graph_save = [[0] * m for _ in range(n)]




# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             graph_save[i][j] = 1
#             for k in range(8):
#                 nx = dx[k] + j
#                 ny = dy[k] + i

#                 if 0<= nx <= m-1 and 0<=ny<=n-1:
#                     graph_save[ny][nx] = 1
# # print(graph_save)

# def dfs(x, y):
#     global result

#     if graph_save[x][y] == 0:
#         graph_save[x][y] = 1
#         result += 1
#         for i in range(8):
#             nx = dx[i] + x
#             ny = dy[i] + y

#             if 0<= ny <= m-1 and 0<=nx<=n-1:
#                 dfs(nx,ny) 
                
#     return 0

# max_val = 0
# for i in range(n):
#     for j in range(m):
#         if graph_save[i][j] == 0:
#             result = 0
#             dfs(i,j)
#             max_val = max(max_val, result)
# print(max_val)

    
