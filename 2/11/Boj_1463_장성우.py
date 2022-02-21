"""
https://www.acmicpc.net/problem/1463


1. 3으로 나누어지면 3으로 나눈다.
2. 2로 나누어지면 2로 나눈다.
3. 1을 뺀다.



"""

dp = [0] * 1000001

n = int(input())

i=2
while(i<=n):
    first, second, third = 1e9, 1e9, 1e9

    if i % 3 == 0:
        first = dp[i//3] + 1
    if i % 2 == 0:
        second = dp[i//2] + 1
    third = dp[i-1] + 1

    dp[i] = min(first, second, third)

    i += 1

print(dp[n])


# 더 좋은 방법

# info = {
#     1 : 0,
#     2 : 1,
# }


# n = int(input())

# def find_one(num):
#     if num in info:
#         return info[num]
    
#     m = 1 + min(find_one(num//2) + num % 2, find_one(num//3) + num % 3)
#     info[num] = m

#     return m


# print(find_one(n))