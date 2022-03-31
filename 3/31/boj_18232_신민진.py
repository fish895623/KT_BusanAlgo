from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    q = deque()
    q.append((node, 0))
    while q:
        x, t = q.popleft()
        if x == E:
            return t
        if 1 <= x <= N:
            if not visited[x]:
                visited[x] = True
                q.append((x+1, t+1))
                q.append((x-1, t+1))
                if len(graph[x]) > 0:
                    for i in graph[x]:
                        q.append((i, t+1))

print(bfs(S))