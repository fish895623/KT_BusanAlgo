n = 7
sch = [
    (3,10),
    (5,20),
    (1,10),
    (1,20),
    (2,15),
    (4,40),
    (2,200)       
]

# n = 10
# sch = [
#     (1,1),
#     (1,2),
#     (1,3),
#     (1,4),
#     (1,5),
#     (1,6),
#     (1,7),
#     (1,8),
#     (1,9),
#     (1,10),
# ]

n = 10
sch = [
    (5,50),
    (4,40),
    (3,30),
    (2,20),
    (1,10),
    (1,10),
    (2,20),
    (3,30),
    (4,40),
    (5,50),
]

from collections import deque
# import sys
# n = int(input())
# sch = []
# for i in range(n):
#     n1,n2 = map(int,sys.stdin.readline().rstrip().split())
#     sch.append((n1,n2))

print(sch)

cost_list = []
for next in range(len(sch)):
    visited = [0] * (len(sch))
    cost = 0
    q = deque([0])
    while q:
        cur = q.popleft()
        next += cur
        if next >= len(sch):  # 퇴사 전날은 Pass
            break
        # print(next, sch[next],cost)
        if not(visited[next]): # 방문을 하지 않았다면,
            if (next + sch[next][0]) > len(sch):
                break
            cost += sch[next][1]
            q.append(sch[next][0])
            visited[next] = 1
    
    # print(cost)
    cost_list.append(cost)
print(max(cost_list))
# print("최대값 : " ,max(cost_list))