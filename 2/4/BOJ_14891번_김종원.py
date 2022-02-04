# 첫번째 줄 1번 톱니바퀴의 상태,
# 둘번째 줄 2번 톱니바퀴의 상태,
# 세번째 줄 3번 톱니바퀴의 상태,
# 네번째 줄 4번 톱니바퀴의 상태
# 12시부터 시계방향으로 값이 채워지는데 0 : N, 1 : S
# N 과 N이면 멈춤/ N 과 S로 서로 다르면 회전.(시계 또는 반시계)
# 다섯번째 줄 K라는 회전 수(1<k<=100)
# 첫번째 인자 : 톱니바퀴 번호, 두번째 인자는 돌린 방향(1 : 시계방향, -1 : 반시계방향)

# t1 = [1, 0, 1, 0, 1, 1, 1, 1]
# # 시계방향
# t1 = [1, 1, 0, 1, 0, 1, 1, 1]  -> [-1]번째 인덱스를 pop()하고 맨앞으로 insert하면 됨
# # 반시계방향
# t1 = [0, 1, 0, 1, 1, 1, 1, 1]  -> [0]번째 인덱스를 pop(0)하고 맨뒤에 append하면 됨.

# 회전 체크시 인덱스 번호는 2번째와 -2번째 인덱스가 서로 같은지 다른지 확인해야한다.
# 회전시 서로 극이 다르면 돌아간 톱니의 방향에 반대 방향으로 회전

from copy import deepcopy
from collections import deque
import sys

T = []
for _ in range(4):
    m = sys.stdin.readline().rstrip()
    T.append([int(i) for i in m])

T1 = deepcopy(T)

order_list = []

# 톱니바퀴 탐색 가능한 범위
graph = [[],[2], [1,3], [2,4], [3]]

k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    p1,p2 = map(int,sys.stdin.readline().rstrip().split())
    order_list.append([p1,p2])

def rotation_T1(choice_t, signal):
    if signal == -1:
        tmp = T1[choice_t-1].pop(0)
        T1[choice_t-1].append(tmp)

    elif signal == 1:
        tmp = T1[choice_t-1].pop()
        T1[choice_t-1].insert(0,tmp)

def checkValue(choice):
    return (T[choice-1][2],T[choice-1][-2])


for start_number, signal in order_list:
    visited = [0,0,0,0,0]
    visited[start_number] = 1
    q = deque()
    q.append((start_number,signal))
    while q:
        curr, curr_signal = q.popleft()
        right_curr, left_curr = checkValue(curr)
        # print(curr,end = " -> ")
        for next in graph[curr]:
            if not(visited[next]):
                visited[next] = 1
                right_next,left_next, = checkValue(next)
                if curr > next:
                    if left_curr != right_next:
                        next_signal = curr_signal * -1
                        rotation_T1(next,next_signal)
                        q.append((next,next_signal))
                elif curr < next:
                    if left_next != right_curr:
                        next_signal = curr_signal * -1
                        rotation_T1(next,next_signal)
                        q.append((next,next_signal))
                
    rotation_T1(start_number,signal)
    T = deepcopy(T1)
    # print()
total = 0
for i in range(4):
    if T[i][0] ==1:
        if i == 0:
            total +=1
        elif i==1:
            total+=2
        elif i==2:
            total+=4
        elif i==3:
            total+=8
print(total)

