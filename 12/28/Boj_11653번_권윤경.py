import sys
input = sys.stdin.readline
n = int(input())
for i in range(2,n+1):
    if n%i == 0:
        while n%i == 0:
            print(i)
            n = n // i