import sys
input = sys.stdin.readline

# n = int(input())
# m = list(map(int, input().split()))
# k = list(map(int, input().split()))

n = 4 # 도시 수
m = [2,3,1] # 거리 수
k = [5,2,4,1] # 주유소 가격

cost = k[0]
result = 0

for i in range(n-1):
    if cost >= k[i]:
        result += k[i]*m[i]
        cost = k[i]

    else:
        result += cost*m[i]
print(result)