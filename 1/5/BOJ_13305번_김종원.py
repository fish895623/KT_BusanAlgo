# 13305번
# 도시 4개
# 거리 2 3 1
# 1리터당 주유 가격 5 2 4 1
# --------

dp = [0] * 5

# 2 + 3 +1 = 7km가야한다.

price = [5, 2, 4, 1]
dist = [0, 2, 3, 1]

oil ,buyOil,money = 0, 0, 0

total = sum(dist)
for i in range(4):
    for j in range(i,4-1):
        if buyOil ==0:
            buyOil = abs(total - dist[-j])
            money = price[i]  * buyOil # 충전.
            total = total - buyOil
    break
print(money,total,buyOil)
