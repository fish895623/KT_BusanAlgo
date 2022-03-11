"""
https://www.acmicpc.net/problem/14595

1. dp => 자기자신을 가르키는 데이터 (O(n))
2. 데이터 받아오면서 dp[a] = b (b는 max값) (O(n))
3. 데이터 처음부터 보면서 자기 자신을 가르키면 cnt += 1
4. 데이터가 다른 값을 가르키게되면 현재 max_val = 가 자기자신인지 확인 자기자신이면 cnt +=1

O(n)으로 완료가능
=> n이 1억까진 안되더라도 1000만까지는 가능
"""

import sys

input = sys.stdin.readline


def solution(n):
    cnt = 0
    max_val = 1
    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = i
    
    # 부시는 것 진행
    for _ in range(int(input())):
        a, b = map(int, input().split())

        dp[a] = max(dp[a], b) # a ~ b까지 파괴

    for room in range(1,n+1):
        if dp[room] < max_val:
            pass
        elif dp[room] == room:
            cnt += 1
        # elif dp[room] == max_val:
        #     cnt += 1
        else:
            max_val = max(max_val, dp[room])
            
    return cnt

if __name__ == "__main__":
    n = int(input())

    print(solution(n))