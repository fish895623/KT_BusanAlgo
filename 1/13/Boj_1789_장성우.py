"""
https://www.acmicpc.net/problem/1789


-> 1 ~ 19 sum (10제외) + 20

1 ~ n까지의 합 : n(n+1)/2


"""
import math

n = int(input()) * 2

result = int(math.sqrt(n))

while result ** 2 + result > n:
    result -= 1

print(result)

