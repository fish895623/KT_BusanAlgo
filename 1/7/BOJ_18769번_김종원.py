# 18769번
T = 3
R , C = 2,3
Redge = [[1,3], [3,1]]
Ledge = [[2, 4, 2]]

graph = {
    "vertices" :[],
    "edges" :[]
}

# 1,1  ->  1,2  1  0 0
# 1,2  ->  1,3  3  0 1

# 2,1  ->  2,2  3  1 0
# 2,2  ->  2,3  1  1 1

# 1,2 -> 2,2
# 1,1 -> 2,1

# R = 2, C =3
# X -> i Y -> j

#vertice 초기화
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

#해당 vertice의 최상위 정점을 찾는다
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

#두 정점을 연결한다
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]: 
            rank[root2] += 1

def kruskal(graph):
    minimum_spanning_tree = []
    minimum_cost = 0
    #초기화
    for vertice in graph['vertices']:
        make_set(vertice)

    #간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()
    
    #최소 간선 순으로 연결 (사이클 없게)
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            # print("vertice1 : ",vertice1, " -> vertice2 : ",vertice2)
            union(vertice1, vertice2)
            # print("Par : ",parent)
            minimum_spanning_tree.append(edge)
            minimum_cost += edge[0]
    return minimum_spanning_tree ,minimum_cost

import sys

T = int(input())
for _ in range(T):
    Redge, Ledge= [],[]
    R,C = map(int,sys.stdin.readline().rstrip().split())
    for _ in range(R):
        m = list(map(int,sys.stdin.readline().rstrip().split()))
        Redge.append(m)
    for _ in range(R-1):
        n = list(map(int,sys.stdin.readline().rstrip().split()))
        Ledge.append(n)
    graph = {
    "vertices" :[],
    "edges" :[]
    }

    for i in range(1,R+1):
        for j in range(1, C+1):
            
            graph["vertices"].append((i,j))
            # i,j -> x,y
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                NextX = i + x
                NextY = j + y
                if NextX >=R+1 or NextY >= C+1: # 열을 넘어간 경우 탐색 X
                    pass
                elif NextX == 0 or NextY == 0: # 좌표가 1부터 시작하는데 0이된 경우 pass
                    pass
                else:
                    if NextX == i and NextY != j:
                        # print("R엣지에서 : ",i,j , " -> ",NextX, NextY,"\n")     # R엣지 정보를 구하기 위해 좌표가 어떻게 이동하는지 주석을 제거하면 확인가능함.
                        cost = Redge[NextX-1][max(NextY,j)-2]
                        graph["edges"].append((cost, (i,j), (NextX,NextY)))
                    elif NextX !=i and NextY == j:
                        # print("L엣지에서 : ",i,j , " -> ",NextX, NextY,"\n")     # L엣지 정보를 구하기 위해 좌표가 어떻게 이동하는지 주석을 제거하면 확인가능함.
                        cost = Ledge[max(NextX,i)-2][NextY-1]
                        graph["edges"].append((cost, (i,j), (NextX,NextY)))
    # print(graph)

    parent = dict()
    rank = dict()
    result = kruskal(graph)
    print(result[1])