from sys import stdin

def bfs(start,visited, graph):
    dic=dict()
    from collections import deque
    visited[start] = True
    queue = deque([start])
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i]== False:
                queue.append(i)
                dic[i] = v
                visited[i] = True
    return dic

n = int(stdin.readline())
s=[]
for i in range(n-1):
    s.append(list(map(int, stdin.readline().split())))
    
graph = [[] for _ in range(n+1)]
for v1, v2 in s:
    graph[v1].append(v2)
    graph[v2].append(v1)
visited = [False]*(n+1)

dd = bfs(1, visited, graph)
for i in range(2,n+1):
    print(dd[i])