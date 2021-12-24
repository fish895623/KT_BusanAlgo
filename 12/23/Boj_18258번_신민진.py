from sys import stdin
from collections import deque
num = int(stdin.readline())
q = deque([]) # 덱

for i in range(num):
    od = stdin.readline().split() # input 쪼개기 + 시간절약
    if od[0] == 'push':
        q.append(od[1])
    elif od[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft()) # 가장 앞에 있는 정수빼고 + 출력 -> popleft 사용!
    elif od[0] == 'size':
        print(len(q))
    elif od[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif od[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0]) # 큐의 가장 앞에 있는 정수 출력
    elif od[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1]) # 큐의 가장 뒤에 있는 정수 출력