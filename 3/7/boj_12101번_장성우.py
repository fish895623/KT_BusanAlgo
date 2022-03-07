"""
https://www.acmicpc.net/problem/12101


"""
import sys

input = sys.stdin.readline

def solution(n, result):
    global cnt
    if sum(result) == n:
        cnt += 1
    elif sum(result) > n:
        return
    # cnt가 k보다 커진경우 return
    if cnt > k:
        return
    # cnt가 원하는k가 나왔을 경우 print하고 return
    if cnt == k:
        print("+".join(map(str, result)))
        exit(0)

    for i in range(1,4):
        result.append(i)
        solution(n, result)
        result.pop()



if __name__ == "__main__":
    cnt = 0
    n, k = map(int, input().split())
    result = []
    solution(n, result)
    if cnt < k:
        print("-1")

