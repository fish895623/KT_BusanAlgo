import sys
input = sys.stdin.readline
# N, D, K, C = map(int, input().split())
# arr = [int(input()) for _ in range(N)]

# 딕셔너리 사용해보자...
N, D, K, C = 8, 50, 4, 7
arr = [2,7,9,25,7,9,7,30]
arr.extend(arr)
from collections import defaultdict
result = 0
dic = defaultdict(int)
dic[C] += 1
for i in range(N+K):
    dic[arr[i]] += 1
    if i >= K-1: 
        result = max(result, len(dic))
        dic[arr[i-K]] -= 1
        if dic[arr[i-K]] == 0:
            del dic[arr[i-K]]
        print(i-K)
print(result)
        

'''
# 역시나 시간초과
# 큐로 풀어보자..
N, D, K, C = 8, 50, 4, 7
arr = [2,7,9,25,7,9,7,30]
arr.extend(arr)
from collections import deque
arr = deque(arr)
arr2 = deque()
result = 0
for i in range(N):
    while len(arr2) != K:
        arr2.append(arr.popleft())
    result = max(result, len(set(arr2 + deque([C]))))
    arr2.popleft()
print(result)

'''
        
'''
시간 초과 ㅎㅎ..

N, D, K, C = 8, 50, 4, 7
arr = [2,7,9,25,7,9,7,30]
result = 0
for i in range(len(arr)):
    array = arr[i:i+K]
    if len(array) < K:
        array = array+ arr[0:(K-len(array))]
    array.append(C)
    print(array)
    result = max(result, len(set(array)))
print(result)

'''
