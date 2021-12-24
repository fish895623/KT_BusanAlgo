# 4358번

# 생태학에서 나무의 분포도를 측정하는 것은 중요하다. 
# 그러므로 당신은 미국 전역의 나무들이 주어졌을 때,
# 각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램을 만들어야 한다.

import sys
input = sys.stdin.readline

trees ={}
c =0
while True:
    t = input().strip()
    if len(t) ==0:
        break
    if t not in trees:
        trees[t] = 1
    else:
        trees[t] +=1
    c+=1

# 딕셔너리 key 정보를 정렬 시켜서 순서대로 출력되게 조건을 마련한다.
trees_sort = sorted(trees.keys())
for name in trees_sort:
    val = round(trees[name]/c *100,4)
    # 소수점 네번째까지 문자열로 나타내야 해서 format 함수를 사용해 나타냈다.
    print("{} {:.4f}".format(name,val))
    


