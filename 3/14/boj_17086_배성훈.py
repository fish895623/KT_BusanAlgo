"""
구글신!! 나를 도와줘서 고마워!!
"""
import sys
from collections import deque

try:
    sys.stdin = open("3/14/17086.txt", "r")
except:
    pass


N, M = map(int, input().split())
b = []
c = deque()
for i in range(N):
    t = list(map(int, input().split()))
    for j in range(M):
        c.append((i, j))
    b.append(t)

X = [-1, -1, -1, 0, 1, 0, 1, 1]
Y = [-1, 0, 1, 1, 1, -1, 0, -1]


def bfs():
    while c:
        x, y = c.popleft()
        for k in range(8):
            dx = x + X[k]
            dy = y + X[k]
            if 0 <= dx < N and 0 <= dy < M:
                if b[dx][dy] == 0:
                    c.append((dx, dy))
                    b[dx][dy] = b[x][y] + 1


bfs()
safe = 0
for i in range(N):
    for j in range(M):
        safe = max(safe, b[i][j])

print(safe - 1)
