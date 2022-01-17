"""
https://www.acmicpc.net/problem/11365
"""

data = []
while True:
    d = input()
    if d == "END":
        break
    data.append(d[::-1])

for i in data:
    print(i)