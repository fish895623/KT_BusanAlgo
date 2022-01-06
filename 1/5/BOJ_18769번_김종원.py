# 18769번

R = 2
C = 3
graph = [[] for i in range((R*C)+1)]
visited = [0] * (R*C+1)
dp = [0] * (R*C+1)
graphs = {
    "vertices" : [1,2,3,4,5,6],
    "edges" : []
}

Redge, Ledge= [[1,3],[3,1]],[[2,4,2]]

# 1,1 -> 1,2  == 1 -> 2 비용이 1 

for r in range(1,R+1):
    for c in range(1,C+1): # 1 2 3
        # (1,2) -> 1차원 배열의 순서에 맞게 돌리는 수식 ((r - 1) * C) +c
        number = ((r-1) * C) + c
        for x,y in ((-1,0),(+1,0),(0,-1),(0,+1)):
            cost =0
            r1 = r + y
            c1 = c + x
            if r1 ==0 or c1 ==0:
                pass
            elif r1 > R or c1 >C:
                pass
            else:
                new_number =  ((r1 -1) *C) + c1
                if r == r1 and c != c1:
                    if c < c1:
                        cost = Redge[r-1][c1 -2]
                    else:
                        cost = Redge[r-1][c1 -1]
                elif r != r1 and c == c1:
                    # 세로축 엣지방향 구하는 공식 r과 r1의 차이가 늘 1
                    if r < r1:
                        cost = Ledge[r1 -2][c1-1]
                    else:
                        cost = Ledge[r -2][c1-1]
                # print("number : ",number,"뉴넘버 : ",new_number, " C1 : ",c1 ," R1  : ",r1)
                graph[number].append((new_number, cost))
                graphs["edges"].append((cost,number,new_number))
                # graph[new_number].append(number) -> 안하는 이유는 모든 좌표에 대해서 탐색을 하니 방향 그래프로 보고 진행하였다.
print(graphs)
# print(visited)
# print(dp)



## BFS로 풀수 없음.
# from collections import deque

# for i in range(1, (R*C+1)):
#     visited = [0] * (R*C+1)
#     dp = [0] * (R*C+1)
#     # print("i 번째 : ",i)
#     q = deque()
#     q.append([i,0])
#     visited[i] = 1 # 방문함
#     print("방문 순서 : ",i, end=" -> ")
#     while q:
#         start, cost = q.popleft()
#         graph[start] = sorted(graph[start], key= lambda x: x[1]) 
#         print(graph[start] )
#         for e,v in graph[start]:
#             # if visited[e] and dp[e] > v:
#             #     dp[e] = v
#             #     print(" 추가 : ",e,"(",v,")", end=" -> ")
#             if not(visited[e]):
#                 visited[e] = e
#                 dp[e] = v
#                 print(e,"(",v,")", end=" -> ")
#                 q.append([e,v])
#     print()
#     print(visited)
#     print(dp,end =" / ")
#     print(sum(dp),end="\n")
#     break
### 최소값으로 갈수있게 수정을 해야한다. 너무 BFS하는데 방문한 노드라면 pass이니 
## 방문한 노드도 현재 노드의 cost보다 낮으면 바뀌게 되어야할 것 같다.
