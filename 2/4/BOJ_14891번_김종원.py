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

# 톱니바퀴 A와 톱니바퀴 B의 왼쪽 값과 오른쪽 값을 비교할때 회전을 했어도 원본 값이 변경이 안되도록 깊은 복사로 원본 값이 훼손 되지 않게 하였다.
T1 = deepcopy(T)


# 톱니바퀴 탐색 가능한 범위
graph = [[],[2], [1,3], [2,4], [3]]

# 탐색을 시작하는 노드 번호
order_list = []

k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    p1,p2 = map(int,sys.stdin.readline().rstrip().split())
    order_list.append([p1,p2])

# T1 리스트에 대해서 회전을 해야한다면 회전하여 리스트 값을 변경하는 함수
def rotation_T1(choice_t, signal):
    if signal == -1:
        tmp = T1[choice_t-1].pop(0)
        T1[choice_t-1].append(tmp)

    elif signal == 1:
        tmp = T1[choice_t-1].pop()
        T1[choice_t-1].insert(0,tmp)

# T1이 회전이 되어도 원본값을 가져와야하니 T1리스트이 왼쪽 오른쪽 갑이 아니라 원본 톱니바퀴의 왼쪽과 오른쪽 값을 리턴한다.
def checkValue(choice):
    return (T[choice-1][2],T[choice-1][-2])


# BFS로 탐색
for start_number, signal in order_list:
    # 1회 탐색이 끝나면 다시 탐색해야하니 visited 노드 정보를 모두 0으로 초기화
    visited = [0,0,0,0,0]
    visited[start_number] = 1

    q = deque()
    q.append((start_number,signal))
    while q:
        curr, curr_signal = q.popleft()
        # 현재 톱니바퀴의 왼쪽과 오른쪽 값을 가져옴.
        right_curr, left_curr = checkValue(curr)
        # print(curr,end = " -> ")  # 탐색하는 노드 정보 
        for next in graph[curr]:
            # 방문하지 않은 노드이면 탐색
            if not(visited[next]):
                visited[next] = 1
                # 방문하지 않은 톱니바퀴의 왼쪽과 오른쪽값을 가져옴
                right_next,left_next, = checkValue(next)
                # 현재 톱니바퀴 번호와 방문하는 톱니바퀴 번호에 따라 현재 왼쪽과 방문 하는 오른쪽 정보 또는 현재 오른쪽과 방문하는 왼쪽 정보를
                # 비교하는게 다르니 현재 톱니바퀴 번호가 다음번호보다 작으면 어떤 조건으로 탐방하라고 조건절을 기입하였다.
                if curr > next:
                    # 왼쪽과 오른쪽 값이 서로 다르면 N과 S 극으로 방문해야하는 톱니가 회전을 해야하기에 T1 리스트에 대해서 회전시키고
                    # 회전을 하였으니 탐색을 하라고 q에 추가한다.
                    # 톱니가 회전을 하지 않으면 굳이 탐색을 할 필요가 없으니 q에 추가하지 않았다.
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
    # 탐색이 끝난 톱니바퀴에 대해 T1으로 교체해서 k번이 될때까지 탐색한다.
    T = deepcopy(T1)
    # print()
    
# 12시 방향이 S극인 것에 대한 합 구하기
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

