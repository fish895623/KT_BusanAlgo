#n 개의 도시가 있다.
# m개의 버스가 있다.
# graph = [[], [(2, 2), (3, 3), (4, 1), (5, 10), (4, 2)], [(4, 2)], [(4, 1), (5, 1), (5, 10), (1, 8), (4, 2)], [(5, 3)], [(1, 7), (2, 4)]]

import sys
from cmath import inf
from collections import deque

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = [[] for i in range(N+1)]


for _ in range(M):
    n1,n2,cost = map(int,sys.stdin.readline().rstrip().split())
    graph[n1].append((n2,cost))

for s in range(1,N+1):
    visited_cost = [ inf ] *(N+1)
    q = deque()
    q.append((s,0))
    visited_cost[0] =0 
    visited_cost[s] =0 

    while q:
        nextIdx, cost = q.popleft()
        for e,e_cost in graph[nextIdx]:
            if visited_cost[e] > (e_cost + cost):
                visited_cost[e] = (e_cost + cost)
                q.append((e,e_cost+cost))
    for j in range(1,len(visited_cost)):
        if visited_cost[j] == inf:
            print(0,end=" ")
        else:
            print(visited_cost[j],end=" ")
    print()
