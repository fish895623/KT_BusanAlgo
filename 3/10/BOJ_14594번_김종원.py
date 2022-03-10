import sys

room = int(sys.stdin.readline().strip()) # 동아리방의 수
monster = int(sys.stdin.readline().strip())  # 빌런의 행동 수
actions = []


for _ in range(monster):
    a,b = map(int,sys.stdin.readline().strip().split())
    actions.append((a,b))


visited = [1] * (room-1)
# 1 | 2 |  3 |  4 |  5


for action in actions:
    start, end = action
    for i in range(start-1,end -1):
        visited[i] = 0
print(sum(visited)+1)