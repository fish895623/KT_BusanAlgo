from collections import deque
import sys

def bfs(node, visited, graph):
    visited[node] = True
    queue = deque()
    queue.append((node, 0))
    while queue:
        v, t = queue.popleft()
        if v > 0:
            graph[v].append(v-1)
        if v < n:
            graph[v].append(v+1)
        
        for i in graph[v]:
            if visited[i] == False:
                queue.append((i, t+1))
                visited[i] = True
            if i == e:
                return t+1

input = sys.stdin.readline
n, m = map(int, input().split())
s ,e = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(s,visited,graph))
