# 18769번 -> 서브 태스크 1만 맞춤 서브 태스크 2는 시간 초과남 그 이유는 graph 생성 과정에서 1,1, 1,2 이라는 노드 정보를 1 2 로 강제로 변환하는 과정때문에 시간초과 나는 듯함.
## BFS로 풀수 없음.
## 스패닝 트리 중 크루스칼 알고리즘(O(Elog2E))으로 해결해함.
## [ 스패닝 트리가 적용되는 현실 문제 ]

#-------------------------------------------------
## [ 크루스칼 알고리즘 핵심 이론 ]
### 모든 노드들을 최대한 적은 비용으로 연결 시키기 위해 모든 간성 정보를 오름 차순으로 정렬한 뒤
### 비용이 적은 간선부터 그래프에 포함시키는데 사이클이 존재하지 않게 최소 비용 신장 트리를 만든다.
## [ 동작 원리 ]
### 1. 그래프들의 간선 정보를 가중치 기준으로 정렬(오름차순)
### 2. 정렬된 간선 리스트에서 순서대로(가중치가 낮은 간선) 사이클이 생성되지 않게 간선을 선택
### 3. 선택된 간선을 최소 비용 신장 트리 집합에 추가한다.
#-------------------------------------------------

# 변수 저장 상태 -> Redge, Ledge= [[1,3],[3,1]],[[2,4,2]]

T = int(input())
for _ in range(T):
    Redge, Ledge= [],[]
    R,C = map(int,input().split())
    for _ in range(R):
        m = list(map(int,input().split()))
        Redge.append(m)
    for _ in range(R-1):
        n = list(map(int,input().split()))
        Ledge.append(n)

    graphs = {
        "vertices" : [(i+1) for i in range(R*C)],
        "edges" : []
    }
    parent = dict()
    rank = dict()

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
                    # graph[number].append((new_number, cost))
                    graphs["edges"].append((cost,number,new_number))



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
        if root1 != root2:
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
        # print("엣지 : ",edges)
        #간선 연결 (사이클 없게)
        for edge in edges:
            weight, vertice1, vertice2 = edge
            if find(vertice1) != find(vertice2):
                union(vertice1, vertice2)
                minimum_spanning_tree.append(edge)
                minimum_cost += edge[0]
        return minimum_spanning_tree ,minimum_cost
    result = kruskal(graphs)
    print(result[1])
