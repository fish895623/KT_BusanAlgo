import sys
from itertools import combinations

sys.stdin = open(
    "2800",
    "r"
)

location = []
array = []
result = []

data = input()

# 괄호의 끝과 시작
for i in range(len(data)):
    if data[i] == "(":
        location.append(i)
    elif data[i] == ')':
        num = location.pop()
        array.append([i, num])

for i in range(1, len(array) + 1):
    for com in list(combinations(array, i)):
        res = []
        ans = []
        for a, b in com:
            res.append(a)
            res.append(b)
        res = sorted(res, reverse=True)

        data2 = list(data)
        for c in res:
            data2.pop(c)
        result.append("".join(data2))

for i in result:
    print(i)
