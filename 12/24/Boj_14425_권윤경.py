from sys import stdin
n, m = list(map(int, stdin.readline().split()))
s = []
for i in range(n+m):
	s.append(stdin.readline())
    
from collections import Counter
li = dict(Counter(s[n:]))

result = 0
for a2 in s[:n]:
    if a2 in li:
        result += li[a2]
print(result)