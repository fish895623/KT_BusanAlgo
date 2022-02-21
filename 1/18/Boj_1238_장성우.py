"""
https://www.acmicpc.net/problem/1238

"""

import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]



for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c



for k in range(1, n+1):
    for a in range(1, n+1):
        if k == a:
            continue
        for b in range(1, n+1):
            if k == b:
                continue

            if a==b:
                graph[a][b] = 0
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

max_len = 0

for i in range(1, n+1):
    max_len = max(graph[i][x] + graph[x][i], max_len)

print(max_len)