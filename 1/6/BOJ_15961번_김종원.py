# 15961번
# x부터 k 번재까지 연속으로 먹으면 할인된 정액 가격으로 제공된다.
# 쿠폰 n번 종류를 요청하면 무료로 먹을 수 있고 자료구조 속에 없어도 무료로 제공된다.

# 입력
# 첫번째 줄 접시 수 N. 초밥의 가짓 수 d, 연속해서 먹는 접시 수 k, 쿠폰번호

# N = 8
# d = 30
# k = 4
# cuppon = 30
# Nodes = []
# dish = [7,9,7,30,2,7,9,25]

import sys

N,d,k,cuppon = map(int,sys.stdin.readline().rstrip().split())
Nodes = []
dp = 0

for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    Nodes.append(n)

cnt =0
for i in range(0,N,1):
    dictDish = {cuppon:1}
    for j in range(i+1,i+k+1,1):    
        Right1 = (j)%N
        if Nodes[Right1] not in dictDish:
            dictDish[Nodes[Right1]] =1
    dp = max(dp,len(dictDish))
print(dp)


# 값 입력 완료.
# for i in range(N):
#     print()
#     print("Left : ",Nodes[i].leftNode, " left 값 : ",Nodes[Nodes[i].leftNode].curNode)
#     print("curtent : ",i, " curtent 값 : ",Nodes[i].curNode)
#     print("Right : ",Nodes[i].RightNode," Right 값 : ",Nodes[Nodes[i].RightNode].curNode)
#     print()