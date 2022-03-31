import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
book = [input().strip() for _ in range(n)]
dic = Counter(book)
result = ''
cnt = 0
temp = []
for k,v in dic.items():
    if v > cnt:
        result = k
        cnt = v
    elif v == cnt:
        temp.append(result)
        temp.append(k)
        temp.sort()
        print(temp)
        result = temp[0]
        temp = []
print(result)