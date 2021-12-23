"""
https://www.acmicpc.net/problem/1874



"""
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

stack = []
result = []
stack_num = 1
check = True
for i in range(n):
    num = int(input())

    while stack_num <= num:
        stack.append(stack_num)
        result.append("+")
        stack_num += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    
    else:
        print("NO")
        check = False
        break
        

if check:
    for j in range(len(result)):
        print(result[j])

# data = deque()

# for _ in range(n):
#     data.append(int(input()))

# stack = []
# result = []
# if len(data) != 0:
#     d = data.popleft()

# for i in range(1, n+1):

    
#     stack.append(i)
#     result.append("+")

#     while stack[-1] == d:

#         result.append("-")
#         stack.pop()
#         if len(stack) == 0:
#             break
#         d = data.popleft()

# if len(stack) != 0:
#     print("NO")
# else:
#     for j in range(len(result)):
#         print(result[j])