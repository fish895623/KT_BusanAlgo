from sys import stdin

n = int(stdin.readline())
s = []
for i in range(n):
	s.append(stdin.readline())
    
from collections import deque

queue = deque()

for i in range(n):
    if s[i].split()[0] == 'push':
        queue.append(s[i].split()[1])
        
    elif s[i].split()[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            p = queue.popleft()
            print(p)
        
    elif s[i].split()[0] == 'size':
        print(len(queue))
        
    elif s[i].split()[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif s[i].split()[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
        
    elif s[i].split()[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
        
    else:
        break
    