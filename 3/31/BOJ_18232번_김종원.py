# 주예와 방주는 S점에서 만나서 저녁을 먹기로 했다.
# 주예는 점 S에 도착했지만 길치인 방주는 30분이 지나도 나타나지 않아 방주에게 연락하니 E 지점에 있는것을 알게되었고, 직접 E로 간다.

# 1 ~ N까지 각 점에 하나의 텔레포트 정거장이 위치해있고 텔레포트를 통하여 연결되어 있는 다른 텔레포트로 이동가능
# 현재 위치가 X라면 X +1 또는 X-1을 이동하거나 X와 연결된 텔레포트 지점으로 이동 가능하다. 빨리 방주를 만나고자 한다.
# 최소 시간은

import sys
from collections import deque

N, M = map(int,sys.stdin.readline().strip().split())
S, E = map(int,sys.stdin.readline().strip().split())

graph = [[] for i in range(N+1)]

# 텔레포트
for _ in range(M):
    a,b = map(int,sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(S)
min_time = 300001

visited = [0] * (N+1)

while q:
    cur_index = q.popleft()
    if cur_index == E:
        break

    search_space = []
    if len(graph[cur_index]) !=0:
        for j in range(len(graph[cur_index])):
            search_space.append(graph[cur_index][j])

    if cur_index != 1 and cur_index != N:
        search_space = search_space  +  [cur_index + 1, cur_index -1]
    elif cur_index == 1:
        search_space = search_space  +  [cur_index + 1]
    elif cur_index == N:
        search_space = search_space  +  [cur_index -1]

    for next_index in search_space:
        if not(visited[next_index]):
            visited[next_index] = visited[cur_index] + 1
            q.append(next_index)

# print(visited)
print(visited[E])

# 처음 방문했어요. 그 지점을 가는 최소 거리 한번도 방문하지 않는 곳에 그 곳은 최소의 거리이다.
# 절대적으로 제일 앞에 있는 해당 하는 거리가 제일 앞에있는 작으니, 해당 지점에 한번도 방문하지 않는게 최소거리가 된다.
# 만약에 만약에 현재 