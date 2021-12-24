"""
https://www.acmicpc.net/problem/14425
문자열 집합



"""
import sys

n, m = map(int, input().split())


data = []
for _ in range(n):
    data.append(sys.stdin.readline().rstrip())

count = 0

for _ in range(m):
    if sys.stdin.readline().rstrip() in data:
        count += 1

print(count)