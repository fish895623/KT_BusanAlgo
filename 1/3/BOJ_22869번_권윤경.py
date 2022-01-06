import sys
input = sys.stdin.readline

n, k =  map(int, input().split())
array = list(map(int, input().split()))
# print(array)
# n = 5
# k = 3
# array = [1, 5, 2, 1, 6]

dp = [sys.maxsize] * (n)
dp[0] = 99999

for i in range(n-1):
    if dp[i] != sys.maxsize:
        for j in range(i+1, n):
            if dp[j] == sys.maxsize:
                m = (j-i)*(1+ abs(array[i] - array[j]))
                if m <= k:
                    dp[j] = min(dp[j], m)
            # print(dp, (j-i)*(1+ abs(array[i] - array[j])))
            
print("YES" if (dp[n-1]!=sys.maxsize) else "NO")
# print(dp[n-1])