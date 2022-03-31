'''
1번은 모두 복사하는 것이므로 (S,C) -> (S,S)
2번은 클립보드 이모티콘을 화면에 붙이는 것으므로, (S,C) -> (S+C, C)
3번은 화면 이모티콘 중 하나를 삭제하는 것이므로 (S,C) -> (S-1,C)
'''
from collections import deque
import math

def bfs(n):
    queue = deque()
    queue.append([1,0])
    e[1][0] = 0
    
    while queue:
        s,c = queue.popleft()
        if e[s][s] == -1:
            e[s][s] = e[s][c]+1
            queue.append([s,s])
        if s+c <=n and e[s+c][c] == -1:   # s+c 가 n보다 크면 구하는 범위를 벗어나니까 s+c<=n 조건이 들어가야함
            e[s+c][c] = e[s][c] +1
            queue.append([s+c,c])
        if s-1 > 0 and e[s-1][c] == -1:    # s-1 이 0보다 작을 수 없으므로 s-1 > 0 조건이 들어가야함
            e[s-1][c] = e[s][c] +1
            queue.append([s-1,c])
            
n = int(input())
e = [[-1 for _ in range(n+1)] for _ in range(n+1)]                
bfs(n)

result = math.inf
for i in range(1,n+1):
    if e[n][i] != -1:
        result = min(result,e[n][i])
        
print(result)