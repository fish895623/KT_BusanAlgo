"""
문제 링크 : https://www.acmicpc.net/problem/4811
푼 날짜 : 220322
문제 유형 : DP


풀이 : 

약 반알, 약 N개 담긴 병

첫날 병에서 약 하나 -> 반으로 쪼갠 후 하나를 먹고 나머지 하나는 병
이후 꺼냇을 때 반개면 먹고 하나면 쪼갠 후 먹는다

하나를 꺼낸 날은 W
반개를 꺼낸 날은 H를 보낸다

2N일이 지나면 길이가 2N인 문자열이 나온다. 이때 가능한 서로 다른 문자열의 갯수는?


"""

import sys

MAX_NUM = 31

input = sys.stdin.readline

def solution():
    # 31 * 31 행렬 생성
    dp = [[0] * MAX_NUM for _ in range(MAX_NUM)]

    for i in range(MAX_NUM):
        for j in range(i, MAX_NUM):
            if i == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]


    return dp

if __name__ == "__main__":

    dp = solution()


    while True:
        n = int(input())
        if n == 0:
            break
        print(dp[n][n])
        