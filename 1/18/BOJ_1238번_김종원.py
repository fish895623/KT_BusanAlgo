# 학생 N
# 도로 M

import sys
from cmath import inf
from collections import deque

N,M, X = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for i in range(N+1)]


for _ in range(M):
    n1,n2,cost = map(int,sys.stdin.readline().rstrip().split())
    graph[n1].append((n2,cost))

resultM = []

for s in range(1,N+1):
    visited_cost = [ inf ] *(N+1)
    q = deque()
    q.append((s,0))
    visited_cost[0] =0 
    visited_cost[s] =0 
    result = []

    while q:
        nextIdx, cost = q.popleft()
        for e,e_cost in graph[nextIdx]:
            if visited_cost[e] > (e_cost + cost):
                visited_cost[e] = (e_cost + cost)
                q.append((e,e_cost+cost))
    for j in range(1,len(visited_cost)):
        if visited_cost[j] == inf:
            # print(0,end=" ")
            result.append(0)
        else:
            # print(visited_cost[j],end=" ")
            result.append(int(visited_cost[j]))
    resultM.append(result)
    # print()
MAXNUM = 0
X_List = resultM[X-1]
for i in range(len(resultM)):
    if X-1 != i:
        costTime = X_List[i] + resultM[i][X-1]
        if costTime > MAXNUM:
            MAXNUM = costTime
print(MAXNUM)