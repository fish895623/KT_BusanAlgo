## BOJ 11725번문제
import sys
from collections import deque

node = int(input())

edges = [[] for i in range(node+1)]
visited = [0] * (node +1)
partent_node = [0] * (node+1)

for i in range(node-1):
    n1,n2 = map(int,sys.stdin.readline().rstrip().split())
    edges[n1].append(n2)
    edges[n2].append(n1)

# ---------------------------------
# dfs --> 재귀라서 런타임 에러남.... 시스템 재귀 횟수 제한 조절하는거.. 잊음.
# def dfs(graph,v,visited):
#     visited[v] = True
#     # print(v)
#     for e in edges[v]:
#         if not(visited[e]):
#             partent_node[e] = v
#             dfs(edges,e,visited)

# dfs(edges,1,visited)

# for i in range(2,node+1):
#     print(partent_node[i])

# ---------------------------------
# bfs
q = deque([1])
visited[1] = 1
while q:
    next = q.popleft()
    for v in edges[next]:
        if not(visited[v]):
            q.append(v)
            print("현재 노드 -> ",v, "  부모 노드 -> ",next)
            partent_node[v] = next
            visited[v] = 1

for i in range(2,node+1):
    print(partent_node[i])
    
# ---------------------------------
