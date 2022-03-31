import sys
input = sys.stdin.readline
n = int(input())
p = list(map(int, input().split()))
p.sort()
result = 0
tmp = 0
for i in p:
    tmp += i
    result += tmp
print(result)