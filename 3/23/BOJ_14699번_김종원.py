import sys

# 입력
node ,paths = map(int,sys.stdin.readline().strip().split())
node_depth = list(map(int,sys.stdin.readline().strip().split()))

vertics = [] # 노드마다의 깊이 정보
for k in range(node):
    vertics.append((k+1,node_depth[k]))

edge = [[] for i in range(node+1)] # 그래프 정보

for i in range(paths):
    a,b = map(int,sys.stdin.readline().strip().split())
    if node_depth[a-1] < node_depth[b-1]:
        edge[a].append(b)
    else:
        edge[b].append(a)

# visisted 역할을 dp가 대신 취함
dp = [0] * (node+1)

# 역으로 간다면... 좋은 해법이지 않을까?
vertics.sort(key=lambda x:x[1],reverse=True)

print(edge)
print(vertics)

from collections import deque


for v in vertics:
    cur_node, cur_depth = v
    
    if len(edge[cur_node]) == 0:  # 탐색할 노드가 없다는 것은 맨 위에 있는 노드로 탐색 했던 정보를 1로 취함
        dp[cur_node] = 1
    else:
        for nex in edge[cur_node]:  # 탐색한 노드 정보를 모두 탐색하는데 저장된 노드 정보 보다 큰 정보로 저장.
            dp[ ] = max(dp[cur_node], dp[nex]+1) 
                
for m in range(len(dp)):
    if m!= 0:
        print(dp[m])
      
    
