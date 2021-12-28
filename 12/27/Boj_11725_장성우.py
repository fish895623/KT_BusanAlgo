"""
https://www.acmicpc.net/problem/11725

구현 -> 테스트 문제들은 답이 나오는데 시간초과나옴.

dfs -> 시간초과

bfs -> 통과
 

"""

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)
# bfs 진행

n = int(input())

data = [[] for i in range(n+1)]
visited  =  [False] * (n+1)
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())

    data[a].append(b)
    data[b].append(a)
queue = deque([1])
visited[1]=True

while queue:
    q = queue.popleft()
    for i in data[q]:
        if not visited[i]:
            parent[i] = q
            queue.append(i)

            visited[q] = True
    
for i in range(2, n+1):
    print(parent[i])


# def dfs(val, data, visited):

#     visited[val] = True

#     for i in data[val]:
#         # 방문하지 않은 경우
#         if not visited[i]:
            
#             parent[i] = val
            
#             dfs(i, data, visited)

# dfs(1, data, visited)




# n = int(input())

# data = [[] for i in range(n+1)]
# result = [[] for i in range(n+1)]
# check = []

# # val : 부모노드
# # check_list : 부모들 저장되있는곳
# # result : 
# def find_parent(val, check_list, data, result):
    
#     # 자식이 없으면 패스한다.
#     if len(data[val]) != 0:

#         # 자식이 있는 경우 해당 자식의 부모가 누군지 등록한다.
#         for i in data[val]:

#             # 부모노드들은 뺀다.
#             if i not in check_list:
                
#                 # 부모노드가 되었으므로 추가한다.
#                 check_list.append(i)

#                 # 부모를 등록한다.
#                 result[i] = val

#             # 자식도 반복을 진행한다.
#                 find_parent(i, check_list, data, result)

# for _ in range(n-1):

#     a, b = map(int, input().split())

#     data[a].append(b)
#     data[b].append(a)

# find_parent(1, check, data, result)

# for i in range(2, n+1):
#     print(result[i])


