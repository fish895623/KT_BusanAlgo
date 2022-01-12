"""
https://www.acmicpc.net/problem/1913

방향전환했을 때 데이터가 있으면 방향전환하지말고 진행

"""


n = int(input())
find_n = int(input())


data = [[0] * n for i in range(n)]



# -------------------------------------------
# 처음 x, y 좌표 : (input값) -1 / 2
# dx, dy : 이동되는 좌표값 변경되는 값
# turn_time : 전환되는 방향 (초기값은 0을 넣는다.)
# 가장 처음 x, y의 값은 1로 넣어준다.
# -------------------------------------------
x = int((n-1) / 2)
y = int((n-1) / 2)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 , -1]
turn_time = 0

data[x][y] = 1
find_x, find_y = x, y


for i in range(2, n*n+1):

    # -------------------------------------------
    # Desc : 이동할 방향 찾기
    # 1. 방향 전환을 하고 이동했을 때 데이터가 없다면 해당 방향에 데이터를 집어넣는다.
    # 2. 만약 전환을 했을 때 데이터가 있다면 전환하기 전 방향으로 한번더 진행한다.
    # 3. 1, 2를 반복한다.
    # -------------------------------------------

    while True:
        
        nx = x + dx[turn_time]
        ny = y + dy[turn_time]
        
        if 0 <= nx <= n-1 and 0 <= ny <= n-1:

            # 아직 데이터가 없는 경우 turn_time에 다음 방향을 저장 한 후 나가기
            if data[nx][ny] == 0:
                turn_time = (turn_time + 1) % 4
                x, y = nx, ny
                break

            # 이동한 방향에 데이터가 있는경우 방향 전환하지말고 데이터를 넣는다.
            else:
                turn_time = (turn_time - 1) % 4
        else:
            turn_time = (turn_time + 1) % 4
            


    data[nx][ny] = i
    if i == find_n:
        find_x, find_y = nx+1, ny+1

for a in range(n):
    for b in range(n):
        print(data[a][b], end = " ")
    print()
print(f"{find_x} {find_y}")