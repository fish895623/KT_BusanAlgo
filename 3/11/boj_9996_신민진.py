import sys
input = sys.stdin.readline

n = int(input())

first, second = input().split('*')

for _ in range(n):
    arr = input()
    # first, second가 같아서 겹칠경우도 고려
    if (len(first) + len(second)) <= len(arr) and \
        arr[:len(first)] == first and arr[-len(second):] == second:
        print('DA')
    else:
        print('NE')