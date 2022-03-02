import sys

################################################
sys.stdin = open(file="3/2/16236.txt", mode="r")
answer = 14
N = int(input())
K = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    K[i] = list(map(int, input().split()))
################################################
