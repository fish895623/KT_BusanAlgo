import sys

try:
    sys.stdin = open("3/15/14501.txt", "r")
except:
    pass

n = int(input())
t = []
p = []
c = []

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    c.append(b)
c.append(0)


for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        # print(c[i + 1])
        c[i] = c[i + 1]
    else:
        # print(c[i], c[i + 1], p[i], c[i + t[i]], t[i])
        c[i] = max(c[i + 1], p[i] + c[i + t[i]])

print(c[0])
