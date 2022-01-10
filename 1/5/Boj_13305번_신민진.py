N = int(input())

road = list(map(int, input().split()))
cost = list(map(int, input().split()))

# sum 초기화
sum = cost[0] * road[0]

# min_cost 초기화
if cost[0] <= cost[1]:
    min_cost = cost[0]

else :
    min_cost = cost[1]

sum += min_cost * road[1]

for i in range(2, N - 1):
    min_cost = min(min_cost, cost[i])
    sum += min_cost * road[i]

print(sum)