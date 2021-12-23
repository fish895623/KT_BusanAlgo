"""
https://www.acmicpc.net/problem/18258


큐 구현?

push : deque.append
pop : leftpop
size : len
empty : len
front : len, 0
back : len, len


"""

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

queue = deque()

for _ in range(n):

    text = input().split()

    if text[0] == "push":

        queue.append(text[1])
    elif text[0] == "pop":
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print('-1')
    elif text[0] ==  "size":
        print(len(queue))
    elif text[0] ==  "empty":
        if len(queue) == 0:
            print("1")
        else:
            print('0')

    elif text[0] == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print("-1")
    elif text[0] == "back":
        if len(queue) != 0:
            print(queue[len(queue)-1])
        else:
            print("-1")