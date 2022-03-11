"""
https://www.acmicpc.net/problem/9996

abc*c

=> abc -> x가 나와야함

데이터비교후 안빼면 답 안나옴

"""

import sys

input = sys.stdin.readline


def solution(n):
    yes, no = "DA", "NE"
    first, second = map(str, input().strip().split("*"))

    for _ in range(n):
        
        d = input().strip()
        
        if first == d[:len(first)]: # 처음 값과 같은지 확인
            d = d[len(first):] # 같다면 해당 값은 없애기
        else:
            print(no)
            continue # 만약 답이 아니면 다음 문자 확인

        if second == d[-len(second):]: # 두번째 값 같은지 확인
            print(yes)
        else:
            print(no)
    return 0

if __name__ == "__main__":
    n = int(input())
    solution(n)