# 2156번

n = 6
grapes = [6,10,13,9,8,1]
dp = [0] * n

# import sys
# n = int(input())
# grapes = []
# dp = [0] * n

# for i in range(n):
#     n1 = int(sys.stdin.readline().rstrip())
#     grapes.append(n1)

dp[0] = grapes[0]
dp[1] = grapes[1]



# 6 10, 9,8
# 10 13 8 1
# 13 9 1
# 9 8 

# dp = [0] * n

# 0 1 2 3 4 5
# 0 1   3 4 
# 0   2   4
#   1   3   5
#   1 2   4 5
#     2 3   5
#       3 4 
