N,M = 5,4
Mlist = [(3,1),(3,2),(4,3),(5,3)]

import sys

N,M = map(int, sys.stdin.readline().rstrip().split())
graph =[[] for i in range(N+1)]

for i in range(M):
    n1,n2 = map(int,sys.stdin.readline().rstrip().split())
    # B가 해킹당하면 A가 해킹되기에 n2 -> n1으로 방향 그래프를 표현했다.
    graph[n2].append(n1)

from collections import deque

# rank 변수는 (탐색한 노드 수 , 탐색 시작노드) 정보를 담기 위해 사용됨.
# 현재 [0] * (N) 은 임시로 0으로 초기화함.
rank = [0] * (N)

for num in range(1, N+1):
    rank[num-1] = (1,num) 
    # BFS 코드
    visited = [0] * (N+1)
    q = deque()
    # 순차적으로 1부터 N+1까지 각 노드로 시작하여 BFS를 했을때 제일 많이 탐색되는 노드 정보를 찾는다.
    visited[num] = 1
    q.append(num)
    print(f"{num} ->",end=" ")
    while q :
        nextNode = q.popleft()
        for e in graph[nextNode]:
            if not(visited[e]):
                print(e ,end= " -> ")
                q.append(e)
                # 탐색할 노드를 방문했다고 인증.
                visited[e] = 1
                # rank 변수가 튜플이기에 list로 형변환하여 증감시키고 tuple로 변환
                rank[num-1] = list(rank[num-1])
                rank[num-1][0] += 1
                rank[num-1] = tuple(rank[num-1])

# 랭크 변수에 (탐색 수, 시작 노드) 정보에서 탐색수 기준으로 내림차순으로 정렬을 진행하여
rank = sorted(rank,key= lambda x: x[0],reverse=True)

print(rank)
# 탐색 노드 수가 제일 큰 놈을 찾는다.
MaxNum = max(rank,key=lambda x:x[0])  # or MaxNum = rank[0][0] 정렬이 되어 있기에 0번째 인덱스 값이 제일 큰 수이다.
for i in range(N):
    if rank[i][0] == MaxNum[0]:  # 최대값과 같은 탐색 수일때 출력함.
        print(rank[i][1],end=" ")
    else:
        break

