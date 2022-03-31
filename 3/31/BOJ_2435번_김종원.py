import sys

n, m = map(int, sys.stdin.readline().strip().split())

temp = list(map(int, sys.stdin.readline().strip().split()))

value_list = []
for i in range(n-m+1):
    total = 0
    for j in range(i,i+m):
        total += int(temp[j])
    value_list.append(total)

print(max(value_list))

