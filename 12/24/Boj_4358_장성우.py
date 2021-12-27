"""
https://www.acmicpc.net/problem/4358


"""

from collections import defaultdict
import sys

input= sys.stdin.readline

dic = defaultdict(int)
count = 0

while True:

    name = input().rstrip()

    if not name:
        break

    dic[name] += 1
    count += 1

sort_dic = sorted(dic.items(), key = lambda x: x[0])

for d in sort_dic:
    
    print(d[0], end = " ")
    print("{:.4f}".format(round((int(dic[d[0]]) / count) * 100 , 4))     )