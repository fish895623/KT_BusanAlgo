"""
https://www.acmicpc.net/problem/15961

1. 회전초밥 벨트 상태
2. 메뉴에 있는 초밥 가짓수
3. 연속해서 먹는 접시의 개수
4. 쿠폰 번호

최대 초밥가짓수

1 2 3 2 a s d f l k a s d f j s a
1
2 1
3 2 1


"""
import sys
input = sys.stdin.readline

sushi_len = int(input())
sushi_kind = int(input())
con_eat = int(input())
coupon = int(input())

max_data = [0] * (sushi_len)

sushi_data = []
for _ in range(sushi_len):
    sushi_data.append(int(input()))

data = []
cou_check = 0

first_index = 0


for i in range(sushi_len+con_eat):

    if i > (sushi_len-1):
        i = (i-sushi_len-1)
    
    # 쿠폰 스시인 경우
    if sushi_data[i] == coupon:
        if cou_check == 1:
            for _ in range(data.index(sushi_data[i])):
                # 첫번째 값 없애기
                data.pop(0)
            first_index = i
            cou_check = 0
        else:
            cou_check = 1

    # 해당 스시를 이미 먹은 경우
    # 그 위치까지 일단 다 빼야한다.

    if sushi_data[i] in set(data):
        for _ in range(data.index(sushi_data[i])):
            # 첫번째 값 없애기
            data.pop(0)
        first_index = i

    # 없는경우 first_index는 그대로 가야한다,.

    # 더해줘야한다.
    for k in range(first_index, i+1):
        max_data[k]+= 1

    if max_data[i] == con_eat:
        first_index = i

    data.append(sushi_data[i])



    count = 0
