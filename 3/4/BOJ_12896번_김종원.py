# 도시별로 양방향 그래프이다.
# 최소 비용으로 세우고자 한다.
# 소방소 1개 -> 최적의 위치 최대가 최소인지점.
# 도시의 수와 도로의 연결 상태가 주어질때 최적의 위치에 설치된 소방차가 도착할때 이동해야하는거리 중 최대 거리.

# from collections import deque
# import sys

# Node = int(sys.stdin.readline().strip())
# graph = [[] for i in range(Node+1)]

# for _ in range(Node-1):
#     a,b = map(int,sys.stdin.readline().strip().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# info_119 = Node+1

# for start in range(1,Node+1):
#     box = -1  # 최대인점을 찾아야.
#     q = deque()
#     visited = [0] * (Node+1)
#     cost = 0
#     q.append((start,cost))
#     while q:
#         cur_node, cost = q.popleft()
#         if box < cost:  # 최대 거리
#             box = cost
#             if info_119 < cost:
#                 break
#         visited[cur_node] = True
#         # print(cur_node,"(",cost,")", end=" -> ")
#         for next_node in graph[cur_node]:
#             if not(visited[next_node]):
#                 next_cost = cost + 1
#                 q.append((next_node,next_cost))
#     if info_119 > cost:  # 최소거리
#         info_119 = cost
#     # print()     
# print(info_119)

# 다양한 트리인데
# 상위 트리를 누가 하는 것에 따라서 깊이가 달라진다.


# import sys
# input = sys.stdin.readline
# from collections import deque

# def bfs(idx):
#     visited = [-1]*(n+1)
#     visited[idx] = 0
#     q = deque([idx])
#     while q :
#         now = q.popleft()
        
#         for _next in graph[now] :
#             if visited[_next] == -1:
#                 visited[_next] = visited[now] + 1
#                 q.append(_next)
    
#     cnt = 0
#     node = 0
#     for i in range(1,n+1):
#         if cnt < visited[i]:
#             cnt = visited[i]
#             node = i
#     return node, cnt

# n = int(input())
# graph = [[] for _ in range(n+1)]

# for _ in range(n-1):
#     u,v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# first, firstdist = bfs(1)
# print(first, firstdist)
# second, diameter = bfs(first)
# print(second, diameter)
# print((diameter+1)//2)



# from collections import deque
# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = [[] for _ in range(n + 1)]

# for _ in range(n - 1):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# q = deque()
# q.append(1)
# dist = [-1] * (n + 1)
# dist[1] = 0
# max_node = 0
# max_dist = 0
# while q:
#     now = q.popleft()
#     for nxt in graph[now]:
#         if dist[nxt] == -1:
#             dist[nxt] = dist[now] + 1
#             q.append(nxt)

#             if dist[nxt] > max_dist:
#                 max_dist = dist[nxt]
#                 max_node = nxt

# q = deque()
# q.append(max_node)
# dist = [-1] * (n + 1)
# dist[max_node] = 0
# max_dist = 0
# while q:
#     now = q.popleft()
#     for nxt in graph[now]:
#         if dist[nxt] == -1:
#             dist[nxt] = dist[now] + 1
#             q.append(nxt)

#             if dist[nxt] > max_dist:
#                 max_dist = dist[nxt]
# print((max_dist + 1) // 2)
