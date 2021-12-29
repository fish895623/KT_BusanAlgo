'''import math
from sys import stdin

input = stdin.readline
a, b = map(int, input().split())
print(math.gcd(a,b))
print(math.lcm(a,b)) -> math 모듈 사용'''

from sys import stdin

input = stdin.readline
a, b = map(int,input().split())

# 유클리드 호제법..ㅋ
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))