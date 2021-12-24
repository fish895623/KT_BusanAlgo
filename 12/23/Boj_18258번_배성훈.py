import sys
from collections import deque


def input():
    return sys.stdin.readline()


if __name__ == "__main__":
    n = int(input())
    que = deque()
    for i in range(n):
        inputs = input().split()
        command = inputs[0]
        num = 0
        if len(inputs) > 1:
            num = inputs[1]
        if command == "push":
            que.append(num)
        elif command == "pop":
            if len(que) > 0:
                print(que.popleft())
            else:
                print(-1)
        elif command == "size":
            print(len(que))
        elif command == "empty":
            if len(que) == 0:
                print(1)
            else:
                print(0)
        elif command == "front":
            if len(que) > 0:
                print(que[0])
            else:
                print(-1)
        elif command == "back":
            if len(que) > 0:
                print(que[-1])
            else:
                print(-1)
