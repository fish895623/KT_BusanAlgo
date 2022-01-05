# 돌의 갯수 N개
# 최대 힘 K
# A의 배열

# i를 계속 넘겨야 되는 군
# 넘기면서 dp 라는 배열을 조사하는데 이때 한가지라도 갈수 있다면 pass
# 아니면 NO

import sys
rock, threshold = map(int,input().split())
A = list(map(int, input().split()))

def cal(i,j,A):
    return  (j - i) * (1 + abs(A[i] - A[j]))

dp =[0] * (len(A))
dp[0] =1
for i in range(0,len(A)-1):
    # 주어진 공식으로 탐색된 정보가 있는 거만 탐색한다. 
    if dp[i] !=0:
        for j in range(i+1,len(A)):
            if dp[j] == 0:
                cost = cal(i,j,A)
                # print("I의 ",i,"번째 값은 : ",A[i], "J의 ",j,"번째 값은 : ",A[j] , " Cost : ",cost)
                if cost <= threshold:
                    dp[j] = cost
        if dp[-1] !=0:
            break
    # print(dp)
# 맨마지막 인덱스에 초기값이 아닌 값이 존재하면 탐색이 돼서 YES 아니면 NO.
if dp[-1] ==0:
    print("NO")
else:
    print("YES")


