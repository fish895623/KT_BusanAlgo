import sys

try:
    sys.stdin = open("3/11/9996.txt", "r")
except:
    pass

N = int(input())
REGEX = input().split("*")
for _ in range(N):
    INPUT = input()
    if (
        INPUT[: len(REGEX[0])] == REGEX[0]
        and INPUT[-len(REGEX[1]) :] == REGEX[1]
        and len("".join(REGEX)) <= len(INPUT)  # 필터식이 검색문자열을 넘으면 안됨 이거 ㅈㄴ 함정
    ):
        print("DA")
    else:
        print("NE")
