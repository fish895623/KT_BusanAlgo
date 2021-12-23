"""
https://www.acmicpc.net/problem/1874



"""
from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

data = deque()

for _ in range(n):
    data.append(int(input()))

stack = []
result = []
d = data.popleft()

for i in range(1, n+1):

    
    stack.append(i)
    result.append("+")

    while stack[-1] == d:

        result.append("-")
        stack.pop()
        if len(stack) == 0:
            break
        d = data.popleft()

if len(stack) != 0:
    print("NO")
else:
    for j in range(len(result)):
        print(result[j])






