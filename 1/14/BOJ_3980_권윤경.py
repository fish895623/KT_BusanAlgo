def max_position(i,num):
    global maximum
    if i == 11:
        maximum = max(maximum, num)
        return

    for j in range(11):
        if visited[j]: continue
        if array[i][j] !=0 :
            visited[j] = 1
            max_position(i+1 , num+array[i][j])
            visited[j] = 0
    

import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    visited = [0] * 11
    maximum = 0 
    array = [list(map(int, input().split())) for _ in range(11)]
    max_position(0,0)
    print(maximum)