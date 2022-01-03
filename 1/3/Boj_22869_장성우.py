"""
https://www.acmicpc.net/problem/22869

1) 1에서부터 갈 수 있는지를 알아야한다.

2) 갈 수 있는 곳의 dp를 1로 표시하며 끝까지 진행을 하자.

3) 어디 한곳이라도 갈 수 있으면 Yes 아니면 No출력

python으로 하면 시간초과 pypy3로 하면 통과..
어디선가 더 줄여야한다...


"""


import sys


input = sys.stdin.readline

n, m = map(int, input().split())

# -1은 아직 갈 수 없는 곳
dp = [-1] * (n+1)
dp[1] = 1

data = list(map(int, input().split()))

for first_num in range(1, n):
    if dp[first_num] == 1:
        for second_num in range(first_num+1, n+1):
            
            if dp[second_num] == -1:
                result = (second_num-first_num) * (1 + abs(data[first_num-1] - data[second_num-1]))

                if result <= m:
                    dp[second_num] = 1
            if dp[n] == 1:
                break
            
    if dp[n] == 1:
        break


if dp[n] == 1:
    print("YES")
else:
    print("NO")

# # 가고 싶은 곳 : n
# for second_num in range(2, n+1):

#     for first_num in range(1, second_num):
        
#         # 현재 있는 징검다리가 아직 갈 수 없는 경우 
#         # 그 전에 있는 다리들을 다 지나가보며 갈 수 있는지 판단한다.
#         if dp[second_num] == -1:
#             result = (second_num-first_num) * (1 + abs(data[first_num-1] - data[second_num-1]))

#             if result <= m:
#                 dp[second_num] = 1
#         # 만약 지날 수 있었으면 다음 징검다리로 넘어간다.
#         else:
#             break

# if dp[n] == 1:
#     print("YES")
# else:
#     print("NO")




# def find_val(first, second, data):
#     result = (second-first) * (1 + abs(data[first-1] - data[second-1]))

#     return result

# i = 1
# flag = False
# while True:
    
    
#     for j in range(i, n):
#         print(i, j)
#         j +=1 
#         if find_val(i, j, data) <= m:
#             i = j
            
#             break
    
#     if i == n+1:
#         print("YES")
#         flag = True
#         break
#     if i > n:
#         break
# if not flag:
#     print("NO")



# result = (n-1) * (1 + abs(data[0] - data[-1]))
# print(result)

# for i in range(1, n):

#     result = 1 + abs(data[i] - data[i-1])
#     print(result)
#     if result > m:
#         print("NO")
#         flag = False
#         break

    
