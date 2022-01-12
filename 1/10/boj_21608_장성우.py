"""
https://www.acmicpc.net/problem/21608

1. 첫번째 학생은 무조건 중간이다.
2. 

"""

import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n)]

for i in range(n):
    for j in range(n):
        graph[i].append(False)


data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

