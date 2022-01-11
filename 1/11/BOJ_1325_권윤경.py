from collections import deque

def bfs(start, visited, graph):
    result = 1
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                result += 1
    
    return result

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

array = []
for _ in range(M):
     array.append(list(map(int, input().split())))
    
graph = [[] for _ in range(N+1)]
for v1, v2 in array:
    graph[v2].append(v1)

result = 0
result2 = 0
re = []
for i in range(1,N+1):
    visited = [False] * (N+1)
    result = bfs(i,visited,graph)
    if result2 < result:
        re = []
        re.append(i)   
        result2 = result
    elif result2 == result:
        re.append(i)
        
print(*re)