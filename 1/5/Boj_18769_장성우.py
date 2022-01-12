"""
https://www.acmicpc.net/problem/18769
https://www.acmicpc.net/problem/1167
kruskal 알고리즘 이용해보자.
"""

"""

3 3개의 테스트케이스



2 3   r = 2 / c = 3   2행 3열


1 3   
3 1

i행, i+1 행에 놓인 c개의 서버를 상하로 연결하는 통신망설치
2 4 2 


2 2  r = 2 / c = 2 : 2행 2열

1
1

2 2

3 3   r = 3 / c = 3 : 3행 3열

1 2 
1 4
4 3

2 3 3
3 2 1


"""

t = int(input())

for _ in t:
    r, c = map(int, input().split())
    col_data = []
    row_data = []

    data_num = r * c
    parent = [0] * (data_num+1)

    for _ in range(c-1):
        col_data.append(list(map(int, input().split())))

    for _ in range(r-1):
        row_data.append(list(map(int, input().split())))

    for i in range(1, data_num+1):


