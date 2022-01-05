# 돌의 갯수 N개
# 최대 힘 K
# A의 배열

# i번째에서 j 번째 돌로 이동할때
# (j - i ) * (1 + abs(A[i] - A[j]))
# rock, k  = 5, 3
# A = [1, 4, 1, 3, 1]
# # A = [1,4]
# A = [1, 5, 1, 4, 5]
# check = [0] * (len(A) +1)

# # import sys
# # rock, k = map(int,input().split())
# # A = list(map(int, input().split()))

# def cal(i,j,A):
#     return  (j - i ) * (1 + abs(A[i] - A[j]))
  
# k = threshold = 3
# 1 4 1 3 1
# 0 1 2 3 4
# [10001, 5, 2, 12, 20, 0]
# [10001, 5, 2, 12, 20, 0]


# A = [1, 5, 1, 3, 5]
# A = [1, 5, 2, 1, 6]

import sys
rock, threshold = map(int,input().split())
A = list(map(int, input().split()))


def cal(i,j,A):
    return  (j - i ) * (1 + abs(A[i] - A[j]))

i = 0
tp =[0] * (len(A)+1)
tp[0] = 10001
flag = True
while True:
    if i == len(A)-1:
        break
    m =0
    MINVal = 1000001
    for j in range(i+1,len(A)):
        t = cal(i,j,A)
        if MINVal > t and t <=threshold:
            MINVal = t
            m = j
        tp[j] = t
    # 최소값이 변동이 없다면 threshold 만큼 작거나 같은 같이 없기에 해당 징검다리는 통과하지 못한다.
    if MINVal == 1000001:   
        flag = False
        break
    else:
        # 최소값인 결과의 인덱스 번호를 i로 옮겨서 base 지점을 이전 i에서 최신 i로 이동한다.
        i = m
    # print(tp,i,m,MINVal)
if flag:
    # print(tp[len(A)-1])
    print("YES")
else:
    print("NO")
