"""
https://www.acmicpc.net/problem/14594


"""

import sys
input = sys.stdin.readline


def solution(n, m):

    data = [0] * (n+1)
    
    for i in range(m):
        a, b = map(int, input().split())

        for j in range(a, b):
            data[j] = 1


    return n - data.count(1)
if __name__ == "__main__":
    n = int(input())
    m = int(input())


    print(solution(n, m))