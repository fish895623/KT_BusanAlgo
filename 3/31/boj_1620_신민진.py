import sys
input = sys.stdin.readline

N, M = map(int, input().split())

names = []
nums = {}

for i in range(1, N+1):
    a = input().rstrip()
    names.append(a)
    nums[a] = i

for _ in range(M):
    b = input().rstrip()
    if b.isdigit():
        print(names[int(b)-1])
    else:
        print(nums[b])