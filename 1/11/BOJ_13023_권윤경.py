import sys
input = sys.stdin.readline
N,M = list(map(int,input().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
    v1, v2 = list(map(int, input().split()))
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(start, visited, graph, answer):
    if answer == 4:
        print(1)
        sys.exit(0)
    
    visited[start] = True    
    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            dfs(i, visited, graph, answer+1)
            visited[i] = False     # dfs에서 빠져나왔다는 것은 제일 안쪽 노드까지 방문하고 다시 나오는 것이므로 방문을 해제시킴

for i in range(0,N):
    visited = [False] * (N)
    dfs(i, visited, graph, 0)
print(0)
