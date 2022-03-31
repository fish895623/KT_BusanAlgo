import sys

n,m  = map(int,sys.stdin.readline().strip().split())

poketmon_info = {}
poketmon_list = []
for i in range(n):
    name = sys.stdin.readline().strip()
    poketmon_list.append(name)
    poketmon_info[name] = i+1


qestion = []
for _ in range(m):
    q1 = sys.stdin.readline().strip()
    if q1 not in poketmon_info:
        print(poketmon_list[int(q1) -1])
    else:
        print(poketmon_info[q1])