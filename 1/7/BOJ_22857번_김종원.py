# BOJ 22857번

# 길이가 N인 S 수열이 있다. 
# 수열에서 원하는 위치에 있는 수를 골라 최대 K번 삭제할 수 있다.

# 1 2 3 4 5 6 7 8  --> 4를 지움
# 1 2 3 5 6 7 8
N, k = 10,2
s = [1,4,3,2,5,8,7,6,10,12]

import sys

# N,k = map(int,sys.stdin.readline().rstrip().split())
# s= list(map(int,sys.stdin.readline().rstrip().split()))

s.pop(k-1)

lis = [0] * (N-1)

for i in range(0,N-1):
    if s[i] %2 ==0:
        if i == 0:
            lis[0] = 1
    else:
        lis[i] = 0
        continue
    for j in range(0,i):
        if s[i] > s[j]:
            lis[i] = max(lis[i], lis[j]+1)

print(lis)
print(max(lis))