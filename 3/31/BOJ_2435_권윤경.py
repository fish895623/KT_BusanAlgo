import sys
input = sys.stdin.readline
n, k = map(int, input().split())
temp = list(map(int, input().split()))
arr = []
for i in range(len(temp)-(k-1)):
    arr.append(sum(temp[i:i+k]))
print(max(arr))
