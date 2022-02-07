"""
https://www.acmicpc.net/problem/11404


이코테보고 진행했음,

이해하고 넘어가자.
"""

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] == INF:
        graph[a][b] = c
    else:
        graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("0", end = " ")
        else:
            print(graph[a][b], end = " ")
    print()