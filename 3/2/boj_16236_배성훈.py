import sys

###############################################################################
# https://mingchin.tistory.com/262
###############################################################################
sys.stdin = open(file="3/2/16236.txt", mode="r")
N = int(input())
K = [list(map(int, input().split())) for _ in range(N)]
SIZE = 2
COUNT = 0
ANSWER = int(input())
###############################################################################
# - If val is 1 move to loc
# - If val more than 1, move to nearest
# - If val is same as SIZE , += 1
# - Can't move to larger than SIZE
# - Leftside first
###############################################################################
def bfs(g, start, n, eat):
    global SIZE, COUNT
    visit = [0] * (n**2)
    q = [start]
    x, y = start
    move = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    visit[n * x + y] = 1
    d = 0
    while q:
        d += 1
        tmp = []
        eats = []
        for a, b in q:
            for i, j in move:
                if 0 <= a + i < n and 0 <= b + j < n:
                    if 0 < g[a + i][b + j] < SIZE and not visit[(a + i) * n + b + j]:
                        eats.append((a + i, b + j))
                    elif (
                        g[a + i][b + j] == 0 or g[a + i][b + j] == SIZE
                    ) and not visit[(a + i) * n + b + j]:
                        tmp.append((a + i, b + j))
                        visit[(a + i) * n + b + j] = 1
        if eats:
            eats.sort()
            p, q = eats[0]
            eat += 1
            COUNT += d
            g[p][q] = 0
            g[x][y] = 0
            if eat == SIZE:
                SIZE += 1
                eat = 0
            return bfs(g, eats[0], n, eat)
        q = tmp
    return


for i in range(N):
    for j in range(N):
        if K[i][j] == 9:
            bfs(K, (i, j), N, 0)
            break
assert COUNT == 3
