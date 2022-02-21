"""
https://www.acmicpc.net/problem/5212

R*C

X = 땅
. = 바다

50년이 지나면 인접 3,4개가 바다면 잠긴다.

지도의 크기는 섬을 포함하는 가장 작은 직사각형이다. 

50년 후의 지도를 출력해주자.

바깥쪽으로 한개 더 감싸주어야한다.

자기 주변에 .이 몇개인지 확인해서 3개 이상이면 .으로 바꾸어주자.

이후 x의 x, y좌표를 확인해서 직사각형을만들어주고 해당 위치를 출력해주자.

"""
import copy

# 50년 뒤 사라지는 섬이면 False, 살아있는 섬이면 True를 리턴해준다.
def survive_land(x, y, data_map):

    if data_map[x+1][y] + data_map[x-1][y] + data_map[x][y+1] + data_map[x][y-1] >=3:
        return False
    else:
        return True


r, c = map(int, input().split())

# 바다 1
# 땅 0
# 지도와 지도 바깥부분도 바다로 감싸주자.
data_map = [[1] * (c+2) for i in range(r+2)]

# 땅의 위치를 저장하는 위치
land_loc = [] 


for i in range(r):
    data = input()

    for num, d in enumerate(data):
        # 땅이 들어오면 0으로 바꾸자.
        if d != ".":
            # 바깥부분을 추가해주었으므로 1씩 더해준다.
            data_map[i+1][num+1] = 0
            land_loc.append([i+1, num+1])

# 얕은 복사를 하면 이전데이터를 변경하면 같이 변하므로 깊은 복사를 진행한다.
new_map = copy.deepcopy(data_map)

# 땅의 위치 데이터를 받아와서 50년 뒤에 살아있는지 확인한다.
for x, y in land_loc:
    if not survive_land(x, y, data_map):
        new_map[x][y] = 1

# 직사각형 크기를 구한다.
INF = 1e9
min_x, min_y, max_x, max_y = INF,INF,-INF,-INF

# 땅인 경우만 생각해서 x, y의 최소 최대값 위치만 찾아준다.
for y, new_map_data in enumerate(new_map):
    for x in range(len(new_map_data)):
        if new_map[y][x] == 0:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

# 그래프 출력을 해준다.
for y in range(min_y, max_y+1):
    for i in new_map[y][min_x:max_x+1]:
        if i == 1:
            print(".", end="")
        else:
            print("X", end="")
    print()