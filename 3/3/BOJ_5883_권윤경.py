n = int(input())
arr = [int(input()) for i in range(n)]
result = 1
from collections import deque
for target in set(arr):
    tmp = []
    queue = deque(arr)
    max_sum = 1
    while queue:
        t = queue.popleft()
        if target != t:
            if len(tmp) !=0 :
                if tmp[-1] == t:
                    max_sum += 1
                    result = max(result, max_sum)
                else:
                    max_sum = 1
            tmp.append(t)
print(result)
                
                
    