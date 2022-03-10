import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

# 벽의 개수
bangs = [1] * (n-1)

for _ in range(m):
    a, b = map(int, input().split())
    # 범위 안의 벽 지우기
    for bang in range(a, b):
        bangs[bang] = 0

result = sum(bangs)
print(result+1) # 최종 방의 개수