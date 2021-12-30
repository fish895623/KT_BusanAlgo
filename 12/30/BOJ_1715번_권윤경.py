# 맞은 풀이
n = int(input())
s = [int(input()) for i in range(n)]

import heapq
result = 0
heapq.heapify(s)
while len(s)>1 :
    n1 = heapq.heappop(s)
    n2 = heapq.heappop(s)
    result += n1 + n2
    heapq.heappush(s, n1+n2)
print(result)


'''
# 틀린 풀이 (메모리 초과 --> 우선순위 큐 안써서)
n = int(input())
s = [int(input()) for i in range(n)]
result = 0
for i in range(len(s)-1):
    result += s[i] + s[i+1]
    s[i+1] = result
print(result)
'''