"""
https://www.acmicpc.net/problem/1106


"""

import sys
INF = 1e9
input = sys.stdin.readline


# C : 적어도 늘어날 고객 수 / n : 도시의 개수
c, n = map(int, input().split())

# # 최대 20개의 도시의 개수
# city = [[-1] for i in range(21)]
city = []

# 명수당 필요한 가격
min_cost = [INF] * (c+100)

min_cost[0] = 0


for _ in range(n):

    # cost, cus
    city.append(list(map(int, input().split())))

# cost 순서 작은 순서로 정리
city_sort = sorted(city, key = lambda x: x[0])



"""
인원수에 따른 최솟값

"""

for cost, cus in city_sort:
    
    # cost 작은순서대로 들어옴

    for i in range(cus, c+100):

        min_cost[i] = min(min_cost[i-cus] + cost, min_cost[i])

print(min(min_cost[c:]))
