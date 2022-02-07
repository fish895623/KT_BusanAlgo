import sys

sys.stdin = open(
    file="2346",
    mode='r'
)

N = int(input())
b = list(map(int, input().rsplit()))

idx = 0

index = [x for x in range(1, N + 1)]
result = []

tmp = b.pop(idx)
result.append(index.pop(idx))

while b:
    if tmp < 0:
        idx = (idx + tmp) % len(b)
    else:
        idx = (idx + tmp - 1) % len(b)

    tmp = b.pop(idx)
    result.append(index.pop(idx))

for i in result:
    print(i, end=" ")
