# n개의 도시가 있다. 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 있다. 각 버스는 한번 사용할 때 필요한 비용있음
# 도시 A -> B로 가는데 필요한 비용의 최솟값. 
# 도시 n : 5, 버스 m : 14

import sys
from math import inf
input = sys.stdin.readline
n = int(input())
m = int(input())
array = [[inf for _  in range(n)] for _  in range(n)]
for _ in range(m):
    i, j, v = list(map(int,input().split()))
    array[i-1][j-1] = min(array[i-1][j-1], v)

for i in range(n):
    for j in range(n):
        if i == j:
            array[i][j] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if array[i][k] + array[k][j] < array[i][j]:
                array[i][j] = array[i][k] + array[k][j]

for i in range(n):
    for j in range(n):
        if array[i][j] == inf:
            print(0, end=" ")
        else:
            print(array[i][j], end=" ")
    print()