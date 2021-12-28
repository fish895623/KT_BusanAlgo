import sys
from collections import deque


n = int(input())
edges = [[] for i in range(n+1)]
visited = [0] * (n+1)
parent_node = [0] * (n+1)
for i in range(n-1):
    n1, n2 = map(int,sys.stdin.readline().rstrip().split())
    edges[n1].append(n2)
    edges[n2].append(n1)

# bfs
q = deque([1])
visited[1] = 1
while q:
    next = q.popleft()
    for e in edges[next]:
        if not(visited[e]):
            print("현재 노드 : ",e," 부모 : ", next)
            parent_node[e] = next
            q.append(e)
            visited[e]=1

print("------")
for i in range(2,n+1):
    print(parent_node[i])